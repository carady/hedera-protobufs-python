# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: query.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import get_by_key_pb2 as get__by__key__pb2
import get_by_solidity_id_pb2 as get__by__solidity__id__pb2
import contract_call_local_pb2 as contract__call__local__pb2
import contract_get_info_pb2 as contract__get__info__pb2
import contract_get_bytecode_pb2 as contract__get__bytecode__pb2
import contract_get_records_pb2 as contract__get__records__pb2
import crypto_get_account_balance_pb2 as crypto__get__account__balance__pb2
import crypto_get_account_records_pb2 as crypto__get__account__records__pb2
import crypto_get_info_pb2 as crypto__get__info__pb2
import crypto_get_live_hash_pb2 as crypto__get__live__hash__pb2
import crypto_get_stakers_pb2 as crypto__get__stakers__pb2
import file_get_contents_pb2 as file__get__contents__pb2
import file_get_info_pb2 as file__get__info__pb2
import transaction_get_receipt_pb2 as transaction__get__receipt__pb2
import transaction_get_record_pb2 as transaction__get__record__pb2
import transaction_get_fast_record_pb2 as transaction__get__fast__record__pb2
import consensus_get_topic_info_pb2 as consensus__get__topic__info__pb2
import network_get_version_info_pb2 as network__get__version__info__pb2
import network_get_execution_time_pb2 as network__get__execution__time__pb2
import token_get_info_pb2 as token__get__info__pb2
import schedule_get_info_pb2 as schedule__get__info__pb2
import token_get_account_nft_infos_pb2 as token__get__account__nft__infos__pb2
import token_get_nft_info_pb2 as token__get__nft__info__pb2
import token_get_nft_infos_pb2 as token__get__nft__infos__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='query.proto',
  package='proto',
  syntax='proto3',
  serialized_options=b'\n\"com.hederahashgraph.api.proto.javaP\001',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x0bquery.proto\x12\x05proto\x1a\x10get_by_key.proto\x1a\x18get_by_solidity_id.proto\x1a\x19\x63ontract_call_local.proto\x1a\x17\x63ontract_get_info.proto\x1a\x1b\x63ontract_get_bytecode.proto\x1a\x1a\x63ontract_get_records.proto\x1a crypto_get_account_balance.proto\x1a crypto_get_account_records.proto\x1a\x15\x63rypto_get_info.proto\x1a\x1a\x63rypto_get_live_hash.proto\x1a\x18\x63rypto_get_stakers.proto\x1a\x17\x66ile_get_contents.proto\x1a\x13\x66ile_get_info.proto\x1a\x1dtransaction_get_receipt.proto\x1a\x1ctransaction_get_record.proto\x1a!transaction_get_fast_record.proto\x1a\x1e\x63onsensus_get_topic_info.proto\x1a\x1enetwork_get_version_info.proto\x1a network_get_execution_time.proto\x1a\x14token_get_info.proto\x1a\x17schedule_get_info.proto\x1a!token_get_account_nft_infos.proto\x1a\x18token_get_nft_info.proto\x1a\x19token_get_nft_infos.proto\"\xcf\x0b\n\x05Query\x12(\n\x08getByKey\x18\x01 \x01(\x0b\x32\x14.proto.GetByKeyQueryH\x00\x12\x36\n\x0fgetBySolidityID\x18\x02 \x01(\x0b\x32\x1b.proto.GetBySolidityIDQueryH\x00\x12:\n\x11\x63ontractCallLocal\x18\x03 \x01(\x0b\x32\x1d.proto.ContractCallLocalQueryH\x00\x12\x36\n\x0f\x63ontractGetInfo\x18\x04 \x01(\x0b\x32\x1b.proto.ContractGetInfoQueryH\x00\x12>\n\x13\x63ontractGetBytecode\x18\x05 \x01(\x0b\x32\x1f.proto.ContractGetBytecodeQueryH\x00\x12<\n\x12\x43ontractGetRecords\x18\x06 \x01(\x0b\x32\x1e.proto.ContractGetRecordsQueryH\x00\x12\x46\n\x17\x63ryptogetAccountBalance\x18\x07 \x01(\x0b\x32#.proto.CryptoGetAccountBalanceQueryH\x00\x12\x46\n\x17\x63ryptoGetAccountRecords\x18\x08 \x01(\x0b\x32#.proto.CryptoGetAccountRecordsQueryH\x00\x12\x32\n\rcryptoGetInfo\x18\t \x01(\x0b\x32\x19.proto.CryptoGetInfoQueryH\x00\x12:\n\x11\x63ryptoGetLiveHash\x18\n \x01(\x0b\x32\x1d.proto.CryptoGetLiveHashQueryH\x00\x12=\n\x15\x63ryptoGetProxyStakers\x18\x0b \x01(\x0b\x32\x1c.proto.CryptoGetStakersQueryH\x00\x12\x36\n\x0f\x66ileGetContents\x18\x0c \x01(\x0b\x32\x1b.proto.FileGetContentsQueryH\x00\x12.\n\x0b\x66ileGetInfo\x18\r \x01(\x0b\x32\x17.proto.FileGetInfoQueryH\x00\x12\x42\n\x15transactionGetReceipt\x18\x0e \x01(\x0b\x32!.proto.TransactionGetReceiptQueryH\x00\x12@\n\x14transactionGetRecord\x18\x0f \x01(\x0b\x32 .proto.TransactionGetRecordQueryH\x00\x12H\n\x18transactionGetFastRecord\x18\x10 \x01(\x0b\x32$.proto.TransactionGetFastRecordQueryH\x00\x12\x42\n\x15\x63onsensusGetTopicInfo\x18\x32 \x01(\x0b\x32!.proto.ConsensusGetTopicInfoQueryH\x00\x12\x42\n\x15networkGetVersionInfo\x18\x33 \x01(\x0b\x32!.proto.NetworkGetVersionInfoQueryH\x00\x12\x30\n\x0ctokenGetInfo\x18\x34 \x01(\x0b\x32\x18.proto.TokenGetInfoQueryH\x00\x12\x36\n\x0fscheduleGetInfo\x18\x35 \x01(\x0b\x32\x1b.proto.ScheduleGetInfoQueryH\x00\x12\x46\n\x17tokenGetAccountNftInfos\x18\x36 \x01(\x0b\x32#.proto.TokenGetAccountNftInfosQueryH\x00\x12\x36\n\x0ftokenGetNftInfo\x18\x37 \x01(\x0b\x32\x1b.proto.TokenGetNftInfoQueryH\x00\x12\x38\n\x10tokenGetNftInfos\x18\x38 \x01(\x0b\x32\x1c.proto.TokenGetNftInfosQueryH\x00\x12\x46\n\x17networkGetExecutionTime\x18\x39 \x01(\x0b\x32#.proto.NetworkGetExecutionTimeQueryH\x00\x42\x07\n\x05queryB&\n\"com.hederahashgraph.api.proto.javaP\x01\x62\x06proto3'
  ,
  dependencies=[get__by__key__pb2.DESCRIPTOR,get__by__solidity__id__pb2.DESCRIPTOR,contract__call__local__pb2.DESCRIPTOR,contract__get__info__pb2.DESCRIPTOR,contract__get__bytecode__pb2.DESCRIPTOR,contract__get__records__pb2.DESCRIPTOR,crypto__get__account__balance__pb2.DESCRIPTOR,crypto__get__account__records__pb2.DESCRIPTOR,crypto__get__info__pb2.DESCRIPTOR,crypto__get__live__hash__pb2.DESCRIPTOR,crypto__get__stakers__pb2.DESCRIPTOR,file__get__contents__pb2.DESCRIPTOR,file__get__info__pb2.DESCRIPTOR,transaction__get__receipt__pb2.DESCRIPTOR,transaction__get__record__pb2.DESCRIPTOR,transaction__get__fast__record__pb2.DESCRIPTOR,consensus__get__topic__info__pb2.DESCRIPTOR,network__get__version__info__pb2.DESCRIPTOR,network__get__execution__time__pb2.DESCRIPTOR,token__get__info__pb2.DESCRIPTOR,schedule__get__info__pb2.DESCRIPTOR,token__get__account__nft__infos__pb2.DESCRIPTOR,token__get__nft__info__pb2.DESCRIPTOR,token__get__nft__infos__pb2.DESCRIPTOR,])




