# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: proto/iam/users.proto
# Protobuf Python Version: 5.27.2
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(
    _runtime_version.Domain.PUBLIC,
    5,
    27,
    2,
    '',
    'proto/iam/users.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x15proto/iam/users.proto\x12\x05users\x1a\x1bgoogle/protobuf/empty.proto\"\x1a\n\tUserLogin\x12\r\n\x05login\x18\x01 \x01(\t\"4\n\x11UserLoginPassword\x12\r\n\x05login\x18\x01 \x01(\t\x12\x10\n\x08password\x18\x02 \x01(\t\"\xaa\x01\n\x04User\x12\r\n\x05login\x18\x01 \x01(\t\x12\x12\n\nfirst_name\x18\x02 \x01(\t\x12\x11\n\tlast_name\x18\x03 \x01(\t\x12\r\n\x05\x65mail\x18\x04 \x01(\t\x12\x0e\n\x06groups\x18\x05 \x01(\t\x12\x11\n\tis_active\x18\x06 \x01(\t\x12\x18\n\x0btelegram_id\x18\x07 \x01(\x03H\x00\x88\x01\x01\x12\x10\n\x08password\x18\x08 \x01(\tB\x0e\n\x0c_telegram_id\"\'\n\tUsersList\x12\x1a\n\x05users\x18\x01 \x03(\x0b\x32\x0b.users.User\"V\n\nUserGrants\x12\x11\n\tedit_self\x18\x01 \x01(\x08\x12\x10\n\x08\x65\x64it_all\x18\x02 \x01(\x08\x12\x11\n\tread_self\x18\x03 \x01(\x08\x12\x10\n\x08read_all\x18\x04 \x01(\x08\x32\xbf\x02\n\x05Users\x12*\n\x07GetUser\x12\x10.users.UserLogin\x1a\x0b.users.User\"\x00\x12\x36\n\x08GetUsers\x12\x16.google.protobuf.Empty\x1a\x10.users.UsersList\"\x00\x12(\n\nCreateUser\x12\x0b.users.User\x1a\x0b.users.User\"\x00\x12(\n\nUpdateUser\x12\x0b.users.User\x1a\x0b.users.User\"\x00\x12\x44\n\x0eUpdatePassword\x12\x18.users.UserLoginPassword\x1a\x16.google.protobuf.Empty\"\x00\x12\x38\n\nDeleteUser\x12\x10.users.UserLogin\x1a\x16.google.protobuf.Empty\"\x00\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'proto.iam.users_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_USERLOGIN']._serialized_start=61
  _globals['_USERLOGIN']._serialized_end=87
  _globals['_USERLOGINPASSWORD']._serialized_start=89
  _globals['_USERLOGINPASSWORD']._serialized_end=141
  _globals['_USER']._serialized_start=144
  _globals['_USER']._serialized_end=314
  _globals['_USERSLIST']._serialized_start=316
  _globals['_USERSLIST']._serialized_end=355
  _globals['_USERGRANTS']._serialized_start=357
  _globals['_USERGRANTS']._serialized_end=443
  _globals['_USERS']._serialized_start=446
  _globals['_USERS']._serialized_end=765
# @@protoc_insertion_point(module_scope)