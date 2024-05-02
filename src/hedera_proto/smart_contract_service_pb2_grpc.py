# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc
import warnings

import query_pb2 as query__pb2
import response_pb2 as response__pb2
import transaction_pb2 as transaction__pb2
import transaction_response_pb2 as transaction__response__pb2

GRPC_GENERATED_VERSION = '1.63.0'
GRPC_VERSION = grpc.__version__
EXPECTED_ERROR_RELEASE = '1.65.0'
SCHEDULED_RELEASE_DATE = 'June 25, 2024'
_version_not_supported = False

try:
    from grpc._utilities import first_version_is_lower
    _version_not_supported = first_version_is_lower(GRPC_VERSION, GRPC_GENERATED_VERSION)
except ImportError:
    _version_not_supported = True

if _version_not_supported:
    warnings.warn(
        f'The grpc package installed is at version {GRPC_VERSION},'
        + f' but the generated code in smart_contract_service_pb2_grpc.py depends on'
        + f' grpcio>={GRPC_GENERATED_VERSION}.'
        + f' Please upgrade your grpc module to grpcio>={GRPC_GENERATED_VERSION}'
        + f' or downgrade your generated code using grpcio-tools<={GRPC_VERSION}.'
        + f' This warning will become an error in {EXPECTED_ERROR_RELEASE},'
        + f' scheduled for release on {SCHEDULED_RELEASE_DATE}.',
        RuntimeWarning
    )


