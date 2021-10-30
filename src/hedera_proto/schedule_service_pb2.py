# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: schedule_service.proto
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
  name='schedule_service.proto',
  package='proto',
  syntax='proto3',
  serialized_options=b'\n&com.hederahashgraph.service.proto.java',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x16schedule_service.proto\x12\x05proto\x1a\x0bquery.proto\x1a\x0eresponse.proto\x1a\x1atransaction_response.proto\x1a\x11transaction.proto2\x87\x02\n\x0fScheduleService\x12@\n\x0e\x63reateSchedule\x12\x12.proto.Transaction\x1a\x1a.proto.TransactionResponse\x12>\n\x0csignSchedule\x12\x12.proto.Transaction\x1a\x1a.proto.TransactionResponse\x12@\n\x0e\x64\x65leteSchedule\x12\x12.proto.Transaction\x1a\x1a.proto.TransactionResponse\x12\x30\n\x0fgetScheduleInfo\x12\x0c.proto.Query\x1a\x0f.proto.ResponseB(\n&com.hederahashgraph.service.proto.javab\x06proto3'
  ,
  dependencies=[query__pb2.DESCRIPTOR,response__pb2.DESCRIPTOR,transaction__response__pb2.DESCRIPTOR,transaction__pb2.DESCRIPTOR,])



_sym_db.RegisterFileDescriptor(DESCRIPTOR)


DESCRIPTOR._options = None

_SCHEDULESERVICE = _descriptor.ServiceDescriptor(
  name='ScheduleService',
  full_name='proto.ScheduleService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=110,
  serialized_end=373,
  methods=[
  _descriptor.MethodDescriptor(
    name='createSchedule',
    full_name='proto.ScheduleService.createSchedule',
    index=0,
    containing_service=None,
    input_type=transaction__pb2._TRANSACTION,
    output_type=transaction__response__pb2._TRANSACTIONRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='signSchedule',
    full_name='proto.ScheduleService.signSchedule',
    index=1,
    containing_service=None,
    input_type=transaction__pb2._TRANSACTION,
    output_type=transaction__response__pb2._TRANSACTIONRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='deleteSchedule',
    full_name='proto.ScheduleService.deleteSchedule',
    index=2,
    containing_service=None,
    input_type=transaction__pb2._TRANSACTION,
    output_type=transaction__response__pb2._TRANSACTIONRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='getScheduleInfo',
    full_name='proto.ScheduleService.getScheduleInfo',
    index=3,
    containing_service=None,
    input_type=query__pb2._QUERY,
    output_type=response__pb2._RESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_SCHEDULESERVICE)

DESCRIPTOR.services_by_name['ScheduleService'] = _SCHEDULESERVICE

# @@protoc_insertion_point(module_scope)
