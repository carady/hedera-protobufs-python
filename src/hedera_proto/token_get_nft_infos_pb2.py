# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: token_get_nft_infos.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import basic_types_pb2 as basic__types__pb2
import token_get_nft_info_pb2 as token__get__nft__info__pb2
import query_header_pb2 as query__header__pb2
import response_header_pb2 as response__header__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='token_get_nft_infos.proto',
  package='proto',
  syntax='proto3',
  serialized_options=b'\n\"com.hederahashgraph.api.proto.javaP\001',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x19token_get_nft_infos.proto\x12\x05proto\x1a\x11\x62\x61sic_types.proto\x1a\x18token_get_nft_info.proto\x1a\x12query_header.proto\x1a\x15response_header.proto\"x\n\x15TokenGetNftInfosQuery\x12\"\n\x06header\x18\x01 \x01(\x0b\x32\x12.proto.QueryHeader\x12\x1f\n\x07tokenID\x18\x02 \x01(\x0b\x32\x0e.proto.TokenID\x12\r\n\x05start\x18\x03 \x01(\x03\x12\x0b\n\x03\x65nd\x18\x04 \x01(\x03\"\x85\x01\n\x18TokenGetNftInfosResponse\x12%\n\x06header\x18\x01 \x01(\x0b\x32\x15.proto.ResponseHeader\x12\x1f\n\x07tokenID\x18\x02 \x01(\x0b\x32\x0e.proto.TokenID\x12!\n\x04nfts\x18\x03 \x03(\x0b\x32\x13.proto.TokenNftInfoB&\n\"com.hederahashgraph.api.proto.javaP\x01\x62\x06proto3'
  ,
  dependencies=[basic__types__pb2.DESCRIPTOR,token__get__nft__info__pb2.DESCRIPTOR,query__header__pb2.DESCRIPTOR,response__header__pb2.DESCRIPTOR,])




_TOKENGETNFTINFOSQUERY = _descriptor.Descriptor(
  name='TokenGetNftInfosQuery',
  full_name='proto.TokenGetNftInfosQuery',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='header', full_name='proto.TokenGetNftInfosQuery.header', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='tokenID', full_name='proto.TokenGetNftInfosQuery.tokenID', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='start', full_name='proto.TokenGetNftInfosQuery.start', index=2,
      number=3, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='end', full_name='proto.TokenGetNftInfosQuery.end', index=3,
      number=4, type=3, cpp_type=2, label=1,
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
  serialized_start=124,
  serialized_end=244,
)


_TOKENGETNFTINFOSRESPONSE = _descriptor.Descriptor(
  name='TokenGetNftInfosResponse',
  full_name='proto.TokenGetNftInfosResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='header', full_name='proto.TokenGetNftInfosResponse.header', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='tokenID', full_name='proto.TokenGetNftInfosResponse.tokenID', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='nfts', full_name='proto.TokenGetNftInfosResponse.nfts', index=2,
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
  serialized_start=247,
  serialized_end=380,
)

_TOKENGETNFTINFOSQUERY.fields_by_name['header'].message_type = query__header__pb2._QUERYHEADER
_TOKENGETNFTINFOSQUERY.fields_by_name['tokenID'].message_type = basic__types__pb2._TOKENID
_TOKENGETNFTINFOSRESPONSE.fields_by_name['header'].message_type = response__header__pb2._RESPONSEHEADER
_TOKENGETNFTINFOSRESPONSE.fields_by_name['tokenID'].message_type = basic__types__pb2._TOKENID
_TOKENGETNFTINFOSRESPONSE.fields_by_name['nfts'].message_type = token__get__nft__info__pb2._TOKENNFTINFO
DESCRIPTOR.message_types_by_name['TokenGetNftInfosQuery'] = _TOKENGETNFTINFOSQUERY
DESCRIPTOR.message_types_by_name['TokenGetNftInfosResponse'] = _TOKENGETNFTINFOSRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

TokenGetNftInfosQuery = _reflection.GeneratedProtocolMessageType('TokenGetNftInfosQuery', (_message.Message,), {
  'DESCRIPTOR' : _TOKENGETNFTINFOSQUERY,
  '__module__' : 'token_get_nft_infos_pb2'
  # @@protoc_insertion_point(class_scope:proto.TokenGetNftInfosQuery)
  })
_sym_db.RegisterMessage(TokenGetNftInfosQuery)

TokenGetNftInfosResponse = _reflection.GeneratedProtocolMessageType('TokenGetNftInfosResponse', (_message.Message,), {
  'DESCRIPTOR' : _TOKENGETNFTINFOSRESPONSE,
  '__module__' : 'token_get_nft_infos_pb2'
  # @@protoc_insertion_point(class_scope:proto.TokenGetNftInfosResponse)
  })
_sym_db.RegisterMessage(TokenGetNftInfosResponse)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
