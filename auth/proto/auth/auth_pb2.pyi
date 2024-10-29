from google.protobuf import empty_pb2 as _empty_pb2
from proto.iam import users_pb2 as _users_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class UserToken(_message.Message):
    __slots__ = ("refresh_token", "jwt_token")
    REFRESH_TOKEN_FIELD_NUMBER: _ClassVar[int]
    JWT_TOKEN_FIELD_NUMBER: _ClassVar[int]
    refresh_token: str
    jwt_token: str
    def __init__(self, refresh_token: _Optional[str] = ..., jwt_token: _Optional[str] = ...) -> None: ...

class RefreshToken(_message.Message):
    __slots__ = ("refresh_token",)
    REFRESH_TOKEN_FIELD_NUMBER: _ClassVar[int]
    refresh_token: str
    def __init__(self, refresh_token: _Optional[str] = ...) -> None: ...

class BotToken(_message.Message):
    __slots__ = ("name", "token")
    NAME_FIELD_NUMBER: _ClassVar[int]
    TOKEN_FIELD_NUMBER: _ClassVar[int]
    name: str
    token: str
    def __init__(self, name: _Optional[str] = ..., token: _Optional[str] = ...) -> None: ...
