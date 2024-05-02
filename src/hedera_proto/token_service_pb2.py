# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: token_service.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import query_pb2 as query__pb2
import response_pb2 as response__pb2
import transaction_response_pb2 as transaction__response__pb2
import transaction_pb2 as transaction__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x13token_service.proto\x12\x05proto\x1a\x0bquery.proto\x1a\x0eresponse.proto\x1a\x1atransaction_response.proto\x1a\x11transaction.proto2\x8e\n\n\x0cTokenService\x12=\n\x0b\x63reateToken\x12\x12.proto.Transaction\x1a\x1a.proto.TransactionResponse\x12=\n\x0bupdateToken\x12\x12.proto.Transaction\x1a\x1a.proto.TransactionResponse\x12;\n\tmintToken\x12\x12.proto.Transaction\x1a\x1a.proto.TransactionResponse\x12;\n\tburnToken\x12\x12.proto.Transaction\x1a\x1a.proto.TransactionResponse\x12=\n\x0b\x64\x65leteToken\x12\x12.proto.Transaction\x1a\x1a.proto.TransactionResponse\x12\x42\n\x10wipeTokenAccount\x12\x12.proto.Transaction\x1a\x1a.proto.TransactionResponse\x12\x44\n\x12\x66reezeTokenAccount\x12\x12.proto.Transaction\x1a\x1a.proto.TransactionResponse\x12\x46\n\x14unfreezeTokenAccount\x12\x12.proto.Transaction\x1a\x1a.proto.TransactionResponse\x12H\n\x16grantKycToTokenAccount\x12\x12.proto.Transaction\x1a\x1a.proto.TransactionResponse\x12K\n\x19revokeKycFromTokenAccount\x12\x12.proto.Transaction\x1a\x1a.proto.TransactionResponse\x12\x41\n\x0f\x61ssociateTokens\x12\x12.proto.Transaction\x1a\x1a.proto.TransactionResponse\x12\x42\n\x10\x64issociateTokens\x12\x12.proto.Transaction\x1a\x1a.proto.TransactionResponse\x12H\n\x16updateTokenFeeSchedule\x12\x12.proto.Transaction\x1a\x1a.proto.TransactionResponse\x12-\n\x0cgetTokenInfo\x12\x0c.proto.Query\x1a\x0f.proto.Response\x12\x38\n\x12getAccountNftInfos\x12\x0c.proto.Query\x1a\x0f.proto.Response\"\x03\x88\x02\x01\x12\x30\n\x0fgetTokenNftInfo\x12\x0c.proto.Query\x1a\x0f.proto.Response\x12\x36\n\x10getTokenNftInfos\x12\x0c.proto.Query\x1a\x0f.proto.Response\"\x03\x88\x02\x01\x12<\n\npauseToken\x12\x12.proto.Transaction\x1a\x1a.proto.TransactionResponse\x12>\n\x0cunpauseToken\x12\x12.proto.Transaction\x1a\x1a.proto.TransactionResponse\x12<\n\nupdateNfts\x12\x12.proto.Transaction\x1a\x1a.proto.TransactionResponseB(\n&com.hederahashgraph.service.proto.javab\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'token_service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n&com.hederahashgraph.service.proto.java'
  _globals['_TOKENSERVICE'].methods_by_name['getAccountNftInfos']._loaded_options = None
  _globals['_TOKENSERVICE'].methods_by_name['getAccountNftInfos']._serialized_options = b'\210\002\001'
  _globals['_TOKENSERVICE'].methods_by_name['getTokenNftInfos']._loaded_options = None
  _globals['_TOKENSERVICE'].methods_by_name['getTokenNftInfos']._serialized_options = b'\210\002\001'
  _globals['_TOKENSERVICE']._serialized_start=107
  _globals['_TOKENSERVICE']._serialized_end=1401
# @@protoc_insertion_point(module_scope)
