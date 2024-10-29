from google.protobuf import empty_pb2 as _empty_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class UserLogin(_message.Message):
    __slots__ = ("login",)
    LOGIN_FIELD_NUMBER: _ClassVar[int]
    login: str
    def __init__(self, login: _Optional[str] = ...) -> None: ...

class UserLoginPassword(_message.Message):
    __slots__ = ("login", "password")
    LOGIN_FIELD_NUMBER: _ClassVar[int]
    PASSWORD_FIELD_NUMBER: _ClassVar[int]
    login: str
    password: str
    def __init__(self, login: _Optional[str] = ..., password: _Optional[str] = ...) -> None: ...

class User(_message.Message):
    __slots__ = ("login", "first_name", "last_name", "email", "groups", "is_active", "telegram_id", "password")
    LOGIN_FIELD_NUMBER: _ClassVar[int]
    FIRST_NAME_FIELD_NUMBER: _ClassVar[int]
    LAST_NAME_FIELD_NUMBER: _ClassVar[int]
    EMAIL_FIELD_NUMBER: _ClassVar[int]
    GROUPS_FIELD_NUMBER: _ClassVar[int]
    IS_ACTIVE_FIELD_NUMBER: _ClassVar[int]
    TELEGRAM_ID_FIELD_NUMBER: _ClassVar[int]
    PASSWORD_FIELD_NUMBER: _ClassVar[int]
    login: str
    first_name: str
    last_name: str
    email: str
    groups: str
    is_active: str
    telegram_id: int
    password: str
    def __init__(self, login: _Optional[str] = ..., first_name: _Optional[str] = ..., last_name: _Optional[str] = ..., email: _Optional[str] = ..., groups: _Optional[str] = ..., is_active: _Optional[str] = ..., telegram_id: _Optional[int] = ..., password: _Optional[str] = ...) -> None: ...

class UsersList(_message.Message):
    __slots__ = ("users",)
    USERS_FIELD_NUMBER: _ClassVar[int]
    users: _containers.RepeatedCompositeFieldContainer[User]
    def __init__(self, users: _Optional[_Iterable[_Union[User, _Mapping]]] = ...) -> None: ...

class UserGrants(_message.Message):
    __slots__ = ("edit_self", "edit_all", "read_self", "read_all")
    EDIT_SELF_FIELD_NUMBER: _ClassVar[int]
    EDIT_ALL_FIELD_NUMBER: _ClassVar[int]
    READ_SELF_FIELD_NUMBER: _ClassVar[int]
    READ_ALL_FIELD_NUMBER: _ClassVar[int]
    edit_self: bool
    edit_all: bool
    read_self: bool
    read_all: bool
    def __init__(self, edit_self: bool = ..., edit_all: bool = ..., read_self: bool = ..., read_all: bool = ...) -> None: ...
