# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: director.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import openfl.protocols.federation_pb2 as federation__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='director.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x0e\x64irector.proto\x1a\x10\x66\x65\x64\x65ration.proto\"U\n\x08NodeInfo\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0e\n\x06\x61\x64ress\x18\x02 \x01(\t\x12\x16\n\x0e\x63uda_available\x18\x03 \x01(\x08\x12\x13\n\x0bmemory_size\x18\x04 \x01(\r\"\x83\x01\n\tShardInfo\x12\x1c\n\tnode_info\x18\x01 \x01(\x0b\x32\t.NodeInfo\x12\x19\n\x11shard_description\x18\x02 \x01(\t\x12\x11\n\tn_samples\x18\x03 \x01(\x04\x12\x14\n\x0csample_shape\x18\x04 \x03(\t\x12\x14\n\x0ctarget_shape\x18\x05 \x03(\t\"(\n\x14ShardAcknowledgement\x12\x10\n\x08\x61\x63\x63\x65pted\x18\x01 \x01(\x08\"2\n\x15WaitExperimentRequest\x12\x19\n\x11\x63ollaborator_name\x18\x01 \x01(\t\"1\n\x16WaitExperimentResponse\x12\x17\n\x0f\x65xperiment_name\x18\x01 \x01(\t\"N\n\x18GetExperimentDataRequest\x12\x17\n\x0f\x65xperiment_name\x18\x01 \x01(\t\x12\x19\n\x11\x63ollaborator_name\x18\x02 \x01(\t\"/\n\x0e\x45xperimentData\x12\x0c\n\x04size\x18\x01 \x01(\r\x12\x0f\n\x07npbytes\x18\x02 \x01(\x0c\"\x86\x01\n\x0e\x45xperimentInfo\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x1a\n\x12\x63ollaborator_names\x18\x02 \x03(\t\x12(\n\x0f\x65xperiment_data\x18\x03 \x01(\x0b\x32\x0f.ExperimentData\x12 \n\x0bmodel_proto\x18\x04 \x01(\x0b\x32\x0b.ModelProto\"I\n\x18SetNewExperimentResponse\x12\x10\n\x08\x61\x63\x63\x65pted\x18\x01 \x01(\x08\x12\x1b\n\x13tensorboard_address\x18\x02 \x01(\t\"\x1b\n\x19GetRegisterdShardsRequest\"<\n\x1aGetRegisterdShardsResponse\x12\x1e\n\nshard_info\x18\x01 \x03(\x0b\x32\n.ShardInfo\"|\n\x16GetTrainedModelRequest\x12\x35\n\nmodel_type\x18\x01 \x01(\x0e\x32!.GetTrainedModelRequest.ModelType\"+\n\tModelType\x12\x0e\n\nBEST_MODEL\x10\x00\x12\x0e\n\nLAST_MODEL\x10\x01\"8\n\x14TrainedModelResponse\x12 \n\x0bmodel_proto\x18\x01 \x01(\x0b\x32\x0b.ModelProto\"\x16\n\x14GetShardsInfoRequest\"/\n\x14StreamMetricsRequest\x12\x17\n\x0f\x65xperiment_name\x18\x01 \x01(\t\"{\n\x15StreamMetricsResponse\x12\x15\n\rmetric_origin\x18\x01 \x01(\t\x12\x11\n\ttask_name\x18\x02 \x01(\t\x12\x13\n\x0bmetric_name\x18\x03 \x01(\t\x12\x14\n\x0cmetric_value\x18\x04 \x01(\x02\x12\r\n\x05round\x18\x05 \x01(\r2\xaf\x04\n\x12\x46\x65\x64\x65rationDirector\x12\x37\n\x10\x41\x63knowledgeShard\x12\n.ShardInfo\x1a\x15.ShardAcknowledgement\"\x00\x12G\n\x0eWaitExperiment\x12\x16.WaitExperimentRequest\x1a\x17.WaitExperimentResponse\"\x00(\x01\x30\x01\x12\x43\n\x11GetExperimentData\x12\x19.GetExperimentDataRequest\x1a\x0f.ExperimentData\"\x00\x30\x01\x12\x42\n\x10SetNewExperiment\x12\x0f.ExperimentInfo\x1a\x19.SetNewExperimentResponse\"\x00(\x01\x12O\n\x12GetRegisterdShards\x12\x1a.GetRegisterdShardsRequest\x1a\x1b.GetRegisterdShardsResponse\"\x00\x12\x34\n\rGetShardsInfo\x12\x15.GetShardsInfoRequest\x1a\n.ShardInfo\"\x00\x12\x43\n\x0fGetTrainedModel\x12\x17.GetTrainedModelRequest\x1a\x15.TrainedModelResponse\"\x00\x12\x42\n\rStreamMetrics\x12\x15.StreamMetricsRequest\x1a\x16.StreamMetricsResponse\"\x00\x30\x01\x62\x06proto3'
  ,
  dependencies=[federation__pb2.DESCRIPTOR,])



