# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: crypto_delete.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import basic_types_pb2 as basic__types__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='crypto_delete.proto',
  package='proto',
  syntax='proto3',
  serialized_options=b'\n\"com.hederahashgraph.api.proto.javaP\001',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x13\x63rypto_delete.proto\x12\x05proto\x1a\x11\x62\x61sic_types.proto\"u\n\x1b\x43ryptoDeleteTransactionBody\x12+\n\x11transferAccountID\x18\x01 \x01(\x0b\x32\x10.proto.AccountID\x12)\n\x0f\x64\x65leteAccountID\x18\x02 \x01(\x0b\x32\x10.proto.AccountIDB&\n\"com.hederahashgraph.api.proto.javaP\x01\x62\x06proto3'
  ,
  dependencies=[basic__types__pb2.DESCRIPTOR,])




_CRYPTODELETETRANSACTIONBODY = _descriptor.Descriptor(
  name='CryptoDeleteTransactionBody',
  full_name='proto.CryptoDeleteTransactionBody',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='transferAccountID', full_name='proto.CryptoDeleteTransactionBody.transferAccountID', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='deleteAccountID', full_name='proto.CryptoDeleteTransactionBody.deleteAccountID', index=1,
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
  serialized_start=49,
  serialized_end=166,
)

_CRYPTODELETETRANSACTIONBODY.fields_by_name['transferAccountID'].message_type = basic__types__pb2._ACCOUNTID
_CRYPTODELETETRANSACTIONBODY.fields_by_name['deleteAccountID'].message_type = basic__types__pb2._ACCOUNTID
DESCRIPTOR.message_types_by_name['CryptoDeleteTransactionBody'] = _CRYPTODELETETRANSACTIONBODY
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

CryptoDeleteTransactionBody = _reflection.GeneratedProtocolMessageType('CryptoDeleteTransactionBody', (_message.Message,), {
  'DESCRIPTOR' : _CRYPTODELETETRANSACTIONBODY,
  '__module__' : 'crypto_delete_pb2'
  # @@protoc_insertion_point(class_scope:proto.CryptoDeleteTransactionBody)
  })
_sym_db.RegisterMessage(CryptoDeleteTransactionBody)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)