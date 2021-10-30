# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: throttle_definitions.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import basic_types_pb2 as basic__types__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='throttle_definitions.proto',
  package='proto',
  syntax='proto3',
  serialized_options=b'\n\"com.hederahashgraph.api.proto.javaP\001',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x1athrottle_definitions.proto\x12\x05proto\x1a\x11\x62\x61sic_types.proto\"W\n\rThrottleGroup\x12.\n\noperations\x18\x01 \x03(\x0e\x32\x1a.proto.HederaFunctionality\x12\x16\n\x0emilliOpsPerSec\x18\x02 \x01(\x04\"c\n\x0eThrottleBucket\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x15\n\rburstPeriodMs\x18\x02 \x01(\x04\x12,\n\x0ethrottleGroups\x18\x03 \x03(\x0b\x32\x14.proto.ThrottleGroup\"E\n\x13ThrottleDefinitions\x12.\n\x0fthrottleBuckets\x18\x01 \x03(\x0b\x32\x15.proto.ThrottleBucketB&\n\"com.hederahashgraph.api.proto.javaP\x01\x62\x06proto3'
  ,
  dependencies=[basic__types__pb2.DESCRIPTOR,])




_THROTTLEGROUP = _descriptor.Descriptor(
  name='ThrottleGroup',
  full_name='proto.ThrottleGroup',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='operations', full_name='proto.ThrottleGroup.operations', index=0,
      number=1, type=14, cpp_type=8, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='milliOpsPerSec', full_name='proto.ThrottleGroup.milliOpsPerSec', index=1,
      number=2, type=4, cpp_type=4, label=1,
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
  serialized_start=56,
  serialized_end=143,
)


_THROTTLEBUCKET = _descriptor.Descriptor(
  name='ThrottleBucket',
  full_name='proto.ThrottleBucket',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='proto.ThrottleBucket.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='burstPeriodMs', full_name='proto.ThrottleBucket.burstPeriodMs', index=1,
      number=2, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='throttleGroups', full_name='proto.ThrottleBucket.throttleGroups', index=2,
      number=3, type=11, cpp_type=10, label=3,
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
  serialized_start=145,
  serialized_end=244,
)


_THROTTLEDEFINITIONS = _descriptor.Descriptor(
  name='ThrottleDefinitions',
  full_name='proto.ThrottleDefinitions',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='throttleBuckets', full_name='proto.ThrottleDefinitions.throttleBuckets', index=0,
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
  serialized_start=246,
  serialized_end=315,
)

_THROTTLEGROUP.fields_by_name['operations'].enum_type = basic__types__pb2._HEDERAFUNCTIONALITY
_THROTTLEBUCKET.fields_by_name['throttleGroups'].message_type = _THROTTLEGROUP
_THROTTLEDEFINITIONS.fields_by_name['throttleBuckets'].message_type = _THROTTLEBUCKET
DESCRIPTOR.message_types_by_name['ThrottleGroup'] = _THROTTLEGROUP
DESCRIPTOR.message_types_by_name['ThrottleBucket'] = _THROTTLEBUCKET
DESCRIPTOR.message_types_by_name['ThrottleDefinitions'] = _THROTTLEDEFINITIONS
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ThrottleGroup = _reflection.GeneratedProtocolMessageType('ThrottleGroup', (_message.Message,), {
  'DESCRIPTOR' : _THROTTLEGROUP,
  '__module__' : 'throttle_definitions_pb2'
  # @@protoc_insertion_point(class_scope:proto.ThrottleGroup)
  })
_sym_db.RegisterMessage(ThrottleGroup)

ThrottleBucket = _reflection.GeneratedProtocolMessageType('ThrottleBucket', (_message.Message,), {
  'DESCRIPTOR' : _THROTTLEBUCKET,
  '__module__' : 'throttle_definitions_pb2'
  # @@protoc_insertion_point(class_scope:proto.ThrottleBucket)
  })
_sym_db.RegisterMessage(ThrottleBucket)

ThrottleDefinitions = _reflection.GeneratedProtocolMessageType('ThrottleDefinitions', (_message.Message,), {
  'DESCRIPTOR' : _THROTTLEDEFINITIONS,
  '__module__' : 'throttle_definitions_pb2'
  # @@protoc_insertion_point(class_scope:proto.ThrottleDefinitions)
  })
_sym_db.RegisterMessage(ThrottleDefinitions)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)