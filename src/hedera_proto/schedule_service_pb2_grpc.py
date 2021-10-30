# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import query_pb2 as query__pb2
import response_pb2 as response__pb2
import transaction_pb2 as transaction__pb2
import transaction_response_pb2 as transaction__response__pb2


class ScheduleServiceStub(object):
    """*
    Transactions and queries for the Schedule Service
    The Schedule Service allows transactions to be submitted without all the required signatures and
    allows anyone to provide the required signatures independently after a transaction has already
    been created.
    Execution:
    Scheduled Transactions are executed once all required signatures are collected and witnessed.
    Every time new signature is provided, a check is performed on the "readiness" of the execution.
    The Scheduled Transaction will be executed immediately after the transaction that triggered it
    and will be externalised in a separate Transaction Record.
    Transaction Record:
    The timestamp of the Scheduled Transaction will be equal to consensusTimestamp + 1 nano, where
    consensusTimestamp is the timestamp of the transaction that triggered the execution.
    The Transaction ID of the Scheduled Transaction will have the scheduled property set to true and
    inherit the transactionValidStart and accountID from the ScheduleCreate transaction.
    The scheduleRef property of the transaction record will be populated with the ScheduleID of the
    Scheduled Transaction.
    Post execution:
    Once a given Scheduled Transaction executes, it will be removed from the ledger and any upcoming
    operation referring the ScheduleID will resolve to INVALID_SCHEDULE_ID.
    Expiry:
    Scheduled Transactions have a global expiry time txExpiryTimeSecs (Currently set to 30 minutes).
    If txExpiryTimeSecs pass and the Scheduled Transaction haven't yet executed, it will be removed
    from the ledger as if ScheduleDelete operation is executed.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.createSchedule = channel.unary_unary(
                '/proto.ScheduleService/createSchedule',
                request_serializer=transaction__pb2.Transaction.SerializeToString,
                response_deserializer=transaction__response__pb2.TransactionResponse.FromString,
                )
        self.signSchedule = channel.unary_unary(
                '/proto.ScheduleService/signSchedule',
                request_serializer=transaction__pb2.Transaction.SerializeToString,
                response_deserializer=transaction__response__pb2.TransactionResponse.FromString,
                )
        self.deleteSchedule = channel.unary_unary(
                '/proto.ScheduleService/deleteSchedule',
                request_serializer=transaction__pb2.Transaction.SerializeToString,
                response_deserializer=transaction__response__pb2.TransactionResponse.FromString,
                )
        self.getScheduleInfo = channel.unary_unary(
                '/proto.ScheduleService/getScheduleInfo',
                request_serializer=query__pb2.Query.SerializeToString,
                response_deserializer=response__pb2.Response.FromString,
                )


class ScheduleServiceServicer(object):
    """*
    Transactions and queries for the Schedule Service
    The Schedule Service allows transactions to be submitted without all the required signatures and
    allows anyone to provide the required signatures independently after a transaction has already
    been created.
    Execution:
    Scheduled Transactions are executed once all required signatures are collected and witnessed.
    Every time new signature is provided, a check is performed on the "readiness" of the execution.
    The Scheduled Transaction will be executed immediately after the transaction that triggered it
    and will be externalised in a separate Transaction Record.
    Transaction Record:
    The timestamp of the Scheduled Transaction will be equal to consensusTimestamp + 1 nano, where
    consensusTimestamp is the timestamp of the transaction that triggered the execution.
    The Transaction ID of the Scheduled Transaction will have the scheduled property set to true and
    inherit the transactionValidStart and accountID from the ScheduleCreate transaction.
    The scheduleRef property of the transaction record will be populated with the ScheduleID of the
    Scheduled Transaction.
    Post execution:
    Once a given Scheduled Transaction executes, it will be removed from the ledger and any upcoming
    operation referring the ScheduleID will resolve to INVALID_SCHEDULE_ID.
    Expiry:
    Scheduled Transactions have a global expiry time txExpiryTimeSecs (Currently set to 30 minutes).
    If txExpiryTimeSecs pass and the Scheduled Transaction haven't yet executed, it will be removed
    from the ledger as if ScheduleDelete operation is executed.
    """

    def createSchedule(self, request, context):
        """*
        Creates a new Schedule by submitting the transaction
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def signSchedule(self, request, context):
        """*
        Signs a new Schedule by submitting the transaction
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def deleteSchedule(self, request, context):
        """*
        Deletes a new Schedule by submitting the transaction
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def getScheduleInfo(self, request, context):
        """*
        Retrieves the metadata of a schedule entity
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_ScheduleServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'createSchedule': grpc.unary_unary_rpc_method_handler(
                    servicer.createSchedule,
                    request_deserializer=transaction__pb2.Transaction.FromString,
                    response_serializer=transaction__response__pb2.TransactionResponse.SerializeToString,
            ),
            'signSchedule': grpc.unary_unary_rpc_method_handler(
                    servicer.signSchedule,
                    request_deserializer=transaction__pb2.Transaction.FromString,
                    response_serializer=transaction__response__pb2.TransactionResponse.SerializeToString,
            ),
            'deleteSchedule': grpc.unary_unary_rpc_method_handler(
                    servicer.deleteSchedule,
                    request_deserializer=transaction__pb2.Transaction.FromString,
                    response_serializer=transaction__response__pb2.TransactionResponse.SerializeToString,
            ),
            'getScheduleInfo': grpc.unary_unary_rpc_method_handler(
                    servicer.getScheduleInfo,
                    request_deserializer=query__pb2.Query.FromString,
                    response_serializer=response__pb2.Response.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'proto.ScheduleService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class ScheduleService(object):
    """*
    Transactions and queries for the Schedule Service
    The Schedule Service allows transactions to be submitted without all the required signatures and
    allows anyone to provide the required signatures independently after a transaction has already
    been created.
    Execution:
    Scheduled Transactions are executed once all required signatures are collected and witnessed.
    Every time new signature is provided, a check is performed on the "readiness" of the execution.
    The Scheduled Transaction will be executed immediately after the transaction that triggered it
    and will be externalised in a separate Transaction Record.
    Transaction Record:
    The timestamp of the Scheduled Transaction will be equal to consensusTimestamp + 1 nano, where
    consensusTimestamp is the timestamp of the transaction that triggered the execution.
    The Transaction ID of the Scheduled Transaction will have the scheduled property set to true and
    inherit the transactionValidStart and accountID from the ScheduleCreate transaction.
    The scheduleRef property of the transaction record will be populated with the ScheduleID of the
    Scheduled Transaction.
    Post execution:
    Once a given Scheduled Transaction executes, it will be removed from the ledger and any upcoming
    operation referring the ScheduleID will resolve to INVALID_SCHEDULE_ID.
    Expiry:
    Scheduled Transactions have a global expiry time txExpiryTimeSecs (Currently set to 30 minutes).
    If txExpiryTimeSecs pass and the Scheduled Transaction haven't yet executed, it will be removed
    from the ledger as if ScheduleDelete operation is executed.
    """

    @staticmethod
    def createSchedule(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/proto.ScheduleService/createSchedule',
            transaction__pb2.Transaction.SerializeToString,
            transaction__response__pb2.TransactionResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def signSchedule(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/proto.ScheduleService/signSchedule',
            transaction__pb2.Transaction.SerializeToString,
            transaction__response__pb2.TransactionResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def deleteSchedule(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/proto.ScheduleService/deleteSchedule',
            transaction__pb2.Transaction.SerializeToString,
            transaction__response__pb2.TransactionResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def getScheduleInfo(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/proto.ScheduleService/getScheduleInfo',
            query__pb2.Query.SerializeToString,
            response__pb2.Response.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
