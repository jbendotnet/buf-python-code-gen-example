# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from acmecorp.filemanagement.v1 import service_pb2 as acmecorp_dot_filemanagement_dot_v1_dot_service__pb2


class DownloadServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Download = channel.unary_unary(
                '/acmecorp.filemanagement.v1.DownloadService/Download',
                request_serializer=acmecorp_dot_filemanagement_dot_v1_dot_service__pb2.DownloadRequest.SerializeToString,
                response_deserializer=acmecorp_dot_filemanagement_dot_v1_dot_service__pb2.DownloadResponse.FromString,
                )


class DownloadServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def Download(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_DownloadServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Download': grpc.unary_unary_rpc_method_handler(
                    servicer.Download,
                    request_deserializer=acmecorp_dot_filemanagement_dot_v1_dot_service__pb2.DownloadRequest.FromString,
                    response_serializer=acmecorp_dot_filemanagement_dot_v1_dot_service__pb2.DownloadResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'acmecorp.filemanagement.v1.DownloadService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class DownloadService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def Download(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/acmecorp.filemanagement.v1.DownloadService/Download',
            acmecorp_dot_filemanagement_dot_v1_dot_service__pb2.DownloadRequest.SerializeToString,
            acmecorp_dot_filemanagement_dot_v1_dot_service__pb2.DownloadResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
