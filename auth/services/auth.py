from grpc import ServicerContext, StatusCode
from proto.auth.auth_pb2_grpc import AuthServicer
from proto.auth.auth_pb2 import RefreshToken, UserToken, BotToken
from proto.iam.users_pb2 import UserLoginPassword

from core.config import Settings
from repositories.tokens import TokenRepository


class AuthService(AuthServicer):
    def __init__(self, settings: Settings):
        self.token_repository = TokenRepository(settings)

    def GetUserToken(self, request: UserLoginPassword, context: ServicerContext):
        """Missing associated documentation comment in .proto file."""
        context.set_code(StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def RefreshUserToken(self, request: RefreshToken, context: ServicerContext):
        """Missing associated documentation comment in .proto file."""
        context.set_code(StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DeleteUserToken(self, request: RefreshToken, context: ServicerContext):
        """Missing associated documentation comment in .proto file."""
        context.set_code(StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CheckUserToken(self, request: UserToken, context: ServicerContext):
        """Missing associated documentation comment in .proto file."""
        context.set_code(StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CheckBotToken(self, request: BotToken, context: ServicerContext):
        """Missing associated documentation comment in .proto file."""
        context.set_code(StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')
