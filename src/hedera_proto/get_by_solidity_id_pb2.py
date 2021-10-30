# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: get_by_solidity_id.proto
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
  name='get_by_solidity_id.proto',
  package='proto',
  syntax='proto3',
  serialized_options=b'\n\"com.hederahashgraph.api.proto.javaP\001',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x18get_by_solidity_id.proto\x12\x05proto\x1a\x11\x62\x61sic_types.proto\x1a\x12query_header.proto\x1a\x15response_header.proto\"N\n\x14GetBySolidityIDQuery\x12\"\n\x06header\x18\x01 \x01(\x0b\x32\x12.proto.QueryHeader\x12\x12\n\nsolidityID\x18\x02 \x01(\t\"\xab\x01\n\x17GetBySolidityIDResponse\x12%\n\x06header\x18\x01 \x01(\x0b\x32\x15.proto.ResponseHeader\x12#\n\taccountID\x18\x02 \x01(\x0b\x32\x10.proto.AccountID\x12\x1d\n\x06\x66ileID\x18\x03 \x01(\x0b\x32\r.proto.FileID\x12%\n\ncontractID\x18\x04 \x01(\x0b\x32\x11.proto.ContractIDB&\n\"com.hederahashgraph.api.proto.javaP\x01\x62\x06proto3'
  ,
  dependencies=[basic__types__pb2.DESCRIPTOR,query__header__pb2.DESCRIPTOR,response__header__pb2.DESCRIPTOR,])




_GETBYSOLIDITYIDQUERY = _descriptor.Descriptor(
  name='GetBySolidityIDQuery',
  full_name='proto.GetBySolidityIDQuery',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='header', full_name='proto.GetBySolidityIDQuery.header', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='solidityID', full_name='proto.GetBySolidityIDQuery.solidityID', index=1,
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
  serialized_start=97,
  serialized_end=175,
)


_GETBYSOLIDITYIDRESPONSE = _descriptor.Descriptor(
  name='GetBySolidityIDResponse',
  full_name='proto.GetBySolidityIDResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='header', full_name='proto.GetBySolidityIDResponse.header', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='accountID', full_name='proto.GetBySolidityIDResponse.accountID', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='fileID', full_name='proto.GetBySolidityIDResponse.fileID', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='contractID', full_name='proto.GetBySolidityIDResponse.contractID', index=3,
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
  serialized_start=178,
  serialized_end=349,
)

_GETBYSOLIDITYIDQUERY.fields_by_name['header'].message_type = query__header__pb2._QUERYHEADER
_GETBYSOLIDITYIDRESPONSE.fields_by_name['header'].message_type = response__header__pb2._RESPONSEHEADER
_GETBYSOLIDITYIDRESPONSE.fields_by_name['accountID'].message_type = basic__types__pb2._ACCOUNTID
_GETBYSOLIDITYIDRESPONSE.fields_by_name['fileID'].message_type = basic__types__pb2._FILEID
_GETBYSOLIDITYIDRESPONSE.fields_by_name['contractID'].message_type = basic__types__pb2._CONTRACTID
DESCRIPTOR.message_types_by_name['GetBySolidityIDQuery'] = _GETBYSOLIDITYIDQUERY
DESCRIPTOR.message_types_by_name['GetBySolidityIDResponse'] = _GETBYSOLIDITYIDRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

GetBySolidityIDQuery = _reflection.GeneratedProtocolMessageType('GetBySolidityIDQuery', (_message.Message,), {
  'DESCRIPTOR' : _GETBYSOLIDITYIDQUERY,
  '__module__' : 'get_by_solidity_id_pb2'
  # @@protoc_insertion_point(class_scope:proto.GetBySolidityIDQuery)
  })
_sym_db.RegisterMessage(GetBySolidityIDQuery)

GetBySolidityIDResponse = _reflection.GeneratedProtocolMessageType('GetBySolidityIDResponse', (_message.Message,), {
  'DESCRIPTOR' : _GETBYSOLIDITYIDRESPONSE,
  '__module__' : 'get_by_solidity_id_pb2'
  # @@protoc_insertion_point(class_scope:proto.GetBySolidityIDResponse)
  })
_sym_db.RegisterMessage(GetBySolidityIDResponse)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
