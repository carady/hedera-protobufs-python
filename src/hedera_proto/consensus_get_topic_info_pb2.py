# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: consensus_get_topic_info.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import basic_types_pb2 as basic__types__pb2
import query_header_pb2 as query__header__pb2
import response_header_pb2 as response__header__pb2
import consensus_topic_info_pb2 as consensus__topic__info__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='consensus_get_topic_info.proto',
  package='proto',
  syntax='proto3',
  serialized_options=b'\n\"com.hederahashgraph.api.proto.javaP\001',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x1e\x63onsensus_get_topic_info.proto\x12\x05proto\x1a\x11\x62\x61sic_types.proto\x1a\x12query_header.proto\x1a\x15response_header.proto\x1a\x1a\x63onsensus_topic_info.proto\"a\n\x1a\x43onsensusGetTopicInfoQuery\x12\"\n\x06header\x18\x01 \x01(\x0b\x32\x12.proto.QueryHeader\x12\x1f\n\x07topicID\x18\x02 \x01(\x0b\x32\x0e.proto.TopicID\"\x95\x01\n\x1d\x43onsensusGetTopicInfoResponse\x12%\n\x06header\x18\x01 \x01(\x0b\x32\x15.proto.ResponseHeader\x12\x1f\n\x07topicID\x18\x02 \x01(\x0b\x32\x0e.proto.TopicID\x12,\n\ttopicInfo\x18\x05 \x01(\x0b\x32\x19.proto.ConsensusTopicInfoB&\n\"com.hederahashgraph.api.proto.javaP\x01\x62\x06proto3'
  ,
  dependencies=[basic__types__pb2.DESCRIPTOR,query__header__pb2.DESCRIPTOR,response__header__pb2.DESCRIPTOR,consensus__topic__info__pb2.DESCRIPTOR,])




_CONSENSUSGETTOPICINFOQUERY = _descriptor.Descriptor(
  name='ConsensusGetTopicInfoQuery',
  full_name='proto.ConsensusGetTopicInfoQuery',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='header', full_name='proto.ConsensusGetTopicInfoQuery.header', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='topicID', full_name='proto.ConsensusGetTopicInfoQuery.topicID', index=1,
      number=2, type=11, cpp_type=10, label=1,
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
  serialized_start=131,
  serialized_end=228,
)


_CONSENSUSGETTOPICINFORESPONSE = _descriptor.Descriptor(
  name='ConsensusGetTopicInfoResponse',
  full_name='proto.ConsensusGetTopicInfoResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='header', full_name='proto.ConsensusGetTopicInfoResponse.header', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='topicID', full_name='proto.ConsensusGetTopicInfoResponse.topicID', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='topicInfo', full_name='proto.ConsensusGetTopicInfoResponse.topicInfo', index=2,
      number=5, type=11, cpp_type=10, label=1,
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
  serialized_start=231,
  serialized_end=380,
)

_CONSENSUSGETTOPICINFOQUERY.fields_by_name['header'].message_type = query__header__pb2._QUERYHEADER
_CONSENSUSGETTOPICINFOQUERY.fields_by_name['topicID'].message_type = basic__types__pb2._TOPICID
_CONSENSUSGETTOPICINFORESPONSE.fields_by_name['header'].message_type = response__header__pb2._RESPONSEHEADER
_CONSENSUSGETTOPICINFORESPONSE.fields_by_name['topicID'].message_type = basic__types__pb2._TOPICID
_CONSENSUSGETTOPICINFORESPONSE.fields_by_name['topicInfo'].message_type = consensus__topic__info__pb2._CONSENSUSTOPICINFO
DESCRIPTOR.message_types_by_name['ConsensusGetTopicInfoQuery'] = _CONSENSUSGETTOPICINFOQUERY
DESCRIPTOR.message_types_by_name['ConsensusGetTopicInfoResponse'] = _CONSENSUSGETTOPICINFORESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ConsensusGetTopicInfoQuery = _reflection.GeneratedProtocolMessageType('ConsensusGetTopicInfoQuery', (_message.Message,), {
  'DESCRIPTOR' : _CONSENSUSGETTOPICINFOQUERY,
  '__module__' : 'consensus_get_topic_info_pb2'
  # @@protoc_insertion_point(class_scope:proto.ConsensusGetTopicInfoQuery)
  })
_sym_db.RegisterMessage(ConsensusGetTopicInfoQuery)

ConsensusGetTopicInfoResponse = _reflection.GeneratedProtocolMessageType('ConsensusGetTopicInfoResponse', (_message.Message,), {
  'DESCRIPTOR' : _CONSENSUSGETTOPICINFORESPONSE,
  '__module__' : 'consensus_get_topic_info_pb2'
  # @@protoc_insertion_point(class_scope:proto.ConsensusGetTopicInfoResponse)
  })
_sym_db.RegisterMessage(ConsensusGetTopicInfoResponse)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