_QUERY = _descriptor.Descriptor(
  name='Query',
  full_name='proto.Query',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='getByKey', full_name='proto.Query.getByKey', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='getBySolidityID', full_name='proto.Query.getBySolidityID', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='contractCallLocal', full_name='proto.Query.contractCallLocal', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='contractGetInfo', full_name='proto.Query.contractGetInfo', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='contractGetBytecode', full_name='proto.Query.contractGetBytecode', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='ContractGetRecords', full_name='proto.Query.ContractGetRecords', index=5,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='cryptogetAccountBalance', full_name='proto.Query.cryptogetAccountBalance', index=6,
      number=7, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='cryptoGetAccountRecords', full_name='proto.Query.cryptoGetAccountRecords', index=7,
      number=8, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='cryptoGetInfo', full_name='proto.Query.cryptoGetInfo', index=8,
      number=9, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='cryptoGetLiveHash', full_name='proto.Query.cryptoGetLiveHash', index=9,
      number=10, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='cryptoGetProxyStakers', full_name='proto.Query.cryptoGetProxyStakers', index=10,
      number=11, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='fileGetContents', full_name='proto.Query.fileGetContents', index=11,
      number=12, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='fileGetInfo', full_name='proto.Query.fileGetInfo', index=12,
      number=13, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='transactionGetReceipt', full_name='proto.Query.transactionGetReceipt', index=13,
      number=14, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='transactionGetRecord', full_name='proto.Query.transactionGetRecord', index=14,
      number=15, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='transactionGetFastRecord', full_name='proto.Query.transactionGetFastRecord', index=15,
      number=16, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='consensusGetTopicInfo', full_name='proto.Query.consensusGetTopicInfo', index=16,
      number=50, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='networkGetVersionInfo', full_name='proto.Query.networkGetVersionInfo', index=17,
      number=51, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='tokenGetInfo', full_name='proto.Query.tokenGetInfo', index=18,
      number=52, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='scheduleGetInfo', full_name='proto.Query.scheduleGetInfo', index=19,
      number=53, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='tokenGetAccountNftInfos', full_name='proto.Query.tokenGetAccountNftInfos', index=20,
      number=54, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='tokenGetNftInfo', full_name='proto.Query.tokenGetNftInfo', index=21,
      number=55, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='tokenGetNftInfos', full_name='proto.Query.tokenGetNftInfos', index=22,
      number=56, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='networkGetExecutionTime', full_name='proto.Query.networkGetExecutionTime', index=23,
      number=57, type=11, cpp_type=10, label=1,
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
    _descriptor.OneofDescriptor(
      name='query', full_name='proto.Query.query',
      index=0, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
  ],
  serialized_start=696,
  serialized_end=2183,
)

