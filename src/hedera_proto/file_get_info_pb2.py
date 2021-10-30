# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: file_get_info.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import timestamp_pb2 as timestamp__pb2
import basic_types_pb2 as basic__types__pb2
import query_header_pb2 as query__header__pb2
import response_header_pb2 as response__header__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='file_get_info.proto',
  package='proto',
  syntax='proto3',
  serialized_options=b'\n\"com.hederahashgraph.api.proto.javaP\001',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x13\x66ile_get_info.proto\x12\x05proto\x1a\x0ftimestamp.proto\x1a\x11\x62\x61sic_types.proto\x1a\x12query_header.proto\x1a\x15response_header.proto\"U\n\x10\x46ileGetInfoQuery\x12\"\n\x06header\x18\x01 \x01(\x0b\x32\x12.proto.QueryHeader\x12\x1d\n\x06\x66ileID\x18\x02 \x01(\x0b\x32\r.proto.FileID\"\x94\x02\n\x13\x46ileGetInfoResponse\x12%\n\x06header\x18\x01 \x01(\x0b\x32\x15.proto.ResponseHeader\x12\x35\n\x08\x66ileInfo\x18\x02 \x01(\x0b\x32#.proto.FileGetInfoResponse.FileInfo\x1a\x9e\x01\n\x08\x46ileInfo\x12\x1d\n\x06\x66ileID\x18\x01 \x01(\x0b\x32\r.proto.FileID\x12\x0c\n\x04size\x18\x02 \x01(\x03\x12(\n\x0e\x65xpirationTime\x18\x03 \x01(\x0b\x32\x10.proto.Timestamp\x12\x0f\n\x07\x64\x65leted\x18\x04 \x01(\x08\x12\x1c\n\x04keys\x18\x05 \x01(\x0b\x32\x0e.proto.KeyList\x12\x0c\n\x04memo\x18\x06 \x01(\tB&\n\"com.hederahashgraph.api.proto.javaP\x01\x62\x06proto3'
  ,
  dependencies=[timestamp__pb2.DESCRIPTOR,basic__types__pb2.DESCRIPTOR,query__header__pb2.DESCRIPTOR,response__header__pb2.DESCRIPTOR,])




_FILEGETINFOQUERY = _descriptor.Descriptor(
  name='FileGetInfoQuery',
  full_name='proto.FileGetInfoQuery',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='header', full_name='proto.FileGetInfoQuery.header', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='fileID', full_name='proto.FileGetInfoQuery.fileID', index=1,
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
  serialized_start=109,
  serialized_end=194,
)


_FILEGETINFORESPONSE_FILEINFO = _descriptor.Descriptor(
  name='FileInfo',
  full_name='proto.FileGetInfoResponse.FileInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='fileID', full_name='proto.FileGetInfoResponse.FileInfo.fileID', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='size', full_name='proto.FileGetInfoResponse.FileInfo.size', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='expirationTime', full_name='proto.FileGetInfoResponse.FileInfo.expirationTime', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='deleted', full_name='proto.FileGetInfoResponse.FileInfo.deleted', index=3,
      number=4, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='keys', full_name='proto.FileGetInfoResponse.FileInfo.keys', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='memo', full_name='proto.FileGetInfoResponse.FileInfo.memo', index=5,
      number=6, type=9, cpp_type=9, label=1,
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
  serialized_start=315,
  serialized_end=473,
)

_FILEGETINFORESPONSE = _descriptor.Descriptor(
  name='FileGetInfoResponse',
  full_name='proto.FileGetInfoResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='header', full_name='proto.FileGetInfoResponse.header', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='fileInfo', full_name='proto.FileGetInfoResponse.fileInfo', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[_FILEGETINFORESPONSE_FILEINFO, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=197,
  serialized_end=473,
)

_FILEGETINFOQUERY.fields_by_name['header'].message_type = query__header__pb2._QUERYHEADER
_FILEGETINFOQUERY.fields_by_name['fileID'].message_type = basic__types__pb2._FILEID
_FILEGETINFORESPONSE_FILEINFO.fields_by_name['fileID'].message_type = basic__types__pb2._FILEID
_FILEGETINFORESPONSE_FILEINFO.fields_by_name['expirationTime'].message_type = timestamp__pb2._TIMESTAMP
_FILEGETINFORESPONSE_FILEINFO.fields_by_name['keys'].message_type = basic__types__pb2._KEYLIST
_FILEGETINFORESPONSE_FILEINFO.containing_type = _FILEGETINFORESPONSE
_FILEGETINFORESPONSE.fields_by_name['header'].message_type = response__header__pb2._RESPONSEHEADER
_FILEGETINFORESPONSE.fields_by_name['fileInfo'].message_type = _FILEGETINFORESPONSE_FILEINFO
DESCRIPTOR.message_types_by_name['FileGetInfoQuery'] = _FILEGETINFOQUERY
DESCRIPTOR.message_types_by_name['FileGetInfoResponse'] = _FILEGETINFORESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

FileGetInfoQuery = _reflection.GeneratedProtocolMessageType('FileGetInfoQuery', (_message.Message,), {
  'DESCRIPTOR' : _FILEGETINFOQUERY,
  '__module__' : 'file_get_info_pb2'
  # @@protoc_insertion_point(class_scope:proto.FileGetInfoQuery)
  })
_sym_db.RegisterMessage(FileGetInfoQuery)

FileGetInfoResponse = _reflection.GeneratedProtocolMessageType('FileGetInfoResponse', (_message.Message,), {

  'FileInfo' : _reflection.GeneratedProtocolMessageType('FileInfo', (_message.Message,), {
    'DESCRIPTOR' : _FILEGETINFORESPONSE_FILEINFO,
    '__module__' : 'file_get_info_pb2'
    # @@protoc_insertion_point(class_scope:proto.FileGetInfoResponse.FileInfo)
    })
  ,
  'DESCRIPTOR' : _FILEGETINFORESPONSE,
  '__module__' : 'file_get_info_pb2'
  # @@protoc_insertion_point(class_scope:proto.FileGetInfoResponse)
  })
_sym_db.RegisterMessage(FileGetInfoResponse)
_sym_db.RegisterMessage(FileGetInfoResponse.FileInfo)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
