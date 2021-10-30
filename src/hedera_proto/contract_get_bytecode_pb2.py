# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: contract_get_bytecode.proto
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


DESCRIPTOR = _descriptor.FileDescriptor(
  name='contract_get_bytecode.proto',
  package='proto',
  syntax='proto3',
  serialized_options=b'\n\"com.hederahashgraph.api.proto.javaP\001',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x1b\x63ontract_get_bytecode.proto\x12\x05proto\x1a\x11\x62\x61sic_types.proto\x1a\x12query_header.proto\x1a\x15response_header.proto\"e\n\x18\x43ontractGetBytecodeQuery\x12\"\n\x06header\x18\x01 \x01(\x0b\x32\x12.proto.QueryHeader\x12%\n\ncontractID\x18\x02 \x01(\x0b\x32\x11.proto.ContractID\"V\n\x1b\x43ontractGetBytecodeResponse\x12%\n\x06header\x18\x01 \x01(\x0b\x32\x15.proto.ResponseHeader\x12\x10\n\x08\x62ytecode\x18\x06 \x01(\x0c\x42&\n\"com.hederahashgraph.api.proto.javaP\x01\x62\x06proto3'
  ,
  dependencies=[basic__types__pb2.DESCRIPTOR,query__header__pb2.DESCRIPTOR,response__header__pb2.DESCRIPTOR,])




_CONTRACTGETBYTECODEQUERY = _descriptor.Descriptor(
  name='ContractGetBytecodeQuery',
  full_name='proto.ContractGetBytecodeQuery',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='header', full_name='proto.ContractGetBytecodeQuery.header', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='contractID', full_name='proto.ContractGetBytecodeQuery.contractID', index=1,
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
  serialized_start=100,
  serialized_end=201,
)


_CONTRACTGETBYTECODERESPONSE = _descriptor.Descriptor(
  name='ContractGetBytecodeResponse',
  full_name='proto.ContractGetBytecodeResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='header', full_name='proto.ContractGetBytecodeResponse.header', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='bytecode', full_name='proto.ContractGetBytecodeResponse.bytecode', index=1,
      number=6, type=12, cpp_type=9, label=1,
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
  serialized_start=203,
  serialized_end=289,
)

_CONTRACTGETBYTECODEQUERY.fields_by_name['header'].message_type = query__header__pb2._QUERYHEADER
_CONTRACTGETBYTECODEQUERY.fields_by_name['contractID'].message_type = basic__types__pb2._CONTRACTID
_CONTRACTGETBYTECODERESPONSE.fields_by_name['header'].message_type = response__header__pb2._RESPONSEHEADER
DESCRIPTOR.message_types_by_name['ContractGetBytecodeQuery'] = _CONTRACTGETBYTECODEQUERY
DESCRIPTOR.message_types_by_name['ContractGetBytecodeResponse'] = _CONTRACTGETBYTECODERESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ContractGetBytecodeQuery = _reflection.GeneratedProtocolMessageType('ContractGetBytecodeQuery', (_message.Message,), {
  'DESCRIPTOR' : _CONTRACTGETBYTECODEQUERY,
  '__module__' : 'contract_get_bytecode_pb2'
  # @@protoc_insertion_point(class_scope:proto.ContractGetBytecodeQuery)
  })
_sym_db.RegisterMessage(ContractGetBytecodeQuery)

ContractGetBytecodeResponse = _reflection.GeneratedProtocolMessageType('ContractGetBytecodeResponse', (_message.Message,), {
  'DESCRIPTOR' : _CONTRACTGETBYTECODERESPONSE,
  '__module__' : 'contract_get_bytecode_pb2'
  # @@protoc_insertion_point(class_scope:proto.ContractGetBytecodeResponse)
  })
_sym_db.RegisterMessage(ContractGetBytecodeResponse)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
