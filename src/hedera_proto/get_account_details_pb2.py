# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: get_account_details.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import timestamp_pb2 as timestamp__pb2
import duration_pb2 as duration__pb2
import basic_types_pb2 as basic__types__pb2
import query_header_pb2 as query__header__pb2
import response_header_pb2 as response__header__pb2
import crypto_add_live_hash_pb2 as crypto__add__live__hash__pb2
from google.protobuf import wrappers_pb2 as google_dot_protobuf_dot_wrappers__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x19get_account_details.proto\x12\x05proto\x1a\x0ftimestamp.proto\x1a\x0e\x64uration.proto\x1a\x11\x62\x61sic_types.proto\x1a\x12query_header.proto\x1a\x15response_header.proto\x1a\x1a\x63rypto_add_live_hash.proto\x1a\x1egoogle/protobuf/wrappers.proto\"b\n\x16GetAccountDetailsQuery\x12\"\n\x06header\x18\x01 \x01(\x0b\x32\x12.proto.QueryHeader\x12$\n\naccount_id\x18\x02 \x01(\x0b\x32\x10.proto.AccountID\"\xbe\x06\n\x19GetAccountDetailsResponse\x12%\n\x06header\x18\x01 \x01(\x0b\x32\x15.proto.ResponseHeader\x12H\n\x0f\x61\x63\x63ount_details\x18\x02 \x01(\x0b\x32/.proto.GetAccountDetailsResponse.AccountDetails\x1a\xaf\x05\n\x0e\x41\x63\x63ountDetails\x12$\n\naccount_id\x18\x01 \x01(\x0b\x32\x10.proto.AccountID\x12\x1b\n\x13\x63ontract_account_id\x18\x02 \x01(\t\x12\x0f\n\x07\x64\x65leted\x18\x03 \x01(\x08\x12.\n\x10proxy_account_id\x18\x04 \x01(\x0b\x32\x10.proto.AccountIDB\x02\x18\x01\x12\x16\n\x0eproxy_received\x18\x05 \x01(\x03\x12\x17\n\x03key\x18\x06 \x01(\x0b\x32\n.proto.Key\x12\x0f\n\x07\x62\x61lance\x18\x07 \x01(\x04\x12\x1d\n\x15receiver_sig_required\x18\x08 \x01(\x08\x12)\n\x0f\x65xpiration_time\x18\t \x01(\x0b\x32\x10.proto.Timestamp\x12*\n\x11\x61uto_renew_period\x18\n \x01(\x0b\x32\x0f.proto.Duration\x12\x35\n\x13token_relationships\x18\x0b \x03(\x0b\x32\x18.proto.TokenRelationship\x12\x0c\n\x04memo\x18\x0c \x01(\t\x12\x12\n\nowned_nfts\x18\r \x01(\x03\x12(\n max_automatic_token_associations\x18\x0e \x01(\x05\x12\r\n\x05\x61lias\x18\x0f \x01(\x0c\x12\x11\n\tledger_id\x18\x10 \x01(\x0c\x12@\n\x19granted_crypto_allowances\x18\x11 \x03(\x0b\x32\x1d.proto.GrantedCryptoAllowance\x12:\n\x16granted_nft_allowances\x18\x12 \x03(\x0b\x32\x1a.proto.GrantedNftAllowance\x12>\n\x18granted_token_allowances\x18\x13 \x03(\x0b\x32\x1c.proto.GrantedTokenAllowance\"K\n\x16GrantedCryptoAllowance\x12!\n\x07spender\x18\x01 \x01(\x0b\x32\x10.proto.AccountID\x12\x0e\n\x06\x61mount\x18\x02 \x01(\x03\"Z\n\x13GrantedNftAllowance\x12 \n\x08token_id\x18\x01 \x01(\x0b\x32\x0e.proto.TokenID\x12!\n\x07spender\x18\x02 \x01(\x0b\x32\x10.proto.AccountID\"l\n\x15GrantedTokenAllowance\x12 \n\x08token_id\x18\x01 \x01(\x0b\x32\x0e.proto.TokenID\x12!\n\x07spender\x18\x02 \x01(\x0b\x32\x10.proto.AccountID\x12\x0e\n\x06\x61mount\x18\x03 \x01(\x03\x42&\n\"com.hederahashgraph.api.proto.javaP\x01\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'get_account_details_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\"com.hederahashgraph.api.proto.javaP\001'
  _globals['_GETACCOUNTDETAILSRESPONSE_ACCOUNTDETAILS'].fields_by_name['proxy_account_id']._loaded_options = None
  _globals['_GETACCOUNTDETAILSRESPONSE_ACCOUNTDETAILS'].fields_by_name['proxy_account_id']._serialized_options = b'\030\001'
  _globals['_GETACCOUNTDETAILSQUERY']._serialized_start=191
  _globals['_GETACCOUNTDETAILSQUERY']._serialized_end=289
  _globals['_GETACCOUNTDETAILSRESPONSE']._serialized_start=292
  _globals['_GETACCOUNTDETAILSRESPONSE']._serialized_end=1122
  _globals['_GETACCOUNTDETAILSRESPONSE_ACCOUNTDETAILS']._serialized_start=435
  _globals['_GETACCOUNTDETAILSRESPONSE_ACCOUNTDETAILS']._serialized_end=1122
  _globals['_GRANTEDCRYPTOALLOWANCE']._serialized_start=1124
  _globals['_GRANTEDCRYPTOALLOWANCE']._serialized_end=1199
  _globals['_GRANTEDNFTALLOWANCE']._serialized_start=1201
  _globals['_GRANTEDNFTALLOWANCE']._serialized_end=1291
  _globals['_GRANTEDTOKENALLOWANCE']._serialized_start=1293
  _globals['_GRANTEDTOKENALLOWANCE']._serialized_end=1401
# @@protoc_insertion_point(module_scope)