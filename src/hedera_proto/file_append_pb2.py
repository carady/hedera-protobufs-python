# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: file_append.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import basic_types_pb2 as basic__types__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='file_append.proto',
  package='proto',
  syntax='proto3',
  serialized_options=b'\n\"com.hederahashgraph.api.proto.javaP\001',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x11\x66ile_append.proto\x12\x05proto\x1a\x11\x62\x61sic_types.proto\"L\n\x19\x46ileAppendTransactionBody\x12\x1d\n\x06\x66ileID\x18\x02 \x01(\x0b\x32\r.proto.FileID\x12\x10\n\x08\x63ontents\x18\x04 \x01(\x0c\x42&\n\"com.hederahashgraph.api.proto.javaP\x01\x62\x06proto3'
  ,
  dependencies=[basic__types__pb2.DESCRIPTOR,])




_FILEAPPENDTRANSACTIONBODY = _descriptor.Descriptor(
  name='FileAppendTransactionBody',
  full_name='proto.FileAppendTransactionBody',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='fileID', full_name='proto.FileAppendTransactionBody.fileID', index=0,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='contents', full_name='proto.FileAppendTransactionBody.contents', index=1,
      number=4, type=12, cpp_type=9, label=1,
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
  serialized_start=47,
  serialized_end=123,
)

_FILEAPPENDTRANSACTIONBODY.fields_by_name['fileID'].message_type = basic__types__pb2._FILEID
DESCRIPTOR.message_types_by_name['FileAppendTransactionBody'] = _FILEAPPENDTRANSACTIONBODY
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

FileAppendTransactionBody = _reflection.GeneratedProtocolMessageType('FileAppendTransactionBody', (_message.Message,), {
  'DESCRIPTOR' : _FILEAPPENDTRANSACTIONBODY,
  '__module__' : 'file_append_pb2'
  # @@protoc_insertion_point(class_scope:proto.FileAppendTransactionBody)
  })
_sym_db.RegisterMessage(FileAppendTransactionBody)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)