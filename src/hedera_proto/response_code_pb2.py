# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: response_code.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x13response_code.proto\x12\x05proto*\xc0L\n\x10ResponseCodeEnum\x12\x06\n\x02OK\x10\x00\x12\x17\n\x13INVALID_TRANSACTION\x10\x01\x12\x1b\n\x17PAYER_ACCOUNT_NOT_FOUND\x10\x02\x12\x18\n\x14INVALID_NODE_ACCOUNT\x10\x03\x12\x17\n\x13TRANSACTION_EXPIRED\x10\x04\x12\x1d\n\x19INVALID_TRANSACTION_START\x10\x05\x12 \n\x1cINVALID_TRANSACTION_DURATION\x10\x06\x12\x15\n\x11INVALID_SIGNATURE\x10\x07\x12\x11\n\rMEMO_TOO_LONG\x10\x08\x12\x17\n\x13INSUFFICIENT_TX_FEE\x10\t\x12\x1e\n\x1aINSUFFICIENT_PAYER_BALANCE\x10\n\x12\x19\n\x15\x44UPLICATE_TRANSACTION\x10\x0b\x12\x08\n\x04\x42USY\x10\x0c\x12\x11\n\rNOT_SUPPORTED\x10\r\x12\x13\n\x0fINVALID_FILE_ID\x10\x0e\x12\x16\n\x12INVALID_ACCOUNT_ID\x10\x0f\x12\x17\n\x13INVALID_CONTRACT_ID\x10\x10\x12\x1a\n\x16INVALID_TRANSACTION_ID\x10\x11\x12\x15\n\x11RECEIPT_NOT_FOUND\x10\x12\x12\x14\n\x10RECORD_NOT_FOUND\x10\x13\x12\x17\n\x13INVALID_SOLIDITY_ID\x10\x14\x12\x0b\n\x07UNKNOWN\x10\x15\x12\x0b\n\x07SUCCESS\x10\x16\x12\x10\n\x0c\x46\x41IL_INVALID\x10\x17\x12\x0c\n\x08\x46\x41IL_FEE\x10\x18\x12\x10\n\x0c\x46\x41IL_BALANCE\x10\x19\x12\x10\n\x0cKEY_REQUIRED\x10\x1a\x12\x10\n\x0c\x42\x41\x44_ENCODING\x10\x1b\x12 \n\x1cINSUFFICIENT_ACCOUNT_BALANCE\x10\x1c\x12\x1c\n\x18INVALID_SOLIDITY_ADDRESS\x10\x1d\x12\x14\n\x10INSUFFICIENT_GAS\x10\x1e\x12 \n\x1c\x43ONTRACT_SIZE_LIMIT_EXCEEDED\x10\x1f\x12%\n!LOCAL_CALL_MODIFICATION_EXCEPTION\x10 \x12\x1c\n\x18\x43ONTRACT_REVERT_EXECUTED\x10!\x12 \n\x1c\x43ONTRACT_EXECUTION_EXCEPTION\x10\"\x12\"\n\x1eINVALID_RECEIVING_NODE_ACCOUNT\x10#\x12\x18\n\x14MISSING_QUERY_HEADER\x10$\x12\x19\n\x15\x41\x43\x43OUNT_UPDATE_FAILED\x10%\x12\x18\n\x14INVALID_KEY_ENCODING\x10&\x12\x19\n\x15NULL_SOLIDITY_ADDRESS\x10\'\x12\x1a\n\x16\x43ONTRACT_UPDATE_FAILED\x10(\x12\x18\n\x14INVALID_QUERY_HEADER\x10)\x12\x19\n\x15INVALID_FEE_SUBMITTED\x10*\x12\x1b\n\x17INVALID_PAYER_SIGNATURE\x10+\x12\x14\n\x10KEY_NOT_PROVIDED\x10,\x12\x1b\n\x17INVALID_EXPIRATION_TIME\x10-\x12\x0f\n\x0bNO_WACL_KEY\x10.\x12\x16\n\x12\x46ILE_CONTENT_EMPTY\x10/\x12\x1b\n\x17INVALID_ACCOUNT_AMOUNTS\x10\x30\x12\x1a\n\x16\x45MPTY_TRANSACTION_BODY\x10\x31\x12\x1c\n\x18INVALID_TRANSACTION_BODY\x10\x32\x12*\n&INVALID_SIGNATURE_TYPE_MISMATCHING_KEY\x10\x33\x12+\n\'INVALID_SIGNATURE_COUNT_MISMATCHING_KEY\x10\x34\x12\x18\n\x14\x45MPTY_LIVE_HASH_BODY\x10\x35\x12\x13\n\x0f\x45MPTY_LIVE_HASH\x10\x36\x12\x18\n\x14\x45MPTY_LIVE_HASH_KEYS\x10\x37\x12\x1a\n\x16INVALID_LIVE_HASH_SIZE\x10\x38\x12\x14\n\x10\x45MPTY_QUERY_BODY\x10\x39\x12\x19\n\x15\x45MPTY_LIVE_HASH_QUERY\x10:\x12\x17\n\x13LIVE_HASH_NOT_FOUND\x10;\x12\x1d\n\x19\x41\x43\x43OUNT_ID_DOES_NOT_EXIST\x10<\x12\x1c\n\x18LIVE_HASH_ALREADY_EXISTS\x10=\x12\x15\n\x11INVALID_FILE_WACL\x10>\x12\x18\n\x14SERIALIZATION_FAILED\x10?\x12\x18\n\x14TRANSACTION_OVERSIZE\x10@\x12\x1f\n\x1bTRANSACTION_TOO_MANY_LAYERS\x10\x41\x12\x14\n\x10\x43ONTRACT_DELETED\x10\x42\x12\x17\n\x13PLATFORM_NOT_ACTIVE\x10\x43\x12\x17\n\x13KEY_PREFIX_MISMATCH\x10\x44\x12$\n PLATFORM_TRANSACTION_NOT_CREATED\x10\x45\x12\x1a\n\x16INVALID_RENEWAL_PERIOD\x10\x46\x12\x1c\n\x18INVALID_PAYER_ACCOUNT_ID\x10G\x12\x13\n\x0f\x41\x43\x43OUNT_DELETED\x10H\x12\x10\n\x0c\x46ILE_DELETED\x10I\x12\'\n#ACCOUNT_REPEATED_IN_ACCOUNT_AMOUNTS\x10J\x12$\n SETTING_NEGATIVE_ACCOUNT_BALANCE\x10K\x12\x15\n\x11OBTAINER_REQUIRED\x10L\x12\x1d\n\x19OBTAINER_SAME_CONTRACT_ID\x10M\x12\x1b\n\x17OBTAINER_DOES_NOT_EXIST\x10N\x12 \n\x1cMODIFYING_IMMUTABLE_CONTRACT\x10O\x12\x19\n\x15\x46ILE_SYSTEM_EXCEPTION\x10P\x12#\n\x1f\x41UTORENEW_DURATION_NOT_IN_RANGE\x10Q\x12\x1d\n\x19\x45RROR_DECODING_BYTESTRING\x10R\x12\x17\n\x13\x43ONTRACT_FILE_EMPTY\x10S\x12\x1b\n\x17\x43ONTRACT_BYTECODE_EMPTY\x10T\x12\x1b\n\x17INVALID_INITIAL_BALANCE\x10U\x12(\n INVALID_RECEIVE_RECORD_THRESHOLD\x10V\x1a\x02\x08\x01\x12%\n\x1dINVALID_SEND_RECORD_THRESHOLD\x10W\x1a\x02\x08\x01\x12\"\n\x1e\x41\x43\x43OUNT_IS_NOT_GENESIS_ACCOUNT\x10X\x12\x1e\n\x1aPAYER_ACCOUNT_UNAUTHORIZED\x10Y\x12#\n\x1fINVALID_FREEZE_TRANSACTION_BODY\x10Z\x12%\n!FREEZE_TRANSACTION_BODY_NOT_FOUND\x10[\x12%\n!TRANSFER_LIST_SIZE_LIMIT_EXCEEDED\x10\\\x12\x1e\n\x1aRESULT_SIZE_LIMIT_EXCEEDED\x10]\x12\x17\n\x13NOT_SPECIAL_ACCOUNT\x10^\x12\x19\n\x15\x43ONTRACT_NEGATIVE_GAS\x10_\x12\x1b\n\x17\x43ONTRACT_NEGATIVE_VALUE\x10`\x12\x14\n\x10INVALID_FEE_FILE\x10\x61\x12\x1e\n\x1aINVALID_EXCHANGE_RATE_FILE\x10\x62\x12\x1f\n\x1bINSUFFICIENT_LOCAL_CALL_GAS\x10\x63\x12 \n\x1c\x45NTITY_NOT_ALLOWED_TO_DELETE\x10\x64\x12\x18\n\x14\x41UTHORIZATION_FAILED\x10\x65\x12\x1f\n\x1b\x46ILE_UPLOADED_PROTO_INVALID\x10\x66\x12)\n%FILE_UPLOADED_PROTO_NOT_SAVED_TO_DISK\x10g\x12#\n\x1f\x46\x45\x45_SCHEDULE_FILE_PART_UPLOADED\x10h\x12\'\n#EXCHANGE_RATE_CHANGE_LIMIT_EXCEEDED\x10i\x12!\n\x1dMAX_CONTRACT_STORAGE_EXCEEDED\x10j\x12+\n\'TRANSFER_ACCOUNT_SAME_AS_DELETE_ACCOUNT\x10k\x12 \n\x1cTOTAL_LEDGER_BALANCE_INVALID\x10l\x12$\n EXPIRATION_REDUCTION_NOT_ALLOWED\x10n\x12\x1a\n\x16MAX_GAS_LIMIT_EXCEEDED\x10o\x12\x1a\n\x16MAX_FILE_SIZE_EXCEEDED\x10p\x12\x19\n\x15RECEIVER_SIG_REQUIRED\x10q\x12\x15\n\x10INVALID_TOPIC_ID\x10\x96\x01\x12\x16\n\x11INVALID_ADMIN_KEY\x10\x9b\x01\x12\x17\n\x12INVALID_SUBMIT_KEY\x10\x9c\x01\x12\x11\n\x0cUNAUTHORIZED\x10\x9d\x01\x12\x1a\n\x15INVALID_TOPIC_MESSAGE\x10\x9e\x01\x12\x1e\n\x19INVALID_AUTORENEW_ACCOUNT\x10\x9f\x01\x12\"\n\x1d\x41UTORENEW_ACCOUNT_NOT_ALLOWED\x10\xa0\x01\x12\x12\n\rTOPIC_EXPIRED\x10\xa2\x01\x12\x19\n\x14INVALID_CHUNK_NUMBER\x10\xa3\x01\x12!\n\x1cINVALID_CHUNK_TRANSACTION_ID\x10\xa4\x01\x12\x1d\n\x18\x41\x43\x43OUNT_FROZEN_FOR_TOKEN\x10\xa5\x01\x12&\n!TOKENS_PER_ACCOUNT_LIMIT_EXCEEDED\x10\xa6\x01\x12\x15\n\x10INVALID_TOKEN_ID\x10\xa7\x01\x12\x1b\n\x16INVALID_TOKEN_DECIMALS\x10\xa8\x01\x12!\n\x1cINVALID_TOKEN_INITIAL_SUPPLY\x10\xa9\x01\x12\'\n\"INVALID_TREASURY_ACCOUNT_FOR_TOKEN\x10\xaa\x01\x12\x19\n\x14INVALID_TOKEN_SYMBOL\x10\xab\x01\x12\x1c\n\x17TOKEN_HAS_NO_FREEZE_KEY\x10\xac\x01\x12%\n TRANSFERS_NOT_ZERO_SUM_FOR_TOKEN\x10\xad\x01\x12\x19\n\x14MISSING_TOKEN_SYMBOL\x10\xae\x01\x12\x1a\n\x15TOKEN_SYMBOL_TOO_LONG\x10\xaf\x01\x12&\n!ACCOUNT_KYC_NOT_GRANTED_FOR_TOKEN\x10\xb0\x01\x12\x19\n\x14TOKEN_HAS_NO_KYC_KEY\x10\xb1\x01\x12\x1f\n\x1aINSUFFICIENT_TOKEN_BALANCE\x10\xb2\x01\x12\x16\n\x11TOKEN_WAS_DELETED\x10\xb3\x01\x12\x1c\n\x17TOKEN_HAS_NO_SUPPLY_KEY\x10\xb4\x01\x12\x1a\n\x15TOKEN_HAS_NO_WIPE_KEY\x10\xb5\x01\x12\x1e\n\x19INVALID_TOKEN_MINT_AMOUNT\x10\xb6\x01\x12\x1e\n\x19INVALID_TOKEN_BURN_AMOUNT\x10\xb7\x01\x12$\n\x1fTOKEN_NOT_ASSOCIATED_TO_ACCOUNT\x10\xb8\x01\x12\'\n\"CANNOT_WIPE_TOKEN_TREASURY_ACCOUNT\x10\xb9\x01\x12\x14\n\x0fINVALID_KYC_KEY\x10\xba\x01\x12\x15\n\x10INVALID_WIPE_KEY\x10\xbb\x01\x12\x17\n\x12INVALID_FREEZE_KEY\x10\xbc\x01\x12\x17\n\x12INVALID_SUPPLY_KEY\x10\xbd\x01\x12\x17\n\x12MISSING_TOKEN_NAME\x10\xbe\x01\x12\x18\n\x13TOKEN_NAME_TOO_LONG\x10\xbf\x01\x12\x1a\n\x15INVALID_WIPING_AMOUNT\x10\xc0\x01\x12\x17\n\x12TOKEN_IS_IMMUTABLE\x10\xc1\x01\x12(\n#TOKEN_ALREADY_ASSOCIATED_TO_ACCOUNT\x10\xc2\x01\x12-\n(TRANSACTION_REQUIRES_ZERO_TOKEN_BALANCES\x10\xc3\x01\x12\x18\n\x13\x41\x43\x43OUNT_IS_TREASURY\x10\xc4\x01\x12$\n\x1fTOKEN_ID_REPEATED_IN_TOKEN_LIST\x10\xc5\x01\x12,\n\'TOKEN_TRANSFER_LIST_SIZE_LIMIT_EXCEEDED\x10\xc6\x01\x12\x1e\n\x19\x45MPTY_TOKEN_TRANSFER_BODY\x10\xc7\x01\x12)\n$EMPTY_TOKEN_TRANSFER_ACCOUNT_AMOUNTS\x10\xc8\x01\x12\x18\n\x13INVALID_SCHEDULE_ID\x10\xc9\x01\x12\x1a\n\x15SCHEDULE_IS_IMMUTABLE\x10\xca\x01\x12\x1e\n\x19INVALID_SCHEDULE_PAYER_ID\x10\xcb\x01\x12 \n\x1bINVALID_SCHEDULE_ACCOUNT_ID\x10\xcc\x01\x12\x1c\n\x17NO_NEW_VALID_SIGNATURES\x10\xcd\x01\x12\"\n\x1dUNRESOLVABLE_REQUIRED_SIGNERS\x10\xce\x01\x12+\n&SCHEDULED_TRANSACTION_NOT_IN_WHITELIST\x10\xcf\x01\x12!\n\x1cSOME_SIGNATURES_WERE_INVALID\x10\xd0\x01\x12%\n TRANSACTION_ID_FIELD_NOT_ALLOWED\x10\xd1\x01\x12\'\n\"IDENTICAL_SCHEDULE_ALREADY_CREATED\x10\xd2\x01\x12 \n\x1bINVALID_ZERO_BYTE_IN_STRING\x10\xd3\x01\x12\x1d\n\x18SCHEDULE_ALREADY_DELETED\x10\xd4\x01\x12\x1e\n\x19SCHEDULE_ALREADY_EXECUTED\x10\xd5\x01\x12\x1b\n\x16MESSAGE_SIZE_TOO_LARGE\x10\xd6\x01\x12(\n#OPERATION_REPEATED_IN_BUCKET_GROUPS\x10\xd7\x01\x12\x1d\n\x18\x42UCKET_CAPACITY_OVERFLOW\x10\xd8\x01\x12/\n*NODE_CAPACITY_NOT_SUFFICIENT_FOR_OPERATION\x10\xd9\x01\x12\"\n\x1d\x42UCKET_HAS_NO_THROTTLE_GROUPS\x10\xda\x01\x12(\n#THROTTLE_GROUP_HAS_ZERO_OPS_PER_SEC\x10\xdb\x01\x12+\n&SUCCESS_BUT_MISSING_EXPECTED_OPERATION\x10\xdc\x01\x12%\n UNPARSEABLE_THROTTLE_DEFINITIONS\x10\xdd\x01\x12!\n\x1cINVALID_THROTTLE_DEFINITIONS\x10\xde\x01\x12(\n#ACCOUNT_EXPIRED_AND_PENDING_REMOVAL\x10\xdf\x01\x12\x1d\n\x18INVALID_TOKEN_MAX_SUPPLY\x10\xe0\x01\x12$\n\x1fINVALID_TOKEN_NFT_SERIAL_NUMBER\x10\xe1\x01\x12\x13\n\x0eINVALID_NFT_ID\x10\xe2\x01\x12\x16\n\x11METADATA_TOO_LONG\x10\xe3\x01\x12\x1e\n\x19\x42\x41TCH_SIZE_LIMIT_EXCEEDED\x10\xe4\x01\x12\x18\n\x13INVALID_QUERY_RANGE\x10\xe5\x01\x12\x1d\n\x18\x46RACTION_DIVIDES_BY_ZERO\x10\xe6\x01\x12\x32\n)INSUFFICIENT_PAYER_BALANCE_FOR_CUSTOM_FEE\x10\xe7\x01\x1a\x02\x08\x01\x12\x1e\n\x19\x43USTOM_FEES_LIST_TOO_LONG\x10\xe8\x01\x12!\n\x1cINVALID_CUSTOM_FEE_COLLECTOR\x10\xe9\x01\x12$\n\x1fINVALID_TOKEN_ID_IN_CUSTOM_FEES\x10\xea\x01\x12*\n%TOKEN_NOT_ASSOCIATED_TO_FEE_COLLECTOR\x10\xeb\x01\x12\x1d\n\x18TOKEN_MAX_SUPPLY_REACHED\x10\xec\x01\x12&\n!SENDER_DOES_NOT_OWN_NFT_SERIAL_NO\x10\xed\x01\x12#\n\x1e\x43USTOM_FEE_NOT_FULLY_SPECIFIED\x10\xee\x01\x12 \n\x1b\x43USTOM_FEE_MUST_BE_POSITIVE\x10\xef\x01\x12\"\n\x1dTOKEN_HAS_NO_FEE_SCHEDULE_KEY\x10\xf0\x01\x12%\n CUSTOM_FEE_OUTSIDE_NUMERIC_RANGE\x10\xf1\x01\x12\'\n\"ROYALTY_FRACTION_CANNOT_EXCEED_ONE\x10\xf2\x01\x12\x33\n.FRACTIONAL_FEE_MAX_AMOUNT_LESS_THAN_MIN_AMOUNT\x10\xf3\x01\x12(\n#CUSTOM_SCHEDULE_ALREADY_HAS_NO_FEES\x10\xf4\x01\x12\x34\n/CUSTOM_FEE_DENOMINATION_MUST_BE_FUNGIBLE_COMMON\x10\xf5\x01\x12;\n6CUSTOM_FRACTIONAL_FEE_ONLY_ALLOWED_FOR_FUNGIBLE_COMMON\x10\xf6\x01\x12$\n\x1fINVALID_CUSTOM_FEE_SCHEDULE_KEY\x10\xf7\x01\x12 \n\x1bINVALID_TOKEN_MINT_METADATA\x10\xf8\x01\x12 \n\x1bINVALID_TOKEN_BURN_METADATA\x10\xf9\x01\x12%\n CURRENT_TREASURY_STILL_OWNS_NFTS\x10\xfa\x01\x12\x1c\n\x17\x41\x43\x43OUNT_STILL_OWNS_NFTS\x10\xfb\x01\x12!\n\x1cTREASURY_MUST_OWN_BURNED_NFT\x10\xfc\x01\x12#\n\x1e\x41\x43\x43OUNT_DOES_NOT_OWN_WIPED_NFT\x10\xfd\x01\x12>\n9ACCOUNT_AMOUNT_TRANSFERS_ONLY_ALLOWED_FOR_FUNGIBLE_COMMON\x10\xfe\x01\x12.\n)MAX_NFTS_IN_PRICE_REGIME_HAVE_BEEN_MINTED\x10\xff\x01\x12\x1a\n\x15PAYER_ACCOUNT_DELETED\x10\x80\x02\x12\x35\n0CUSTOM_FEE_CHARGING_EXCEEDED_MAX_RECURSION_DEPTH\x10\x81\x02\x12\x35\n0CUSTOM_FEE_CHARGING_EXCEEDED_MAX_ACCOUNT_AMOUNTS\x10\x82\x02\x12\x37\n2INSUFFICIENT_SENDER_ACCOUNT_BALANCE_FOR_CUSTOM_FEE\x10\x83\x02\x12 \n\x1bSERIAL_NUMBER_LIMIT_REACHED\x10\x84\x02\x12<\n7CUSTOM_ROYALTY_FEE_ONLY_ALLOWED_FOR_NON_FUNGIBLE_UNIQUE\x10\x85\x02\x12(\n#NO_REMAINING_AUTOMATIC_ASSOCIATIONS\x10\x86\x02\x12\x37\n2EXISTING_AUTOMATIC_ASSOCIATIONS_EXCEED_GIVEN_LIMIT\x10\x87\x02\x12\x43\n>REQUESTED_NUM_AUTOMATIC_ASSOCIATIONS_EXCEEDS_ASSOCIATION_LIMIT\x10\x88\x02\x12\x14\n\x0fTOKEN_IS_PAUSED\x10\x89\x02\x12\x1b\n\x16TOKEN_HAS_NO_PAUSE_KEY\x10\x8a\x02\x12\x16\n\x11INVALID_PAUSE_KEY\x10\x8b\x02\x12&\n!FREEZE_UPDATE_FILE_DOES_NOT_EXIST\x10\x8c\x02\x12+\n&FREEZE_UPDATE_FILE_HASH_DOES_NOT_MATCH\x10\x8d\x02\x12!\n\x1cNO_UPGRADE_HAS_BEEN_PREPARED\x10\x8e\x02\x12\x1b\n\x16NO_FREEZE_IS_SCHEDULED\x10\x8f\x02\x12\x33\n.UPDATE_FILE_HASH_CHANGED_SINCE_PREPARE_UPGRADE\x10\x90\x02\x12%\n FREEZE_START_TIME_MUST_BE_FUTURE\x10\x91\x02\x12&\n!PREPARED_UPDATE_FILE_IS_IMMUTABLE\x10\x92\x02\x12\x1d\n\x18\x46REEZE_ALREADY_SCHEDULED\x10\x93\x02\x12\x1f\n\x1a\x46REEZE_UPGRADE_IN_PROGRESS\x10\x94\x02\x12+\n&UPDATE_FILE_ID_DOES_NOT_MATCH_PREPARED\x10\x95\x02\x12-\n(UPDATE_FILE_HASH_DOES_NOT_MATCH_PREPARED\x10\x96\x02\x12\x1c\n\x17\x43ONSENSUS_GAS_EXHAUSTED\x10\x97\x02\x12\x15\n\x10REVERTED_SUCCESS\x10\x98\x02\x12.\n)MAX_STORAGE_IN_PRICE_REGIME_HAS_BEEN_USED\x10\x99\x02\x12\x16\n\x11INVALID_ALIAS_KEY\x10\x9a\x02\x12\x1e\n\x19UNEXPECTED_TOKEN_DECIMALS\x10\x9b\x02\x12!\n\x18INVALID_PROXY_ACCOUNT_ID\x10\x9c\x02\x1a\x02\x08\x01\x12 \n\x1bINVALID_TRANSFER_ACCOUNT_ID\x10\x9d\x02\x12%\n INVALID_FEE_COLLECTOR_ACCOUNT_ID\x10\x9e\x02\x12\x17\n\x12\x41LIAS_IS_IMMUTABLE\x10\x9f\x02\x12\"\n\x1dSPENDER_ACCOUNT_SAME_AS_OWNER\x10\xa0\x02\x12$\n\x1f\x41MOUNT_EXCEEDS_TOKEN_MAX_SUPPLY\x10\xa1\x02\x12\x1e\n\x19NEGATIVE_ALLOWANCE_AMOUNT\x10\xa2\x02\x12/\n&CANNOT_APPROVE_FOR_ALL_FUNGIBLE_COMMON\x10\xa3\x02\x1a\x02\x08\x01\x12$\n\x1fSPENDER_DOES_NOT_HAVE_ALLOWANCE\x10\xa4\x02\x12\x1d\n\x18\x41MOUNT_EXCEEDS_ALLOWANCE\x10\xa5\x02\x12\x1c\n\x17MAX_ALLOWANCES_EXCEEDED\x10\xa6\x02\x12\x15\n\x10\x45MPTY_ALLOWANCES\x10\xa7\x02\x12/\n&SPENDER_ACCOUNT_REPEATED_IN_ALLOWANCES\x10\xa8\x02\x1a\x02\x08\x01\x12/\n&REPEATED_SERIAL_NUMS_IN_NFT_ALLOWANCES\x10\xa9\x02\x1a\x02\x08\x01\x12%\n FUNGIBLE_TOKEN_IN_NFT_ALLOWANCES\x10\xaa\x02\x12%\n NFT_IN_FUNGIBLE_TOKEN_ALLOWANCES\x10\xab\x02\x12\x1f\n\x1aINVALID_ALLOWANCE_OWNER_ID\x10\xac\x02\x12!\n\x1cINVALID_ALLOWANCE_SPENDER_ID\x10\xad\x02\x12&\n\x1dREPEATED_ALLOWANCES_TO_DELETE\x10\xae\x02\x1a\x02\x08\x01\x12\x1f\n\x1aINVALID_DELEGATING_SPENDER\x10\xaf\x02\x12\x34\n/DELEGATING_SPENDER_CANNOT_GRANT_APPROVE_FOR_ALL\x10\xb0\x02\x12\x35\n0DELEGATING_SPENDER_DOES_NOT_HAVE_APPROVE_FOR_ALL\x10\xb1\x02\x12/\n*SCHEDULE_EXPIRATION_TIME_TOO_FAR_IN_FUTURE\x10\xb2\x02\x12@\n;SCHEDULE_EXPIRATION_TIME_MUST_BE_HIGHER_THAN_CONSENSUS_TIME\x10\xb3\x02\x12&\n!SCHEDULE_FUTURE_THROTTLE_EXCEEDED\x10\xb4\x02\x12\'\n\"SCHEDULE_FUTURE_GAS_LIMIT_EXCEEDED\x10\xb5\x02\x12!\n\x1cINVALID_ETHEREUM_TRANSACTION\x10\xb6\x02\x12\x13\n\x0eWRONG_CHAIN_ID\x10\xb7\x02\x12\x10\n\x0bWRONG_NONCE\x10\xb8\x02\x12\x1c\n\x17\x41\x43\x43\x45SS_LIST_UNSUPPORTED\x10\xb9\x02\x12 \n\x1bSCHEDULE_PENDING_EXPIRATION\x10\xba\x02\x12\x1f\n\x1a\x43ONTRACT_IS_TOKEN_TREASURY\x10\xbb\x02\x12)\n$CONTRACT_HAS_NON_ZERO_TOKEN_BALANCES\x10\xbc\x02\x12)\n$CONTRACT_EXPIRED_AND_PENDING_REMOVAL\x10\xbd\x02\x12\'\n\"CONTRACT_HAS_NO_AUTO_RENEW_ACCOUNT\x10\xbe\x02\x12\x31\n,PERMANENT_REMOVAL_REQUIRES_SYSTEM_INITIATION\x10\xbf\x02\x12)\n$PROXY_ACCOUNT_ID_FIELD_IS_DEPRECATED\x10\xc0\x02\x12 \n\x1bSELF_STAKING_IS_NOT_ALLOWED\x10\xc1\x02\x12\x17\n\x12INVALID_STAKING_ID\x10\xc2\x02\x12\x18\n\x13STAKING_NOT_ENABLED\x10\xc3\x02\x12\x17\n\x12INVALID_PRNG_RANGE\x10\xc4\x02\x12\x33\n.MAX_ENTITIES_IN_PRICE_REGIME_HAVE_BEEN_CREATED\x10\xc5\x02\x12\x31\n,INVALID_FULL_PREFIX_SIGNATURE_FOR_PRECOMPILE\x10\xc6\x02\x12+\n&INSUFFICIENT_BALANCES_FOR_STORAGE_RENT\x10\xc7\x02\x12\x1f\n\x1aMAX_CHILD_RECORDS_EXCEEDED\x10\xc8\x02\x12+\n&INSUFFICIENT_BALANCES_FOR_RENEWAL_FEES\x10\xc9\x02\x12#\n\x1eTRANSACTION_HAS_UNKNOWN_FIELDS\x10\xca\x02\x12\x19\n\x14\x41\x43\x43OUNT_IS_IMMUTABLE\x10\xcb\x02\x12\x1b\n\x16\x41LIAS_ALREADY_ASSIGNED\x10\xcc\x02\x12\x19\n\x14INVALID_METADATA_KEY\x10\xcd\x02\x12\x1e\n\x19TOKEN_HAS_NO_METADATA_KEY\x10\xce\x02\x12\x1b\n\x16MISSING_TOKEN_METADATA\x10\xcf\x02\x12\x1b\n\x16MISSING_SERIAL_NUMBERS\x10\xd0\x02\x42&\n\"com.hederahashgraph.api.proto.javaP\x01\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'response_code_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\"com.hederahashgraph.api.proto.javaP\001'
  _globals['_RESPONSECODEENUM'].values_by_name["INVALID_RECEIVE_RECORD_THRESHOLD"]._loaded_options = None
  _globals['_RESPONSECODEENUM'].values_by_name["INVALID_RECEIVE_RECORD_THRESHOLD"]._serialized_options = b'\010\001'
  _globals['_RESPONSECODEENUM'].values_by_name["INVALID_SEND_RECORD_THRESHOLD"]._loaded_options = None
  _globals['_RESPONSECODEENUM'].values_by_name["INVALID_SEND_RECORD_THRESHOLD"]._serialized_options = b'\010\001'
  _globals['_RESPONSECODEENUM'].values_by_name["INSUFFICIENT_PAYER_BALANCE_FOR_CUSTOM_FEE"]._loaded_options = None
  _globals['_RESPONSECODEENUM'].values_by_name["INSUFFICIENT_PAYER_BALANCE_FOR_CUSTOM_FEE"]._serialized_options = b'\010\001'
  _globals['_RESPONSECODEENUM'].values_by_name["INVALID_PROXY_ACCOUNT_ID"]._loaded_options = None
  _globals['_RESPONSECODEENUM'].values_by_name["INVALID_PROXY_ACCOUNT_ID"]._serialized_options = b'\010\001'
  _globals['_RESPONSECODEENUM'].values_by_name["CANNOT_APPROVE_FOR_ALL_FUNGIBLE_COMMON"]._loaded_options = None
  _globals['_RESPONSECODEENUM'].values_by_name["CANNOT_APPROVE_FOR_ALL_FUNGIBLE_COMMON"]._serialized_options = b'\010\001'
  _globals['_RESPONSECODEENUM'].values_by_name["SPENDER_ACCOUNT_REPEATED_IN_ALLOWANCES"]._loaded_options = None
  _globals['_RESPONSECODEENUM'].values_by_name["SPENDER_ACCOUNT_REPEATED_IN_ALLOWANCES"]._serialized_options = b'\010\001'
  _globals['_RESPONSECODEENUM'].values_by_name["REPEATED_SERIAL_NUMS_IN_NFT_ALLOWANCES"]._loaded_options = None
  _globals['_RESPONSECODEENUM'].values_by_name["REPEATED_SERIAL_NUMS_IN_NFT_ALLOWANCES"]._serialized_options = b'\010\001'
  _globals['_RESPONSECODEENUM'].values_by_name["REPEATED_ALLOWANCES_TO_DELETE"]._loaded_options = None
  _globals['_RESPONSECODEENUM'].values_by_name["REPEATED_ALLOWANCES_TO_DELETE"]._serialized_options = b'\010\001'
  _globals['_RESPONSECODEENUM']._serialized_start=31
  _globals['_RESPONSECODEENUM']._serialized_end=9823
# @@protoc_insertion_point(module_scope)