_GETTRAINEDMODELREQUEST_MODELTYPE = _descriptor.EnumDescriptor(
  name='ModelType',
  full_name='GetTrainedModelRequest.ModelType',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='BEST_MODEL', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='LAST_MODEL', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=915,
  serialized_end=958,
)
_sym_db.RegisterEnumDescriptor(_GETTRAINEDMODELREQUEST_MODELTYPE)


_NODEINFO = _descriptor.Descriptor(
  name='NodeInfo',
  full_name='NodeInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='NodeInfo.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='adress', full_name='NodeInfo.adress', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='cuda_available', full_name='NodeInfo.cuda_available', index=2,
      number=3, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='memory_size', full_name='NodeInfo.memory_size', index=3,
      number=4, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=36,
  serialized_end=121,
)


_SHARDINFO = _descriptor.Descriptor(
  name='ShardInfo',
  full_name='ShardInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='node_info', full_name='ShardInfo.node_info', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='shard_description', full_name='ShardInfo.shard_description', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='n_samples', full_name='ShardInfo.n_samples', index=2,
      number=3, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='sample_shape', full_name='ShardInfo.sample_shape', index=3,
      number=4, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='target_shape', full_name='ShardInfo.target_shape', index=4,
      number=5, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=124,
  serialized_end=255,
)


_SHARDACKNOWLEDGEMENT = _descriptor.Descriptor(
  name='ShardAcknowledgement',
  full_name='ShardAcknowledgement',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='accepted', full_name='ShardAcknowledgement.accepted', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=257,
  serialized_end=297,
)


_WAITEXPERIMENTREQUEST = _descriptor.Descriptor(
  name='WaitExperimentRequest',
  full_name='WaitExperimentRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='collaborator_name', full_name='WaitExperimentRequest.collaborator_name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=299,
  serialized_end=349,
)


_WAITEXPERIMENTRESPONSE = _descriptor.Descriptor(
  name='WaitExperimentResponse',
  full_name='WaitExperimentResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='experiment_name', full_name='WaitExperimentResponse.experiment_name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=351,
  serialized_end=400,
)


_GETEXPERIMENTDATAREQUEST = _descriptor.Descriptor(
  name='GetExperimentDataRequest',
  full_name='GetExperimentDataRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='experiment_name', full_name='GetExperimentDataRequest.experiment_name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='collaborator_name', full_name='GetExperimentDataRequest.collaborator_name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=402,
  serialized_end=480,
)


_EXPERIMENTDATA = _descriptor.Descriptor(
  name='ExperimentData',
  full_name='ExperimentData',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='size', full_name='ExperimentData.size', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='npbytes', full_name='ExperimentData.npbytes', index=1,
      number=2, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=482,
  serialized_end=529,
)


_EXPERIMENTINFO = _descriptor.Descriptor(
  name='ExperimentInfo',
  full_name='ExperimentInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='ExperimentInfo.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='collaborator_names', full_name='ExperimentInfo.collaborator_names', index=1,
      number=2, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='experiment_data', full_name='ExperimentInfo.experiment_data', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='model_proto', full_name='ExperimentInfo.model_proto', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=532,
  serialized_end=666,
)


_SETNEWEXPERIMENTRESPONSE = _descriptor.Descriptor(
  name='SetNewExperimentResponse',
  full_name='SetNewExperimentResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='accepted', full_name='SetNewExperimentResponse.accepted', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='tensorboard_address', full_name='SetNewExperimentResponse.tensorboard_address', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=668,
  serialized_end=741,
)


_GETREGISTERDSHARDSREQUEST = _descriptor.Descriptor(
  name='GetRegisterdShardsRequest',
  full_name='GetRegisterdShardsRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=743,
  serialized_end=770,
)


