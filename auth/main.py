from core import setup_logger, Settings, GRPCServer
from services.auth import AuthService

# Services
from proto.auth.auth_pb2_grpc import add_AuthServicer_to_server


SETTINGS = Settings()


if __name__ == "__main__":
    setup_logger()
    server = GRPCServer(SETTINGS.APP_PORT, SETTINGS.MAX_WORKERS)
    add_AuthServicer_to_server(AuthService(SETTINGS), server.server)

    server.start()
