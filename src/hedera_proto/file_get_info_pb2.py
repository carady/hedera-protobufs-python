# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: file_get_info.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import timestamp_pb2 as timestamp__pb2
import basic_types_pb2 as basic__types__pb2
import query_header_pb2 as query__header__pb2
import response_header_pb2 as response__header__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x13\x66ile_get_info.proto\x12\x05proto\x1a\x0ftimestamp.proto\x1a\x11\x62\x61sic_types.proto\x1a\x12query_header.proto\x1a\x15response_header.proto\"U\n\x10\x46ileGetInfoQuery\x12\"\n\x06header\x18\x01 \x01(\x0b\x32\x12.proto.QueryHeader\x12\x1d\n\x06\x66ileID\x18\x02 \x01(\x0b\x32\r.proto.FileID\"\xa7\x02\n\x13\x46ileGetInfoResponse\x12%\n\x06header\x18\x01 \x01(\x0b\x32\x15.proto.ResponseHeader\x12\x35\n\x08\x66ileInfo\x18\x02 \x01(\x0b\x32#.proto.FileGetInfoResponse.FileInfo\x1a\xb1\x01\n\x08\x46ileInfo\x12\x1d\n\x06\x66ileID\x18\x01 \x01(\x0b\x32\r.proto.FileID\x12\x0c\n\x04size\x18\x02 \x01(\x03\x12(\n\x0e\x65xpirationTime\x18\x03 \x01(\x0b\x32\x10.proto.Timestamp\x12\x0f\n\x07\x64\x65leted\x18\x04 \x01(\x08\x12\x1c\n\x04keys\x18\x05 \x01(\x0b\x32\x0e.proto.KeyList\x12\x0c\n\x04memo\x18\x06 \x01(\t\x12\x11\n\tledger_id\x18\x07 \x01(\x0c\x42&\n\"com.hederahashgraph.api.proto.javaP\x01\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'file_get_info_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\"com.hederahashgraph.api.proto.javaP\001'
  _globals['_FILEGETINFOQUERY']._serialized_start=109
  _globals['_FILEGETINFOQUERY']._serialized_end=194
  _globals['_FILEGETINFORESPONSE']._serialized_start=197
  _globals['_FILEGETINFORESPONSE']._serialized_end=492
  _globals['_FILEGETINFORESPONSE_FILEINFO']._serialized_start=315
  _globals['_FILEGETINFORESPONSE_FILEINFO']._serialized_end=492
# @@protoc_insertion_point(module_scope)