_GETREGISTERDSHARDSRESPONSE = _descriptor.Descriptor(
  name='GetRegisterdShardsResponse',
  full_name='GetRegisterdShardsResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='shard_info', full_name='GetRegisterdShardsResponse.shard_info', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=772,
  serialized_end=832,
)


_GETTRAINEDMODELREQUEST = _descriptor.Descriptor(
  name='GetTrainedModelRequest',
  full_name='GetTrainedModelRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='model_type', full_name='GetTrainedModelRequest.model_type', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _GETTRAINEDMODELREQUEST_MODELTYPE,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=834,
  serialized_end=958,
)


_TRAINEDMODELRESPONSE = _descriptor.Descriptor(
  name='TrainedModelResponse',
  full_name='TrainedModelResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='model_proto', full_name='TrainedModelResponse.model_proto', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=960,
  serialized_end=1016,
)


_GETSHARDSINFOREQUEST = _descriptor.Descriptor(
  name='GetShardsInfoRequest',
  full_name='GetShardsInfoRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1018,
  serialized_end=1040,
)


_STREAMMETRICSREQUEST = _descriptor.Descriptor(
  name='StreamMetricsRequest',
  full_name='StreamMetricsRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='experiment_name', full_name='StreamMetricsRequest.experiment_name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1042,
  serialized_end=1089,
)


_STREAMMETRICSRESPONSE = _descriptor.Descriptor(
  name='StreamMetricsResponse',
  full_name='StreamMetricsResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='metric_origin', full_name='StreamMetricsResponse.metric_origin', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='task_name', full_name='StreamMetricsResponse.task_name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='metric_name', full_name='StreamMetricsResponse.metric_name', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='metric_value', full_name='StreamMetricsResponse.metric_value', index=3,
      number=4, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='round', full_name='StreamMetricsResponse.round', index=4,
      number=5, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1091,
  serialized_end=1214,
)

_SHARDINFO.fields_by_name['node_info'].message_type = _NODEINFO
_EXPERIMENTINFO.fields_by_name['experiment_data'].message_type = _EXPERIMENTDATA
_EXPERIMENTINFO.fields_by_name['model_proto'].message_type = federation__pb2._MODELPROTO
_GETREGISTERDSHARDSRESPONSE.fields_by_name['shard_info'].message_type = _SHARDINFO
_GETTRAINEDMODELREQUEST.fields_by_name['model_type'].enum_type = _GETTRAINEDMODELREQUEST_MODELTYPE
_GETTRAINEDMODELREQUEST_MODELTYPE.containing_type = _GETTRAINEDMODELREQUEST
_TRAINEDMODELRESPONSE.fields_by_name['model_proto'].message_type = federation__pb2._MODELPROTO
DESCRIPTOR.message_types_by_name['NodeInfo'] = _NODEINFO
DESCRIPTOR.message_types_by_name['ShardInfo'] = _SHARDINFO
DESCRIPTOR.message_types_by_name['ShardAcknowledgement'] = _SHARDACKNOWLEDGEMENT
DESCRIPTOR.message_types_by_name['WaitExperimentRequest'] = _WAITEXPERIMENTREQUEST
DESCRIPTOR.message_types_by_name['WaitExperimentResponse'] = _WAITEXPERIMENTRESPONSE
DESCRIPTOR.message_types_by_name['GetExperimentDataRequest'] = _GETEXPERIMENTDATAREQUEST
DESCRIPTOR.message_types_by_name['ExperimentData'] = _EXPERIMENTDATA
DESCRIPTOR.message_types_by_name['ExperimentInfo'] = _EXPERIMENTINFO
DESCRIPTOR.message_types_by_name['SetNewExperimentResponse'] = _SETNEWEXPERIMENTRESPONSE
DESCRIPTOR.message_types_by_name['GetRegisterdShardsRequest'] = _GETREGISTERDSHARDSREQUEST
DESCRIPTOR.message_types_by_name['GetRegisterdShardsResponse'] = _GETREGISTERDSHARDSRESPONSE
DESCRIPTOR.message_types_by_name['GetTrainedModelRequest'] = _GETTRAINEDMODELREQUEST
DESCRIPTOR.message_types_by_name['TrainedModelResponse'] = _TRAINEDMODELRESPONSE
DESCRIPTOR.message_types_by_name['GetShardsInfoRequest'] = _GETSHARDSINFOREQUEST
DESCRIPTOR.message_types_by_name['StreamMetricsRequest'] = _STREAMMETRICSREQUEST
DESCRIPTOR.message_types_by_name['StreamMetricsResponse'] = _STREAMMETRICSRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

