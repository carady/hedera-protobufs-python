# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: file_service.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import query_pb2 as query__pb2
import response_pb2 as response__pb2
import transaction_response_pb2 as transaction__response__pb2
import transaction_pb2 as transaction__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='file_service.proto',
  package='proto',
  syntax='proto3',
  serialized_options=b'\n&com.hederahashgraph.service.proto.java',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x12\x66ile_service.proto\x12\x05proto\x1a\x0bquery.proto\x1a\x0eresponse.proto\x1a\x1atransaction_response.proto\x1a\x11transaction.proto2\xe9\x03\n\x0b\x46ileService\x12<\n\ncreateFile\x12\x12.proto.Transaction\x1a\x1a.proto.TransactionResponse\x12<\n\nupdateFile\x12\x12.proto.Transaction\x1a\x1a.proto.TransactionResponse\x12<\n\ndeleteFile\x12\x12.proto.Transaction\x1a\x1a.proto.TransactionResponse\x12?\n\rappendContent\x12\x12.proto.Transaction\x1a\x1a.proto.TransactionResponse\x12/\n\x0egetFileContent\x12\x0c.proto.Query\x1a\x0f.proto.Response\x12,\n\x0bgetFileInfo\x12\x0c.proto.Query\x1a\x0f.proto.Response\x12>\n\x0csystemDelete\x12\x12.proto.Transaction\x1a\x1a.proto.TransactionResponse\x12@\n\x0esystemUndelete\x12\x12.proto.Transaction\x1a\x1a.proto.TransactionResponseB(\n&com.hederahashgraph.service.proto.javab\x06proto3'
  ,
  dependencies=[query__pb2.DESCRIPTOR,response__pb2.DESCRIPTOR,transaction__response__pb2.DESCRIPTOR,transaction__pb2.DESCRIPTOR,])



_sym_db.RegisterFileDescriptor(DESCRIPTOR)


DESCRIPTOR._options = None

_FILESERVICE = _descriptor.ServiceDescriptor(
  name='FileService',
  full_name='proto.FileService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=106,
  serialized_end=595,
  methods=[
  _descriptor.MethodDescriptor(
    name='createFile',
    full_name='proto.FileService.createFile',
    index=0,
    containing_service=None,
    input_type=transaction__pb2._TRANSACTION,
    output_type=transaction__response__pb2._TRANSACTIONRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='updateFile',
    full_name='proto.FileService.updateFile',
    index=1,
    containing_service=None,
    input_type=transaction__pb2._TRANSACTION,
    output_type=transaction__response__pb2._TRANSACTIONRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='deleteFile',
    full_name='proto.FileService.deleteFile',
    index=2,
    containing_service=None,
    input_type=transaction__pb2._TRANSACTION,
    output_type=transaction__response__pb2._TRANSACTIONRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='appendContent',
    full_name='proto.FileService.appendContent',
    index=3,
    containing_service=None,
    input_type=transaction__pb2._TRANSACTION,
    output_type=transaction__response__pb2._TRANSACTIONRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='getFileContent',
    full_name='proto.FileService.getFileContent',
    index=4,
    containing_service=None,
    input_type=query__pb2._QUERY,
    output_type=response__pb2._RESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='getFileInfo',
    full_name='proto.FileService.getFileInfo',
    index=5,
    containing_service=None,
    input_type=query__pb2._QUERY,
    output_type=response__pb2._RESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='systemDelete',
    full_name='proto.FileService.systemDelete',
    index=6,
    containing_service=None,
    input_type=transaction__pb2._TRANSACTION,
    output_type=transaction__response__pb2._TRANSACTIONRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='systemUndelete',
    full_name='proto.FileService.systemUndelete',
    index=7,
    containing_service=None,
    input_type=transaction__pb2._TRANSACTION,
    output_type=transaction__response__pb2._TRANSACTIONRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_FILESERVICE)

DESCRIPTOR.services_by_name['FileService'] = _FILESERVICE

# @@protoc_insertion_point(module_scope)