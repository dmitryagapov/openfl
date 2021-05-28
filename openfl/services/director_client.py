import logging
import os
import shutil

import grpc

from openfl.protocols import preparations_pb2
from openfl.protocols import preparations_pb2_grpc

logger = logging.getLogger(__name__)


class ShardDirectorClient:
    def __init__(self, director_uri, shard_name) -> None:
        self.shard_name = shard_name
        channel = grpc.insecure_channel(director_uri)
        self.stub = preparations_pb2_grpc.FederationDirectorStub(channel)

    def report_shard_info(self, data_path) -> bool:
        logger.info('Send report AcknowledgeShard')
        # True considered as successful registration
        shard_info = preparations_pb2.ShardInfo(
            shard_description=data_path,
            # n_samples = len(shard_descriptor),
            sample_shape=1,
            target_shape=1
        )

        shard_info.node_info.CopyFrom(self._get_node_info())

        acknowledgement = self.stub.AcknowledgeShard(shard_info)
        return acknowledgement.accepted

    # def is_new_experiment_avalable(self):
    #     logger.info('Send IsNewExperimentAvalable request')
    #     response = self.stub.IsNewExperimentAvalable(
    #         preparations_pb2.NewExperimentAvalableRequest())
    #     logger.info(f'Response received: {response}')
    #     return response.is_available

    def get_experiment_data(self):
        logger.info('Send WaitExperiment request')
        response_iter = self.stub.WaitExperiment(self._get_experiment_data())
        logger.info(f'WaitExperiment response has received')
        # TODO: seperate into two resuests (get status and get file)
        experiment_name = None
        for response in response_iter:
            experiment_name = response.experiment_name
        if not experiment_name:
            raise Exception('No experiment')
        logger.info(f'Request experiment {experiment_name}')
        request = preparations_pb2.GetExperimentDataRequest(
            experiment_name=experiment_name,
            collaborator_name=self.shard_name
        )
        response_iter = self.stub.GetExperimentData(request)

        self.create_workspace(experiment_name, response_iter)

        return experiment_name

    @staticmethod
    def create_workspace(experiment_name, response_iter):
        if os.path.exists(experiment_name):
            shutil.rmtree(experiment_name)
        os.makedirs(experiment_name)

        arch_name = f'{experiment_name}/{experiment_name}' + '.zip'
        with open(arch_name, 'wb') as content_file:
            for response in response_iter:
                logger.info(f'Size: {response.size}')
                if response.size == len(response.npbytes):
                    content_file.write(response.npbytes)
                else:
                    raise Exception('Broken archive')

        shutil.unpack_archive(arch_name, experiment_name)

    def _get_experiment_data(self):
        yield preparations_pb2.WaitExperimentRequest(collaborator_name=self.shard_name)

    def _get_node_info(self):
        return preparations_pb2.NodeInfo(name=self.shard_name)


class DirectorClient:
    def __init__(self, director_uri) -> None:
        channel = grpc.insecure_channel(director_uri)
        self.stub = preparations_pb2_grpc.FederationDirectorStub(channel)

    def set_new_experiment(self, name, col_names, arch_path):
        logger.info('SetNewExperiment')
        with open(arch_path, 'rb') as arch:
            def st():
                max_buffer_size = (2 * 1024 * 1024)
                chunk = arch.read(max_buffer_size)
                while chunk != b"":
                    if not chunk:
                        raise StopIteration
                    # TODO: add hash or/and size to check
                    experiment_info = preparations_pb2.ExperimentInfo(
                        name=name,
                        collaborator_names=col_names,
                    )
                    experiment_info.experiment_data.size = len(chunk)
                    experiment_info.experiment_data.npbytes = chunk
                    yield experiment_info
                    chunk = arch.read(max_buffer_size)

            resp = self.stub.SetNewExperiment(st())
            return resp


