# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: contract_create.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import basic_types_pb2 as basic__types__pb2
import duration_pb2 as duration__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x15\x63ontract_create.proto\x12\x05proto\x1a\x11\x62\x61sic_types.proto\x1a\x0e\x64uration.proto\"\xdf\x04\n\x1d\x43ontractCreateTransactionBody\x12\x1f\n\x06\x66ileID\x18\x01 \x01(\x0b\x32\r.proto.FileIDH\x00\x12\x12\n\x08initcode\x18\x10 \x01(\x0cH\x00\x12\x1c\n\x08\x61\x64minKey\x18\x03 \x01(\x0b\x32\n.proto.Key\x12\x0b\n\x03gas\x18\x04 \x01(\x03\x12\x16\n\x0einitialBalance\x18\x05 \x01(\x03\x12,\n\x0eproxyAccountID\x18\x06 \x01(\x0b\x32\x10.proto.AccountIDB\x02\x18\x01\x12(\n\x0f\x61utoRenewPeriod\x18\x08 \x01(\x0b\x32\x0f.proto.Duration\x12\x1d\n\x15\x63onstructorParameters\x18\t \x01(\x0c\x12\x1f\n\x07shardID\x18\n \x01(\x0b\x32\x0e.proto.ShardID\x12\x1f\n\x07realmID\x18\x0b \x01(\x0b\x32\x0e.proto.RealmID\x12$\n\x10newRealmAdminKey\x18\x0c \x01(\x0b\x32\n.proto.Key\x12\x0c\n\x04memo\x18\r \x01(\t\x12(\n max_automatic_token_associations\x18\x0e \x01(\x05\x12/\n\x15\x61uto_renew_account_id\x18\x0f \x01(\x0b\x32\x10.proto.AccountID\x12-\n\x11staked_account_id\x18\x11 \x01(\x0b\x32\x10.proto.AccountIDH\x01\x12\x18\n\x0estaked_node_id\x18\x12 \x01(\x03H\x01\x12\x16\n\x0e\x64\x65\x63line_reward\x18\x13 \x01(\x08\x42\x10\n\x0einitcodeSourceB\x0b\n\tstaked_idB&\n\"com.hederahashgraph.api.proto.javaP\x01\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'contract_create_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\"com.hederahashgraph.api.proto.javaP\001'
  _globals['_CONTRACTCREATETRANSACTIONBODY'].fields_by_name['proxyAccountID']._loaded_options = None
  _globals['_CONTRACTCREATETRANSACTIONBODY'].fields_by_name['proxyAccountID']._serialized_options = b'\030\001'
  _globals['_CONTRACTCREATETRANSACTIONBODY']._serialized_start=68
  _globals['_CONTRACTCREATETRANSACTIONBODY']._serialized_end=675
# @@protoc_insertion_point(module_scope)
