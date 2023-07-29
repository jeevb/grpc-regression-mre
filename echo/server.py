import logging
from concurrent import futures

import grpc
from grpc_reflection.v1alpha import reflection
import echo_service_pb2
import echo_service_pb2_grpc

logging.basicConfig(level="DEBUG")


class EchoService(echo_service_pb2_grpc.EchoServiceServicer):
    def Echo(self, request, context):
        logging.debug(f"Got request: {request}")
        return echo_service_pb2.EchoResponse(value=request.value)


def main():
    # Create a gRPC server
    server = grpc.server(futures.ThreadPoolExecutor())

    # Add the mock service to the server
    echo_service_pb2_grpc.add_EchoServiceServicer_to_server(EchoService(), server)
    SERVICE_NAMES = (
        echo_service_pb2.DESCRIPTOR.services_by_name["EchoService"].full_name,
        reflection.SERVICE_NAME,
    )
    reflection.enable_server_reflection(SERVICE_NAMES, server)

    # Start the server on port 5000
    bind = "[::]:50051"
    server.add_insecure_port(bind)
    logging.info(f"Listening on: {bind}")
    server.start()
    server.wait_for_termination()


if __name__ == "__main__":
    main()