NodeInfo = _reflection.GeneratedProtocolMessageType('NodeInfo', (_message.Message,), {
  'DESCRIPTOR' : _NODEINFO,
  '__module__' : 'director_pb2'
  # @@protoc_insertion_point(class_scope:NodeInfo)
  })
_sym_db.RegisterMessage(NodeInfo)

ShardInfo = _reflection.GeneratedProtocolMessageType('ShardInfo', (_message.Message,), {
  'DESCRIPTOR' : _SHARDINFO,
  '__module__' : 'director_pb2'
  # @@protoc_insertion_point(class_scope:ShardInfo)
  })
_sym_db.RegisterMessage(ShardInfo)

ShardAcknowledgement = _reflection.GeneratedProtocolMessageType('ShardAcknowledgement', (_message.Message,), {
  'DESCRIPTOR' : _SHARDACKNOWLEDGEMENT,
  '__module__' : 'director_pb2'
  # @@protoc_insertion_point(class_scope:ShardAcknowledgement)
  })
_sym_db.RegisterMessage(ShardAcknowledgement)

WaitExperimentRequest = _reflection.GeneratedProtocolMessageType('WaitExperimentRequest', (_message.Message,), {
  'DESCRIPTOR' : _WAITEXPERIMENTREQUEST,
  '__module__' : 'director_pb2'
  # @@protoc_insertion_point(class_scope:WaitExperimentRequest)
  })
_sym_db.RegisterMessage(WaitExperimentRequest)

WaitExperimentResponse = _reflection.GeneratedProtocolMessageType('WaitExperimentResponse', (_message.Message,), {
  'DESCRIPTOR' : _WAITEXPERIMENTRESPONSE,
  '__module__' : 'director_pb2'
  # @@protoc_insertion_point(class_scope:WaitExperimentResponse)
  })
_sym_db.RegisterMessage(WaitExperimentResponse)

GetExperimentDataRequest = _reflection.GeneratedProtocolMessageType('GetExperimentDataRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETEXPERIMENTDATAREQUEST,
  '__module__' : 'director_pb2'
  # @@protoc_insertion_point(class_scope:GetExperimentDataRequest)
  })
_sym_db.RegisterMessage(GetExperimentDataRequest)

ExperimentData = _reflection.GeneratedProtocolMessageType('ExperimentData', (_message.Message,), {
  'DESCRIPTOR' : _EXPERIMENTDATA,
  '__module__' : 'director_pb2'
  # @@protoc_insertion_point(class_scope:ExperimentData)
  })
_sym_db.RegisterMessage(ExperimentData)

ExperimentInfo = _reflection.GeneratedProtocolMessageType('ExperimentInfo', (_message.Message,), {
  'DESCRIPTOR' : _EXPERIMENTINFO,
  '__module__' : 'director_pb2'
  # @@protoc_insertion_point(class_scope:ExperimentInfo)
  })
_sym_db.RegisterMessage(ExperimentInfo)

SetNewExperimentResponse = _reflection.GeneratedProtocolMessageType('SetNewExperimentResponse', (_message.Message,), {
  'DESCRIPTOR' : _SETNEWEXPERIMENTRESPONSE,
  '__module__' : 'director_pb2'
  # @@protoc_insertion_point(class_scope:SetNewExperimentResponse)
  })
_sym_db.RegisterMessage(SetNewExperimentResponse)

GetRegisterdShardsRequest = _reflection.GeneratedProtocolMessageType('GetRegisterdShardsRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETREGISTERDSHARDSREQUEST,
  '__module__' : 'director_pb2'
  # @@protoc_insertion_point(class_scope:GetRegisterdShardsRequest)
  })
_sym_db.RegisterMessage(GetRegisterdShardsRequest)

GetRegisterdShardsResponse = _reflection.GeneratedProtocolMessageType('GetRegisterdShardsResponse', (_message.Message,), {
  'DESCRIPTOR' : _GETREGISTERDSHARDSRESPONSE,
  '__module__' : 'director_pb2'
  # @@protoc_insertion_point(class_scope:GetRegisterdShardsResponse)
  })
