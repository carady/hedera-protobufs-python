# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: token_unpause.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import basic_types_pb2 as basic__types__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='token_unpause.proto',
  package='proto',
  syntax='proto3',
  serialized_options=b'\n\"com.hederahashgraph.api.proto.javaP\001',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x13token_unpause.proto\x12\x05proto\x1a\x11\x62\x61sic_types.proto\"<\n\x1bTokenUnpauseTransactionBody\x12\x1d\n\x05token\x18\x01 \x01(\x0b\x32\x0e.proto.TokenIDB&\n\"com.hederahashgraph.api.proto.javaP\x01\x62\x06proto3'
  ,
  dependencies=[basic__types__pb2.DESCRIPTOR,])




_TOKENUNPAUSETRANSACTIONBODY = _descriptor.Descriptor(
  name='TokenUnpauseTransactionBody',
  full_name='proto.TokenUnpauseTransactionBody',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='token', full_name='proto.TokenUnpauseTransactionBody.token', index=0,
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
  serialized_start=49,
  serialized_end=109,
)

_TOKENUNPAUSETRANSACTIONBODY.fields_by_name['token'].message_type = basic__types__pb2._TOKENID
DESCRIPTOR.message_types_by_name['TokenUnpauseTransactionBody'] = _TOKENUNPAUSETRANSACTIONBODY
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

TokenUnpauseTransactionBody = _reflection.GeneratedProtocolMessageType('TokenUnpauseTransactionBody', (_message.Message,), {
  'DESCRIPTOR' : _TOKENUNPAUSETRANSACTIONBODY,
  '__module__' : 'token_unpause_pb2'
  # @@protoc_insertion_point(class_scope:proto.TokenUnpauseTransactionBody)
  })
_sym_db.RegisterMessage(TokenUnpauseTransactionBody)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