_QUERY.fields_by_name['getByKey'].message_type = get__by__key__pb2._GETBYKEYQUERY
_QUERY.fields_by_name['getBySolidityID'].message_type = get__by__solidity__id__pb2._GETBYSOLIDITYIDQUERY
_QUERY.fields_by_name['contractCallLocal'].message_type = contract__call__local__pb2._CONTRACTCALLLOCALQUERY
_QUERY.fields_by_name['contractGetInfo'].message_type = contract__get__info__pb2._CONTRACTGETINFOQUERY
_QUERY.fields_by_name['contractGetBytecode'].message_type = contract__get__bytecode__pb2._CONTRACTGETBYTECODEQUERY
_QUERY.fields_by_name['ContractGetRecords'].message_type = contract__get__records__pb2._CONTRACTGETRECORDSQUERY
_QUERY.fields_by_name['cryptogetAccountBalance'].message_type = crypto__get__account__balance__pb2._CRYPTOGETACCOUNTBALANCEQUERY
_QUERY.fields_by_name['cryptoGetAccountRecords'].message_type = crypto__get__account__records__pb2._CRYPTOGETACCOUNTRECORDSQUERY
_QUERY.fields_by_name['cryptoGetInfo'].message_type = crypto__get__info__pb2._CRYPTOGETINFOQUERY
_QUERY.fields_by_name['cryptoGetLiveHash'].message_type = crypto__get__live__hash__pb2._CRYPTOGETLIVEHASHQUERY
_QUERY.fields_by_name['cryptoGetProxyStakers'].message_type = crypto__get__stakers__pb2._CRYPTOGETSTAKERSQUERY
_QUERY.fields_by_name['fileGetContents'].message_type = file__get__contents__pb2._FILEGETCONTENTSQUERY
_QUERY.fields_by_name['fileGetInfo'].message_type = file__get__info__pb2._FILEGETINFOQUERY
_QUERY.fields_by_name['transactionGetReceipt'].message_type = transaction__get__receipt__pb2._TRANSACTIONGETRECEIPTQUERY
_QUERY.fields_by_name['transactionGetRecord'].message_type = transaction__get__record__pb2._TRANSACTIONGETRECORDQUERY
_QUERY.fields_by_name['transactionGetFastRecord'].message_type = transaction__get__fast__record__pb2._TRANSACTIONGETFASTRECORDQUERY
_QUERY.fields_by_name['consensusGetTopicInfo'].message_type = consensus__get__topic__info__pb2._CONSENSUSGETTOPICINFOQUERY
_QUERY.fields_by_name['networkGetVersionInfo'].message_type = network__get__version__info__pb2._NETWORKGETVERSIONINFOQUERY
_QUERY.fields_by_name['tokenGetInfo'].message_type = token__get__info__pb2._TOKENGETINFOQUERY
_QUERY.fields_by_name['scheduleGetInfo'].message_type = schedule__get__info__pb2._SCHEDULEGETINFOQUERY
_QUERY.fields_by_name['tokenGetAccountNftInfos'].message_type = token__get__account__nft__infos__pb2._TOKENGETACCOUNTNFTINFOSQUERY
_QUERY.fields_by_name['tokenGetNftInfo'].message_type = token__get__nft__info__pb2._TOKENGETNFTINFOQUERY
_QUERY.fields_by_name['tokenGetNftInfos'].message_type = token__get__nft__infos__pb2._TOKENGETNFTINFOSQUERY
_QUERY.fields_by_name['networkGetExecutionTime'].message_type = network__get__execution__time__pb2._NETWORKGETEXECUTIONTIMEQUERY
_QUERY.oneofs_by_name['query'].fields.append(
  _QUERY.fields_by_name['getByKey'])
