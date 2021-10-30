# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: token_fee_schedule_update.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import basic_types_pb2 as basic__types__pb2
import custom_fees_pb2 as custom__fees__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='token_fee_schedule_update.proto',
  package='proto',
  syntax='proto3',
  serialized_options=b'\n\"com.hederahashgraph.api.proto.javaP\001',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x1ftoken_fee_schedule_update.proto\x12\x05proto\x1a\x11\x62\x61sic_types.proto\x1a\x11\x63ustom_fees.proto\"p\n%TokenFeeScheduleUpdateTransactionBody\x12 \n\x08token_id\x18\x01 \x01(\x0b\x32\x0e.proto.TokenID\x12%\n\x0b\x63ustom_fees\x18\x02 \x03(\x0b\x32\x10.proto.CustomFeeB&\n\"com.hederahashgraph.api.proto.javaP\x01\x62\x06proto3'
  ,
  dependencies=[basic__types__pb2.DESCRIPTOR,custom__fees__pb2.DESCRIPTOR,])




_TOKENFEESCHEDULEUPDATETRANSACTIONBODY = _descriptor.Descriptor(
  name='TokenFeeScheduleUpdateTransactionBody',
  full_name='proto.TokenFeeScheduleUpdateTransactionBody',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='token_id', full_name='proto.TokenFeeScheduleUpdateTransactionBody.token_id', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='custom_fees', full_name='proto.TokenFeeScheduleUpdateTransactionBody.custom_fees', index=1,
      number=2, type=11, cpp_type=10, label=3,
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
  serialized_start=80,
  serialized_end=192,
)

_TOKENFEESCHEDULEUPDATETRANSACTIONBODY.fields_by_name['token_id'].message_type = basic__types__pb2._TOKENID
_TOKENFEESCHEDULEUPDATETRANSACTIONBODY.fields_by_name['custom_fees'].message_type = custom__fees__pb2._CUSTOMFEE
DESCRIPTOR.message_types_by_name['TokenFeeScheduleUpdateTransactionBody'] = _TOKENFEESCHEDULEUPDATETRANSACTIONBODY
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

TokenFeeScheduleUpdateTransactionBody = _reflection.GeneratedProtocolMessageType('TokenFeeScheduleUpdateTransactionBody', (_message.Message,), {
  'DESCRIPTOR' : _TOKENFEESCHEDULEUPDATETRANSACTIONBODY,
  '__module__' : 'token_fee_schedule_update_pb2'
  # @@protoc_insertion_point(class_scope:proto.TokenFeeScheduleUpdateTransactionBody)
  })
_sym_db.RegisterMessage(TokenFeeScheduleUpdateTransactionBody)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
