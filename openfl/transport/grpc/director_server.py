# Copyright (C) 2020-2021 Intel Corporation
# SPDX-License-Identifier: Apache-2.0

"""Director server."""

import asyncio
import logging
import uuid
from pathlib import Path

from grpc import aio
from grpc import ssl_server_credentials

from openfl.pipelines import NoCompressionPipeline
from openfl.protocols import director_pb2
from openfl.protocols import director_pb2_grpc
from openfl.protocols.utils import construct_model_proto
from openfl.protocols.utils import deconstruct_model_proto

logger = logging.getLogger(__name__)


class DirectorGRPCServer(director_pb2_grpc.FederationDirectorServicer):
    """Director transport class."""

    def __init__(self, *, director_cls, tls: bool = True,
                 root_ca: str = None, key: str = None, cert: str = None,
                 listen_ip='[::]', listen_port=50051, **kwargs) -> None:
        """Initialize a director object."""
        # TODO: add working directory
        super().__init__()

        self.listen_addr = f'{listen_ip}:{listen_port}'
        self.tls = tls
        self.root_ca = None
        self.key = None
        self.cert = None
        self._fill_certs(root_ca, key, cert)
        self.server = None
        self.director = director_cls(
            tls=self.tls,
            root_ca=self.root_ca,
            key=self.key,
            cert=self.cert,
            **kwargs
        )

    def _fill_certs(self, root_ca, key, cert):
        """Fill certificates."""
        if self.tls:
            if not (root_ca and key and cert):
                raise Exception('No certificates provided')
            self.root_ca = Path(root_ca).absolute()
            self.key = Path(key).absolute()
            self.cert = Path(cert).absolute()

    def get_sender(self, context):
        """
        Get sender name.

        Args:
            context: The gRPC context

        Returns:
            If TLS is used return sender name from certificate
            If TLS is unused return default name 'unauthorized_sender'
        """
        sender = 'unauthorized_sender'
        if self.tls:
            sender = context.auth_context()['x509_common_name'][0].decode('utf-8')
        return sender

    def start(self):
        """Launch the director GRPC server."""
        asyncio.run(self._run())

    async def _run(self):
        channel_opt = [('grpc.max_send_message_length', 512 * 1024 * 1024),
                       ('grpc.max_receive_message_length', 512 * 1024 * 1024)]
        self.server = aio.server(options=channel_opt)
        director_pb2_grpc.add_FederationDirectorServicer_to_server(self, self.server)

        if not self.tls:
            self.server.add_insecure_port(self.listen_addr)
        else:
            with open(self.key, 'rb') as f:
                key_b = f.read()
            with open(self.cert, 'rb') as f:
                cert_b = f.read()
            with open(self.root_ca, 'rb') as f:
                root_ca_b = f.read()
            server_credentials = ssl_server_credentials(
                ((key_b, cert_b),),
                root_certificates=root_ca_b,
                require_client_auth=True
            )
            self.server.add_secure_port(self.listen_addr, server_credentials)
        logger.info(f'Starting server on {self.listen_addr}')
        await self.server.start()
        await self.server.wait_for_termination()

    async def AcknowledgeShard(self, shard_info, context):  # NOQA:N802
        """Receive acknowledge shard info."""
        logger.info(f'AcknowledgeShard request has got: {shard_info}')
        is_accepted = self.director.acknowledge_shard(shard_info)
        reply = director_pb2.ShardAcknowledgement(accepted=is_accepted)

        return reply

    async def SetNewExperiment(self, stream, context):  # NOQA:N802
        """Request to set new experiment."""
        logger.info(f'SetNewExperiment request has got {stream}')
        # TODO: add streaming reader
        data_file_path = Path(str(uuid.uuid4())).absolute()
        with open(data_file_path, 'wb') as data_file:
            async for request in stream:
                if request.experiment_data.size == len(request.experiment_data.npbytes):
                    data_file.write(request.experiment_data.npbytes)
                else:
                    raise Exception('Bad request')
        sender = self.get_sender(context)

        tensor_dict = None
        if request.model_proto:
            tensor_dict, _ = deconstruct_model_proto(request.model_proto, NoCompressionPipeline())

        is_accepted = await self.director.set_new_experiment(
            experiment_name=request.name,
            sender=sender,
            tensor_dict=tensor_dict,
            collaborator_names=request.collaborator_names,
            data_file_path=data_file_path
        )

        logger.info('Send response')
        return director_pb2.SetNewExperimentResponse(accepted=is_accepted)

    async def GetTrainedModel(self, request, context):  # NOQA:N802
        """RPC for retrieving trained models."""
        logger.info('Request GetTrainedModel has got!')

        if request.model_type == director_pb2.GetTrainedModelRequest.BEST_MODEL:
            model_type = 'best'
        elif request.model_type == director_pb2.GetTrainedModelRequest.LAST_MODEL:
            model_type = 'last'
        else:
            logger.error('Incorrect model type')
            return director_pb2.TrainedModelResponse()

        sender = self.get_sender(context)
        trained_model_dict = self.director.get_trained_model(
            experiment_name=request.experiment_name,
            sender=sender,
            model_type=model_type
        )

        if trained_model_dict is None:
            return director_pb2.TrainedModelResponse()

        model_proto = construct_model_proto(trained_model_dict, 0, NoCompressionPipeline())

        return director_pb2.TrainedModelResponse(model_proto=model_proto)

    async def GetExperimentData(self, request, context):  # NOQA:N802
        """Receive experiment data."""
        # TODO: add size filling
        # TODO: add experiment name field
        # TODO: rename npbytes to data
        data_file_path = self.director.get_experiment_data(request.experiment_name)
        max_buffer_size = (2 * 1024 * 1024)
        with open(data_file_path, 'rb') as df:
            while True:
                data = df.read(max_buffer_size)
                if len(data) == 0:
                    break
                yield director_pb2.ExperimentData(size=len(data), npbytes=data)

    async def WaitExperiment(self, request_iterator, context):  # NOQA:N802
        """Request for wait an experiment."""
        logger.info('Request WaitExperiment has got!')
        async for msg in request_iterator:
            logger.info(msg)
            experiment_name = await self.director.wait_experiment(msg.collaborator_name)
            logger.info(f'Experiment {experiment_name} was prepared')

            yield director_pb2.WaitExperimentResponse(experiment_name=experiment_name)

    async def GetDatasetInfo(self, request, context):  # NOQA:N802
        """Request the info about target and sample shapes in the dataset."""
        logger.info('Request GetDatasetInfo has got!')

        sample_shape, target_shape = self.director.get_dataset_info()
        resp = director_pb2.ShardInfo(
            sample_shape=sample_shape,
            target_shape=target_shape
        )
        return resp

    async def StreamMetrics(self, request, context):  # NOQA:N802
        """Request to stream metrics from the aggregator to frontend."""
        logger.info(f'Request StreamMetrics for {request.experiment_name} experiment has got!')
        metrics = self.director.stream_metrics(
            experiment_name=request.experiment_name,
            sender=request.header.sender
        )
        for metric_dict in metrics:
            if metric_dict is None:
                await asyncio.sleep(5)
                continue
            yield director_pb2.StreamMetricsResponse(**metric_dict)

    async def RemoveExperimentData(self, request, context):  # NOQA:N802
        """Remove experiment data RPC."""
        sender = self.get_sender(context)
        self.director.remove_experiment_data(
            experiment_name=request.experiment_name,
            sender=sender,
        )
        response = director_pb2.RemoveExperimentResponse(acknowledgement=True)
        return response

    async def CollaboratorHealthCheck(self, request, context):  # NOQA:N802
        """Accept health check from envoy."""
        logger.debug(f'Request CollaboratorHealthCheck has got: {request}')
        is_accepted = self.director.collaborator_health_check(
            collaborator_name=request.name,
            is_experiment_running=request.is_experiment_running,
            valid_duration=request.valid_duration.seconds,
        )

        return director_pb2.CollaboratorHealthCheckResponse(accepted=is_accepted)

    async def GetEnvoys(self, request, context):  # NOQA:N802
        """Get a status information about envoys."""
        envoy_infos = self.director.get_envoys()

        return director_pb2.GetEnvoysResponse(envoy_infos=envoy_infos)