_QUERY.fields_by_name['getByKey'].containing_oneof = _QUERY.oneofs_by_name['query']
_QUERY.oneofs_by_name['query'].fields.append(
  _QUERY.fields_by_name['getBySolidityID'])
_QUERY.fields_by_name['getBySolidityID'].containing_oneof = _QUERY.oneofs_by_name['query']
_QUERY.oneofs_by_name['query'].fields.append(
  _QUERY.fields_by_name['contractCallLocal'])
_QUERY.fields_by_name['contractCallLocal'].containing_oneof = _QUERY.oneofs_by_name['query']
_QUERY.oneofs_by_name['query'].fields.append(
  _QUERY.fields_by_name['contractGetInfo'])
_QUERY.fields_by_name['contractGetInfo'].containing_oneof = _QUERY.oneofs_by_name['query']
_QUERY.oneofs_by_name['query'].fields.append(
  _QUERY.fields_by_name['contractGetBytecode'])
_QUERY.fields_by_name['contractGetBytecode'].containing_oneof = _QUERY.oneofs_by_name['query']
_QUERY.oneofs_by_name['query'].fields.append(
  _QUERY.fields_by_name['ContractGetRecords'])
_QUERY.fields_by_name['ContractGetRecords'].containing_oneof = _QUERY.oneofs_by_name['query']
_QUERY.oneofs_by_name['query'].fields.append(
  _QUERY.fields_by_name['cryptogetAccountBalance'])
_QUERY.fields_by_name['cryptogetAccountBalance'].containing_oneof = _QUERY.oneofs_by_name['query']
_QUERY.oneofs_by_name['query'].fields.append(
  _QUERY.fields_by_name['cryptoGetAccountRecords'])
_QUERY.fields_by_name['cryptoGetAccountRecords'].containing_oneof = _QUERY.oneofs_by_name['query']
_QUERY.oneofs_by_name['query'].fields.append(
  _QUERY.fields_by_name['cryptoGetInfo'])
