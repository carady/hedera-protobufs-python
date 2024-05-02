# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: crypto_get_account_records.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import basic_types_pb2 as basic__types__pb2
import transaction_record_pb2 as transaction__record__pb2
import query_header_pb2 as query__header__pb2
import response_header_pb2 as response__header__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n crypto_get_account_records.proto\x12\x05proto\x1a\x11\x62\x61sic_types.proto\x1a\x18transaction_record.proto\x1a\x12query_header.proto\x1a\x15response_header.proto\"g\n\x1c\x43ryptoGetAccountRecordsQuery\x12\"\n\x06header\x18\x01 \x01(\x0b\x32\x12.proto.QueryHeader\x12#\n\taccountID\x18\x02 \x01(\x0b\x32\x10.proto.AccountID\"\x98\x01\n\x1f\x43ryptoGetAccountRecordsResponse\x12%\n\x06header\x18\x01 \x01(\x0b\x32\x15.proto.ResponseHeader\x12#\n\taccountID\x18\x02 \x01(\x0b\x32\x10.proto.AccountID\x12)\n\x07records\x18\x03 \x03(\x0b\x32\x18.proto.TransactionRecordB&\n\"com.hederahashgraph.api.proto.javaP\x01\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'crypto_get_account_records_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\"com.hederahashgraph.api.proto.javaP\001'
  _globals['_CRYPTOGETACCOUNTRECORDSQUERY']._serialized_start=131
  _globals['_CRYPTOGETACCOUNTRECORDSQUERY']._serialized_end=234
  _globals['_CRYPTOGETACCOUNTRECORDSRESPONSE']._serialized_start=237
  _globals['_CRYPTOGETACCOUNTRECORDSRESPONSE']._serialized_end=389
# @@protoc_insertion_point(module_scope)
