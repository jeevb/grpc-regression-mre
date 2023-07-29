import logging
import os

import grpc
import echo_service_pb2
import echo_service_pb2_grpc

logging.basicConfig(level="INFO")


def main():
    with open(
        os.path.join(os.path.dirname(os.path.dirname(__file__)), "cert", "server.crt"),
        "rb",
    ) as f:
        creds = f.read()
    channel = grpc.secure_channel(
        os.environ["SERVER_URL"], grpc.ssl_channel_credentials(creds)
    )
    stub = echo_service_pb2_grpc.EchoServiceStub(channel)
    request = echo_service_pb2.EchoRequest(value="hello")
    response = stub.Echo(request)
    logging.info(f"Got response: {response}")


if __name__ == "__main__":
    main()