_QUERY.fields_by_name['cryptoGetInfo'].containing_oneof = _QUERY.oneofs_by_name['query']
_QUERY.oneofs_by_name['query'].fields.append(
  _QUERY.fields_by_name['cryptoGetLiveHash'])
_QUERY.fields_by_name['cryptoGetLiveHash'].containing_oneof = _QUERY.oneofs_by_name['query']
_QUERY.oneofs_by_name['query'].fields.append(
  _QUERY.fields_by_name['cryptoGetProxyStakers'])
_QUERY.fields_by_name['cryptoGetProxyStakers'].containing_oneof = _QUERY.oneofs_by_name['query']
_QUERY.oneofs_by_name['query'].fields.append(
  _QUERY.fields_by_name['fileGetContents'])
_QUERY.fields_by_name['fileGetContents'].containing_oneof = _QUERY.oneofs_by_name['query']
_QUERY.oneofs_by_name['query'].fields.append(
  _QUERY.fields_by_name['fileGetInfo'])
_QUERY.fields_by_name['fileGetInfo'].containing_oneof = _QUERY.oneofs_by_name['query']
_QUERY.oneofs_by_name['query'].fields.append(
  _QUERY.fields_by_name['transactionGetReceipt'])
_QUERY.fields_by_name['transactionGetReceipt'].containing_oneof = _QUERY.oneofs_by_name['query']
_QUERY.oneofs_by_name['query'].fields.append(
  _QUERY.fields_by_name['transactionGetRecord'])
_QUERY.fields_by_name['transactionGetRecord'].containing_oneof = _QUERY.oneofs_by_name['query']
_QUERY.oneofs_by_name['query'].fields.append(
  _QUERY.fields_by_name['transactionGetFastRecord'])
_QUERY.fields_by_name['transactionGetFastRecord'].containing_oneof = _QUERY.oneofs_by_name['query']
_QUERY.oneofs_by_name['query'].fields.append(
  _QUERY.fields_by_name['consensusGetTopicInfo'])
_QUERY.fields_by_name['consensusGetTopicInfo'].containing_oneof = _QUERY.oneofs_by_name['query']
_QUERY.oneofs_by_name['query'].fields.append(
  _QUERY.fields_by_name['networkGetVersionInfo'])
_QUERY.fields_by_name['networkGetVersionInfo'].containing_oneof = _QUERY.oneofs_by_name['query']
_QUERY.oneofs_by_name['query'].fields.append(
  _QUERY.fields_by_name['tokenGetInfo'])
_QUERY.fields_by_name['tokenGetInfo'].containing_oneof = _QUERY.oneofs_by_name['query']
_QUERY.oneofs_by_name['query'].fields.append(
  _QUERY.fields_by_name['scheduleGetInfo'])
_QUERY.fields_by_name['scheduleGetInfo'].containing_oneof = _QUERY.oneofs_by_name['query']
_QUERY.oneofs_by_name['query'].fields.append(
  _QUERY.fields_by_name['tokenGetAccountNftInfos'])
_QUERY.fields_by_name['tokenGetAccountNftInfos'].containing_oneof = _QUERY.oneofs_by_name['query']
_QUERY.oneofs_by_name['query'].fields.append(
  _QUERY.fields_by_name['tokenGetNftInfo'])
_QUERY.fields_by_name['tokenGetNftInfo'].containing_oneof = _QUERY.oneofs_by_name['query']
_QUERY.oneofs_by_name['query'].fields.append(
  _QUERY.fields_by_name['tokenGetNftInfos'])
_QUERY.fields_by_name['tokenGetNftInfos'].containing_oneof = _QUERY.oneofs_by_name['query']
_QUERY.oneofs_by_name['query'].fields.append(
  _QUERY.fields_by_name['networkGetExecutionTime'])
_QUERY.fields_by_name['networkGetExecutionTime'].containing_oneof = _QUERY.oneofs_by_name['query']
DESCRIPTOR.message_types_by_name['Query'] = _QUERY
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Query = _reflection.GeneratedProtocolMessageType('Query', (_message.Message,), {
  'DESCRIPTOR' : _QUERY,
  '__module__' : 'query_pb2'
  # @@protoc_insertion_point(class_scope:proto.Query)
  })
_sym_db.RegisterMessage(Query)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