class SmartContractServiceStub(object):
    """*
    Transactions and queries for the file service. 
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.createContract = channel.unary_unary(
                '/proto.SmartContractService/createContract',
                request_serializer=transaction__pb2.Transaction.SerializeToString,
                response_deserializer=transaction__response__pb2.TransactionResponse.FromString,
                _registered_method=True)
        self.updateContract = channel.unary_unary(
                '/proto.SmartContractService/updateContract',
                request_serializer=transaction__pb2.Transaction.SerializeToString,
                response_deserializer=transaction__response__pb2.TransactionResponse.FromString,
                _registered_method=True)
        self.contractCallMethod = channel.unary_unary(
                '/proto.SmartContractService/contractCallMethod',
                request_serializer=transaction__pb2.Transaction.SerializeToString,
                response_deserializer=transaction__response__pb2.TransactionResponse.FromString,
                _registered_method=True)
        self.getContractInfo = channel.unary_unary(
                '/proto.SmartContractService/getContractInfo',
                request_serializer=query__pb2.Query.SerializeToString,
                response_deserializer=response__pb2.Response.FromString,
                _registered_method=True)
        self.contractCallLocalMethod = channel.unary_unary(
                '/proto.SmartContractService/contractCallLocalMethod',
                request_serializer=query__pb2.Query.SerializeToString,
                response_deserializer=response__pb2.Response.FromString,
                _registered_method=True)
        self.ContractGetBytecode = channel.unary_unary(
                '/proto.SmartContractService/ContractGetBytecode',
                request_serializer=query__pb2.Query.SerializeToString,
                response_deserializer=response__pb2.Response.FromString,
                _registered_method=True)
        self.getBySolidityID = channel.unary_unary(
                '/proto.SmartContractService/getBySolidityID',
                request_serializer=query__pb2.Query.SerializeToString,
                response_deserializer=response__pb2.Response.FromString,
                _registered_method=True)
        self.getTxRecordByContractID = channel.unary_unary(
                '/proto.SmartContractService/getTxRecordByContractID',
                request_serializer=query__pb2.Query.SerializeToString,
                response_deserializer=response__pb2.Response.FromString,
                _registered_method=True)
        self.deleteContract = channel.unary_unary(
                '/proto.SmartContractService/deleteContract',
                request_serializer=transaction__pb2.Transaction.SerializeToString,
                response_deserializer=transaction__response__pb2.TransactionResponse.FromString,
                _registered_method=True)
        self.systemDelete = channel.unary_unary(
                '/proto.SmartContractService/systemDelete',
                request_serializer=transaction__pb2.Transaction.SerializeToString,
                response_deserializer=transaction__response__pb2.TransactionResponse.FromString,
                _registered_method=True)
        self.systemUndelete = channel.unary_unary(
                '/proto.SmartContractService/systemUndelete',
                request_serializer=transaction__pb2.Transaction.SerializeToString,
                response_deserializer=transaction__response__pb2.TransactionResponse.FromString,
                _registered_method=True)
        self.callEthereum = channel.unary_unary(
                '/proto.SmartContractService/callEthereum',
                request_serializer=transaction__pb2.Transaction.SerializeToString,
                response_deserializer=transaction__response__pb2.TransactionResponse.FromString,
                _registered_method=True)


class SmartContractServiceServicer(object):
    """*
    Transactions and queries for the file service. 
    """

    def createContract(self, request, context):
        """*
        Creates a contract
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def updateContract(self, request, context):
        """*
        Updates a contract with the content
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def contractCallMethod(self, request, context):
        """*
        Calls a contract
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def getContractInfo(self, request, context):
        """*
        Retrieves the contract information
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def contractCallLocalMethod(self, request, context):
        """*
        Calls a smart contract to be run on a single node
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ContractGetBytecode(self, request, context):
        """*
        Retrieves the runtime code of a contract
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def getBySolidityID(self, request, context):
        """*
        Retrieves a contract by its Solidity address
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def getTxRecordByContractID(self, request, context):
        """*
        Always returns an empty record list, as contract accounts are never effective payers for
        transactions
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def deleteContract(self, request, context):
        """*
        Deletes a contract instance and transfers any remaining hbars to a specified receiver
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def systemDelete(self, request, context):
        """*
        Deletes a contract if the submitting account has network admin privileges
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def systemUndelete(self, request, context):
        """*
        Undeletes a contract if the submitting account has network admin privileges
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def callEthereum(self, request, context):
        """*
        Ethereum transaction
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_SmartContractServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'createContract': grpc.unary_unary_rpc_method_handler(
                    servicer.createContract,
                    request_deserializer=transaction__pb2.Transaction.FromString,
                    response_serializer=transaction__response__pb2.TransactionResponse.SerializeToString,
            ),
            'updateContract': grpc.unary_unary_rpc_method_handler(
                    servicer.updateContract,
                    request_deserializer=transaction__pb2.Transaction.FromString,
                    response_serializer=transaction__response__pb2.TransactionResponse.SerializeToString,
            ),
            'contractCallMethod': grpc.unary_unary_rpc_method_handler(
                    servicer.contractCallMethod,
                    request_deserializer=transaction__pb2.Transaction.FromString,
                    response_serializer=transaction__response__pb2.TransactionResponse.SerializeToString,
            ),
            'getContractInfo': grpc.unary_unary_rpc_method_handler(
                    servicer.getContractInfo,
                    request_deserializer=query__pb2.Query.FromString,
                    response_serializer=response__pb2.Response.SerializeToString,
            ),
            'contractCallLocalMethod': grpc.unary_unary_rpc_method_handler(
                    servicer.contractCallLocalMethod,
                    request_deserializer=query__pb2.Query.FromString,
                    response_serializer=response__pb2.Response.SerializeToString,
            ),
            'ContractGetBytecode': grpc.unary_unary_rpc_method_handler(
                    servicer.ContractGetBytecode,
                    request_deserializer=query__pb2.Query.FromString,
                    response_serializer=response__pb2.Response.SerializeToString,
            ),
            'getBySolidityID': grpc.unary_unary_rpc_method_handler(
                    servicer.getBySolidityID,
                    request_deserializer=query__pb2.Query.FromString,
                    response_serializer=response__pb2.Response.SerializeToString,
            ),
            'getTxRecordByContractID': grpc.unary_unary_rpc_method_handler(
                    servicer.getTxRecordByContractID,
                    request_deserializer=query__pb2.Query.FromString,
                    response_serializer=response__pb2.Response.SerializeToString,
            ),
            'deleteContract': grpc.unary_unary_rpc_method_handler(
                    servicer.deleteContract,
                    request_deserializer=transaction__pb2.Transaction.FromString,
                    response_serializer=transaction__response__pb2.TransactionResponse.SerializeToString,
            ),
            'systemDelete': grpc.unary_unary_rpc_method_handler(
                    servicer.systemDelete,
                    request_deserializer=transaction__pb2.Transaction.FromString,
                    response_serializer=transaction__response__pb2.TransactionResponse.SerializeToString,
            ),
            'systemUndelete': grpc.unary_unary_rpc_method_handler(
                    servicer.systemUndelete,
                    request_deserializer=transaction__pb2.Transaction.FromString,
                    response_serializer=transaction__response__pb2.TransactionResponse.SerializeToString,
            ),
            'callEthereum': grpc.unary_unary_rpc_method_handler(
                    servicer.callEthereum,
                    request_deserializer=transaction__pb2.Transaction.FromString,
                    response_serializer=transaction__response__pb2.TransactionResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'proto.SmartContractService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class SmartContractService(object):
    """*
    Transactions and queries for the file service. 
    """

    @staticmethod
    def createContract(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/proto.SmartContractService/createContract',
            transaction__pb2.Transaction.SerializeToString,
            transaction__response__pb2.TransactionResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def updateContract(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/proto.SmartContractService/updateContract',
            transaction__pb2.Transaction.SerializeToString,
            transaction__response__pb2.TransactionResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def contractCallMethod(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/proto.SmartContractService/contractCallMethod',
            transaction__pb2.Transaction.SerializeToString,
            transaction__response__pb2.TransactionResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def getContractInfo(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/proto.SmartContractService/getContractInfo',
            query__pb2.Query.SerializeToString,
            response__pb2.Response.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def contractCallLocalMethod(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/proto.SmartContractService/contractCallLocalMethod',
            query__pb2.Query.SerializeToString,
            response__pb2.Response.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def ContractGetBytecode(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/proto.SmartContractService/ContractGetBytecode',
            query__pb2.Query.SerializeToString,
            response__pb2.Response.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def getBySolidityID(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/proto.SmartContractService/getBySolidityID',
            query__pb2.Query.SerializeToString,
            response__pb2.Response.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def getTxRecordByContractID(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/proto.SmartContractService/getTxRecordByContractID',
            query__pb2.Query.SerializeToString,
            response__pb2.Response.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def deleteContract(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/proto.SmartContractService/deleteContract',
            transaction__pb2.Transaction.SerializeToString,
            transaction__response__pb2.TransactionResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def systemDelete(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/proto.SmartContractService/systemDelete',
            transaction__pb2.Transaction.SerializeToString,
            transaction__response__pb2.TransactionResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def systemUndelete(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/proto.SmartContractService/systemUndelete',
            transaction__pb2.Transaction.SerializeToString,
            transaction__response__pb2.TransactionResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def callEthereum(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/proto.SmartContractService/callEthereum',
            transaction__pb2.Transaction.SerializeToString,
            transaction__response__pb2.TransactionResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)
