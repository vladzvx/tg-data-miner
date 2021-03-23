# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: Configurator.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='Configurator.proto',
  package='snapshot',
  syntax='proto3',
  serialized_options=b'\252\002\006Common',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x12\x43onfigurator.proto\x12\x08snapshot\x1a\x1bgoogle/protobuf/empty.proto\"\x9b\x01\n\x16\x43onfigurationContainer\x12/\n\x0cSessionStore\x18\x01 \x01(\x0b\x32\x19.snapshot.SessionSettings\x12,\n\x0f\x43ollectorParams\x18\x02 \x01(\x0b\x32\x13.snapshot.Collector\x12\"\n\nUserParams\x18\x03 \x01(\x0b\x32\x0e.snapshot.User\"\x97\x01\n\x0fSessionSettings\x12\x12\n\nSQLDialect\x18\x01 \x01(\t\x12\x1a\n\x12SessionStorageUser\x18\x02 \x01(\t\x12\x1e\n\x16SessionStoragePassword\x18\x03 \x01(\t\x12\x1a\n\x12SessionStorageHost\x18\x04 \x01(\t\x12\x18\n\x10SessionStorageDB\x18\x05 \x01(\t\"+\n\tCollector\x12\r\n\x05\x41piId\x18\x01 \x01(\x03\x12\x0f\n\x07\x41piHash\x18\x02 \x01(\t\"I\n\x04User\x12\r\n\x05Phone\x18\x01 \x01(\t\x12\x13\n\x0bSessionName\x18\x02 \x01(\t\x12\x1d\n\x15GetFullChannelCounter\x18\x03 \x01(\x05\x32^\n\x0c\x43onfigurator\x12N\n\x10GetConfiguration\x12\x16.google.protobuf.Empty\x1a .snapshot.ConfigurationContainer0\x01\x42\t\xaa\x02\x06\x43ommonb\x06proto3'
  ,
  dependencies=[google_dot_protobuf_dot_empty__pb2.DESCRIPTOR,])




_CONFIGURATIONCONTAINER = _descriptor.Descriptor(
  name='ConfigurationContainer',
  full_name='snapshot.ConfigurationContainer',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='SessionStore', full_name='snapshot.ConfigurationContainer.SessionStore', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='CollectorParams', full_name='snapshot.ConfigurationContainer.CollectorParams', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='UserParams', full_name='snapshot.ConfigurationContainer.UserParams', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=62,
  serialized_end=217,
)


_SESSIONSETTINGS = _descriptor.Descriptor(
  name='SessionSettings',
  full_name='snapshot.SessionSettings',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='SQLDialect', full_name='snapshot.SessionSettings.SQLDialect', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='SessionStorageUser', full_name='snapshot.SessionSettings.SessionStorageUser', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='SessionStoragePassword', full_name='snapshot.SessionSettings.SessionStoragePassword', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='SessionStorageHost', full_name='snapshot.SessionSettings.SessionStorageHost', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='SessionStorageDB', full_name='snapshot.SessionSettings.SessionStorageDB', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=220,
  serialized_end=371,
)


_COLLECTOR = _descriptor.Descriptor(
  name='Collector',
  full_name='snapshot.Collector',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='ApiId', full_name='snapshot.Collector.ApiId', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='ApiHash', full_name='snapshot.Collector.ApiHash', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=373,
  serialized_end=416,
)


_USER = _descriptor.Descriptor(
  name='User',
  full_name='snapshot.User',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='Phone', full_name='snapshot.User.Phone', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='SessionName', full_name='snapshot.User.SessionName', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='GetFullChannelCounter', full_name='snapshot.User.GetFullChannelCounter', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=418,
  serialized_end=491,
)

_CONFIGURATIONCONTAINER.fields_by_name['SessionStore'].message_type = _SESSIONSETTINGS
_CONFIGURATIONCONTAINER.fields_by_name['CollectorParams'].message_type = _COLLECTOR
_CONFIGURATIONCONTAINER.fields_by_name['UserParams'].message_type = _USER
DESCRIPTOR.message_types_by_name['ConfigurationContainer'] = _CONFIGURATIONCONTAINER
DESCRIPTOR.message_types_by_name['SessionSettings'] = _SESSIONSETTINGS
DESCRIPTOR.message_types_by_name['Collector'] = _COLLECTOR
DESCRIPTOR.message_types_by_name['User'] = _USER
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ConfigurationContainer = _reflection.GeneratedProtocolMessageType('ConfigurationContainer', (_message.Message,), {
  'DESCRIPTOR' : _CONFIGURATIONCONTAINER,
  '__module__' : 'Configurator_pb2'
  # @@protoc_insertion_point(class_scope:snapshot.ConfigurationContainer)
  })
_sym_db.RegisterMessage(ConfigurationContainer)

SessionSettings = _reflection.GeneratedProtocolMessageType('SessionSettings', (_message.Message,), {
  'DESCRIPTOR' : _SESSIONSETTINGS,
  '__module__' : 'Configurator_pb2'
  # @@protoc_insertion_point(class_scope:snapshot.SessionSettings)
  })
_sym_db.RegisterMessage(SessionSettings)

Collector = _reflection.GeneratedProtocolMessageType('Collector', (_message.Message,), {
  'DESCRIPTOR' : _COLLECTOR,
  '__module__' : 'Configurator_pb2'
  # @@protoc_insertion_point(class_scope:snapshot.Collector)
  })
_sym_db.RegisterMessage(Collector)

User = _reflection.GeneratedProtocolMessageType('User', (_message.Message,), {
  'DESCRIPTOR' : _USER,
  '__module__' : 'Configurator_pb2'
  # @@protoc_insertion_point(class_scope:snapshot.User)
  })
_sym_db.RegisterMessage(User)


DESCRIPTOR._options = None

_CONFIGURATOR = _descriptor.ServiceDescriptor(
  name='Configurator',
  full_name='snapshot.Configurator',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=493,
  serialized_end=587,
  methods=[
  _descriptor.MethodDescriptor(
    name='GetConfiguration',
    full_name='snapshot.Configurator.GetConfiguration',
    index=0,
    containing_service=None,
    input_type=google_dot_protobuf_dot_empty__pb2._EMPTY,
    output_type=_CONFIGURATIONCONTAINER,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_CONFIGURATOR)

DESCRIPTOR.services_by_name['Configurator'] = _CONFIGURATOR

# @@protoc_insertion_point(module_scope)