_sym_db.RegisterMessage(GetRegisterdShardsResponse)

GetTrainedModelRequest = _reflection.GeneratedProtocolMessageType('GetTrainedModelRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETTRAINEDMODELREQUEST,
  '__module__' : 'director_pb2'
  # @@protoc_insertion_point(class_scope:GetTrainedModelRequest)
  })
_sym_db.RegisterMessage(GetTrainedModelRequest)

TrainedModelResponse = _reflection.GeneratedProtocolMessageType('TrainedModelResponse', (_message.Message,), {
  'DESCRIPTOR' : _TRAINEDMODELRESPONSE,
  '__module__' : 'director_pb2'
  # @@protoc_insertion_point(class_scope:TrainedModelResponse)
  })
_sym_db.RegisterMessage(TrainedModelResponse)

GetShardsInfoRequest = _reflection.GeneratedProtocolMessageType('GetShardsInfoRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETSHARDSINFOREQUEST,
  '__module__' : 'director_pb2'
  # @@protoc_insertion_point(class_scope:GetShardsInfoRequest)
  })
_sym_db.RegisterMessage(GetShardsInfoRequest)

StreamMetricsRequest = _reflection.GeneratedProtocolMessageType('StreamMetricsRequest', (_message.Message,), {
  'DESCRIPTOR' : _STREAMMETRICSREQUEST,
  '__module__' : 'director_pb2'
  # @@protoc_insertion_point(class_scope:StreamMetricsRequest)
  })
_sym_db.RegisterMessage(StreamMetricsRequest)

StreamMetricsResponse = _reflection.GeneratedProtocolMessageType('StreamMetricsResponse', (_message.Message,), {
  'DESCRIPTOR' : _STREAMMETRICSRESPONSE,
  '__module__' : 'director_pb2'
  # @@protoc_insertion_point(class_scope:StreamMetricsResponse)
  })
_sym_db.RegisterMessage(StreamMetricsResponse)



_FEDERATIONDIRECTOR = _descriptor.ServiceDescriptor(
  name='FederationDirector',
  full_name='FederationDirector',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=1217,
  serialized_end=1776,
  methods=[
  _descriptor.MethodDescriptor(
    name='AcknowledgeShard',
    full_name='FederationDirector.AcknowledgeShard',
    index=0,
    containing_service=None,
    input_type=_SHARDINFO,
    output_type=_SHARDACKNOWLEDGEMENT,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='WaitExperiment',
    full_name='FederationDirector.WaitExperiment',
    index=1,
    containing_service=None,
    input_type=_WAITEXPERIMENTREQUEST,
    output_type=_WAITEXPERIMENTRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='GetExperimentData',
    full_name='FederationDirector.GetExperimentData',
    index=2,
    containing_service=None,
    input_type=_GETEXPERIMENTDATAREQUEST,
    output_type=_EXPERIMENTDATA,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='SetNewExperiment',
    full_name='FederationDirector.SetNewExperiment',
    index=3,
    containing_service=None,
    input_type=_EXPERIMENTINFO,
    output_type=_SETNEWEXPERIMENTRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='GetRegisterdShards',
    full_name='FederationDirector.GetRegisterdShards',
    index=4,
    containing_service=None,
    input_type=_GETREGISTERDSHARDSREQUEST,
    output_type=_GETREGISTERDSHARDSRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='GetShardsInfo',
    full_name='FederationDirector.GetShardsInfo',
    index=5,
    containing_service=None,
    input_type=_GETSHARDSINFOREQUEST,
    output_type=_SHARDINFO,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='GetTrainedModel',
    full_name='FederationDirector.GetTrainedModel',
    index=6,
    containing_service=None,
    input_type=_GETTRAINEDMODELREQUEST,
    output_type=_TRAINEDMODELRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='StreamMetrics',
    full_name='FederationDirector.StreamMetrics',
    index=7,
    containing_service=None,
    input_type=_STREAMMETRICSREQUEST,
    output_type=_STREAMMETRICSRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_FEDERATIONDIRECTOR)

DESCRIPTOR.services_by_name['FederationDirector'] = _FEDERATIONDIRECTOR

# @@protoc_insertion_point(module_scope)
