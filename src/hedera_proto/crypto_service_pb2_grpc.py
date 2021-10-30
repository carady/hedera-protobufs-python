# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import query_pb2 as query__pb2
import response_pb2 as response__pb2
import transaction_pb2 as transaction__pb2
import transaction_response_pb2 as transaction__response__pb2


class CryptoServiceStub(object):
    """*
    Transactions and queries for the Crypto Service
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.createAccount = channel.unary_unary(
                '/proto.CryptoService/createAccount',
                request_serializer=transaction__pb2.Transaction.SerializeToString,
                response_deserializer=transaction__response__pb2.TransactionResponse.FromString,
                )
        self.updateAccount = channel.unary_unary(
                '/proto.CryptoService/updateAccount',
                request_serializer=transaction__pb2.Transaction.SerializeToString,
                response_deserializer=transaction__response__pb2.TransactionResponse.FromString,
                )
        self.cryptoTransfer = channel.unary_unary(
                '/proto.CryptoService/cryptoTransfer',
                request_serializer=transaction__pb2.Transaction.SerializeToString,
                response_deserializer=transaction__response__pb2.TransactionResponse.FromString,
                )
        self.cryptoDelete = channel.unary_unary(
                '/proto.CryptoService/cryptoDelete',
                request_serializer=transaction__pb2.Transaction.SerializeToString,
                response_deserializer=transaction__response__pb2.TransactionResponse.FromString,
                )
        self.addLiveHash = channel.unary_unary(
                '/proto.CryptoService/addLiveHash',
                request_serializer=transaction__pb2.Transaction.SerializeToString,
                response_deserializer=transaction__response__pb2.TransactionResponse.FromString,
                )
        self.deleteLiveHash = channel.unary_unary(
                '/proto.CryptoService/deleteLiveHash',
                request_serializer=transaction__pb2.Transaction.SerializeToString,
                response_deserializer=transaction__response__pb2.TransactionResponse.FromString,
                )
        self.getLiveHash = channel.unary_unary(
                '/proto.CryptoService/getLiveHash',
                request_serializer=query__pb2.Query.SerializeToString,
                response_deserializer=response__pb2.Response.FromString,
                )
        self.getAccountRecords = channel.unary_unary(
                '/proto.CryptoService/getAccountRecords',
                request_serializer=query__pb2.Query.SerializeToString,
                response_deserializer=response__pb2.Response.FromString,
                )
        self.cryptoGetBalance = channel.unary_unary(
                '/proto.CryptoService/cryptoGetBalance',
                request_serializer=query__pb2.Query.SerializeToString,
                response_deserializer=response__pb2.Response.FromString,
                )
        self.getAccountInfo = channel.unary_unary(
                '/proto.CryptoService/getAccountInfo',
                request_serializer=query__pb2.Query.SerializeToString,
                response_deserializer=response__pb2.Response.FromString,
                )
        self.getTransactionReceipts = channel.unary_unary(
                '/proto.CryptoService/getTransactionReceipts',
                request_serializer=query__pb2.Query.SerializeToString,
                response_deserializer=response__pb2.Response.FromString,
                )
        self.getFastTransactionRecord = channel.unary_unary(
                '/proto.CryptoService/getFastTransactionRecord',
                request_serializer=query__pb2.Query.SerializeToString,
                response_deserializer=response__pb2.Response.FromString,
                )
        self.getTxRecordByTxID = channel.unary_unary(
                '/proto.CryptoService/getTxRecordByTxID',
                request_serializer=query__pb2.Query.SerializeToString,
                response_deserializer=response__pb2.Response.FromString,
                )
        self.getStakersByAccountID = channel.unary_unary(
                '/proto.CryptoService/getStakersByAccountID',
                request_serializer=query__pb2.Query.SerializeToString,
                response_deserializer=response__pb2.Response.FromString,
                )


class CryptoServiceServicer(object):
    """*
    Transactions and queries for the Crypto Service
    """

    def createAccount(self, request, context):
        """*
        Creates a new account by submitting the transaction
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def updateAccount(self, request, context):
        """*
        Updates an account by submitting the transaction
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def cryptoTransfer(self, request, context):
        """*
        Initiates a transfer by submitting the transaction
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def cryptoDelete(self, request, context):
        """*
        Deletes and account by submitting the transaction
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def addLiveHash(self, request, context):
        """*
        (NOT CURRENTLY SUPPORTED) Adds a livehash
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def deleteLiveHash(self, request, context):
        """*
        (NOT CURRENTLY SUPPORTED) Deletes a livehash
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def getLiveHash(self, request, context):
        """*
        (NOT CURRENTLY SUPPORTED) Retrieves a livehash for an account
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def getAccountRecords(self, request, context):
        """*
        Returns all transactions in the last 180s of consensus time for which the given account was
        the effective payer <b>and</b> network property <tt>ledger.keepRecordsInState</tt> was
        <tt>true</tt>.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def cryptoGetBalance(self, request, context):
        """*
        Retrieves the balance of an account
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def getAccountInfo(self, request, context):
        """*
        Retrieves the metadata of an account
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def getTransactionReceipts(self, request, context):
        """*
        Retrieves the latest receipt for a transaction that is either awaiting consensus, or reached
        consensus in the last 180 seconds
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def getFastTransactionRecord(self, request, context):
        """*
        (NOT CURRENTLY SUPPORTED) Returns the records of transactions recently funded by an account
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def getTxRecordByTxID(self, request, context):
        """*
        Retrieves the record of a transaction that is either awaiting consensus, or reached consensus
        in the last 180 seconds
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def getStakersByAccountID(self, request, context):
        """*
        (NOT CURRENTLY SUPPORTED) Retrieves the stakers for a node by account id
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_CryptoServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'createAccount': grpc.unary_unary_rpc_method_handler(
                    servicer.createAccount,
                    request_deserializer=transaction__pb2.Transaction.FromString,
                    response_serializer=transaction__response__pb2.TransactionResponse.SerializeToString,
            ),
            'updateAccount': grpc.unary_unary_rpc_method_handler(
                    servicer.updateAccount,
                    request_deserializer=transaction__pb2.Transaction.FromString,
                    response_serializer=transaction__response__pb2.TransactionResponse.SerializeToString,
            ),
            'cryptoTransfer': grpc.unary_unary_rpc_method_handler(
                    servicer.cryptoTransfer,
                    request_deserializer=transaction__pb2.Transaction.FromString,
                    response_serializer=transaction__response__pb2.TransactionResponse.SerializeToString,
            ),
            'cryptoDelete': grpc.unary_unary_rpc_method_handler(
                    servicer.cryptoDelete,
                    request_deserializer=transaction__pb2.Transaction.FromString,
                    response_serializer=transaction__response__pb2.TransactionResponse.SerializeToString,
            ),
            'addLiveHash': grpc.unary_unary_rpc_method_handler(
                    servicer.addLiveHash,
                    request_deserializer=transaction__pb2.Transaction.FromString,
                    response_serializer=transaction__response__pb2.TransactionResponse.SerializeToString,
            ),
            'deleteLiveHash': grpc.unary_unary_rpc_method_handler(
                    servicer.deleteLiveHash,
                    request_deserializer=transaction__pb2.Transaction.FromString,
                    response_serializer=transaction__response__pb2.TransactionResponse.SerializeToString,
            ),
            'getLiveHash': grpc.unary_unary_rpc_method_handler(
                    servicer.getLiveHash,
                    request_deserializer=query__pb2.Query.FromString,
                    response_serializer=response__pb2.Response.SerializeToString,
            ),
            'getAccountRecords': grpc.unary_unary_rpc_method_handler(
                    servicer.getAccountRecords,
                    request_deserializer=query__pb2.Query.FromString,
                    response_serializer=response__pb2.Response.SerializeToString,
            ),
            'cryptoGetBalance': grpc.unary_unary_rpc_method_handler(
                    servicer.cryptoGetBalance,
                    request_deserializer=query__pb2.Query.FromString,
                    response_serializer=response__pb2.Response.SerializeToString,
            ),
            'getAccountInfo': grpc.unary_unary_rpc_method_handler(
                    servicer.getAccountInfo,
                    request_deserializer=query__pb2.Query.FromString,
                    response_serializer=response__pb2.Response.SerializeToString,
            ),
            'getTransactionReceipts': grpc.unary_unary_rpc_method_handler(
                    servicer.getTransactionReceipts,
                    request_deserializer=query__pb2.Query.FromString,
                    response_serializer=response__pb2.Response.SerializeToString,
            ),
            'getFastTransactionRecord': grpc.unary_unary_rpc_method_handler(
                    servicer.getFastTransactionRecord,
                    request_deserializer=query__pb2.Query.FromString,
                    response_serializer=response__pb2.Response.SerializeToString,
            ),
            'getTxRecordByTxID': grpc.unary_unary_rpc_method_handler(
                    servicer.getTxRecordByTxID,
                    request_deserializer=query__pb2.Query.FromString,
                    response_serializer=response__pb2.Response.SerializeToString,
            ),
            'getStakersByAccountID': grpc.unary_unary_rpc_method_handler(
                    servicer.getStakersByAccountID,
                    request_deserializer=query__pb2.Query.FromString,
                    response_serializer=response__pb2.Response.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'proto.CryptoService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class CryptoService(object):
    """*
    Transactions and queries for the Crypto Service
    """

    @staticmethod
    def createAccount(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/proto.CryptoService/createAccount',
            transaction__pb2.Transaction.SerializeToString,
            transaction__response__pb2.TransactionResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def updateAccount(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/proto.CryptoService/updateAccount',
            transaction__pb2.Transaction.SerializeToString,
            transaction__response__pb2.TransactionResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def cryptoTransfer(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/proto.CryptoService/cryptoTransfer',
            transaction__pb2.Transaction.SerializeToString,
            transaction__response__pb2.TransactionResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def cryptoDelete(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/proto.CryptoService/cryptoDelete',
            transaction__pb2.Transaction.SerializeToString,
            transaction__response__pb2.TransactionResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def addLiveHash(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/proto.CryptoService/addLiveHash',
            transaction__pb2.Transaction.SerializeToString,
            transaction__response__pb2.TransactionResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def deleteLiveHash(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/proto.CryptoService/deleteLiveHash',
            transaction__pb2.Transaction.SerializeToString,
            transaction__response__pb2.TransactionResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def getLiveHash(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/proto.CryptoService/getLiveHash',
            query__pb2.Query.SerializeToString,
            response__pb2.Response.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def getAccountRecords(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/proto.CryptoService/getAccountRecords',
            query__pb2.Query.SerializeToString,
            response__pb2.Response.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def cryptoGetBalance(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/proto.CryptoService/cryptoGetBalance',
            query__pb2.Query.SerializeToString,
            response__pb2.Response.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def getAccountInfo(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/proto.CryptoService/getAccountInfo',
            query__pb2.Query.SerializeToString,
            response__pb2.Response.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def getTransactionReceipts(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/proto.CryptoService/getTransactionReceipts',
            query__pb2.Query.SerializeToString,
            response__pb2.Response.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def getFastTransactionRecord(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/proto.CryptoService/getFastTransactionRecord',
            query__pb2.Query.SerializeToString,
            response__pb2.Response.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def getTxRecordByTxID(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/proto.CryptoService/getTxRecordByTxID',
            query__pb2.Query.SerializeToString,
            response__pb2.Response.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def getStakersByAccountID(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/proto.CryptoService/getStakersByAccountID',
            query__pb2.Query.SerializeToString,
            response__pb2.Response.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)