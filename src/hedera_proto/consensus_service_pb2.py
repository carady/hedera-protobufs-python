# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: consensus_service.proto
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


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x17\x63onsensus_service.proto\x12\x05proto\x1a\x0bquery.proto\x1a\x0eresponse.proto\x1a\x1atransaction_response.proto\x1a\x11transaction.proto2\xbf\x02\n\x10\x43onsensusService\x12=\n\x0b\x63reateTopic\x12\x12.proto.Transaction\x1a\x1a.proto.TransactionResponse\x12=\n\x0bupdateTopic\x12\x12.proto.Transaction\x1a\x1a.proto.TransactionResponse\x12=\n\x0b\x64\x65leteTopic\x12\x12.proto.Transaction\x1a\x1a.proto.TransactionResponse\x12-\n\x0cgetTopicInfo\x12\x0c.proto.Query\x1a\x0f.proto.Response\x12?\n\rsubmitMessage\x12\x12.proto.Transaction\x1a\x1a.proto.TransactionResponseB(\n&com.hederahashgraph.service.proto.javab\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'consensus_service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n&com.hederahashgraph.service.proto.java'
  _globals['_CONSENSUSSERVICE']._serialized_start=111
  _globals['_CONSENSUSSERVICE']._serialized_end=430
# @@protoc_insertion_point(module_scope)
