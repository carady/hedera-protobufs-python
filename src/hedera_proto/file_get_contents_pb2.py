# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: file_get_contents.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import basic_types_pb2 as basic__types__pb2
import query_header_pb2 as query__header__pb2
import response_header_pb2 as response__header__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x17\x66ile_get_contents.proto\x12\x05proto\x1a\x11\x62\x61sic_types.proto\x1a\x12query_header.proto\x1a\x15response_header.proto\"Y\n\x14\x46ileGetContentsQuery\x12\"\n\x06header\x18\x01 \x01(\x0b\x32\x12.proto.QueryHeader\x12\x1d\n\x06\x66ileID\x18\x02 \x01(\x0b\x32\r.proto.FileID\"\xc4\x01\n\x17\x46ileGetContentsResponse\x12%\n\x06header\x18\x01 \x01(\x0b\x32\x15.proto.ResponseHeader\x12\x41\n\x0c\x66ileContents\x18\x02 \x01(\x0b\x32+.proto.FileGetContentsResponse.FileContents\x1a?\n\x0c\x46ileContents\x12\x1d\n\x06\x66ileID\x18\x01 \x01(\x0b\x32\r.proto.FileID\x12\x10\n\x08\x63ontents\x18\x02 \x01(\x0c\x42&\n\"com.hederahashgraph.api.proto.javaP\x01\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'file_get_contents_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\"com.hederahashgraph.api.proto.javaP\001'
  _globals['_FILEGETCONTENTSQUERY']._serialized_start=96
  _globals['_FILEGETCONTENTSQUERY']._serialized_end=185
  _globals['_FILEGETCONTENTSRESPONSE']._serialized_start=188
  _globals['_FILEGETCONTENTSRESPONSE']._serialized_end=384
  _globals['_FILEGETCONTENTSRESPONSE_FILECONTENTS']._serialized_start=321
  _globals['_FILEGETCONTENTSRESPONSE_FILECONTENTS']._serialized_end=384
# @@protoc_insertion_point(module_scope)
