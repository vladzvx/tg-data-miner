# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: OrderBoard.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='OrderBoard.proto',
  package='orders',
  syntax='proto3',
  serialized_options=b'\252\002\006Common',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x10OrderBoard.proto\x12\x06orders\x1a\x1bgoogle/protobuf/empty.proto\x1a\x1fgoogle/protobuf/timestamp.proto\"\xb1\x01\n\x0bStateReport\x12\x10\n\x08Messages\x18\x01 \x01(\x05\x12\x10\n\x08\x45ntities\x18\x02 \x01(\x05\x12\x0e\n\x06Orders\x18\x03 \x01(\x05\x12\x18\n\x10SessionsStorages\x18\x04 \x01(\x05\x12\x12\n\nCollectors\x18\x05 \x01(\x05\x12\r\n\x05Users\x18\x06 \x01(\x05\x12\x0b\n\x03\x43PU\x18\x07 \x01(\x01\x12\x10\n\x08\x46reeDisk\x18\x08 \x01(\x03\x12\x12\n\nMemoryUsed\x18\t \x01(\x03\"\x1d\n\x0b\x43heckResult\x12\x0e\n\x06Result\x18\x01 \x01(\x08\"\x99\x01\n\x06\x45ntity\x12\n\n\x02Id\x18\x01 \x01(\x03\x12\x0e\n\x06PairId\x18\x02 \x01(\x03\x12\x0c\n\x04Link\x18\x03 \x01(\t\x12\x10\n\x08PairLink\x18\x04 \x01(\t\x12\x11\n\tFirstName\x18\x05 \x01(\t\x12\x10\n\x08LastName\x18\x06 \x01(\t\x12\x0c\n\x04\x44\x65sc\x18\x07 \x01(\t\x12 \n\x04Type\x18\x08 \x01(\x0e\x32\x12.orders.EntityType\"\xb2\x02\n\x07Message\x12-\n\tTimestamp\x18\x01 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x0c\n\x04Text\x18\x02 \x01(\t\x12\r\n\x05Media\x18\x03 \x01(\t\x12\n\n\x02Id\x18\x04 \x01(\x03\x12\x0e\n\x06\x46romId\x18\x05 \x01(\x03\x12\x15\n\rForwardFromId\x18\x06 \x01(\x03\x12\x1c\n\x14\x46orwardFromMessageId\x18\x07 \x01(\x03\x12\x0e\n\x06\x43hatId\x18\x08 \x01(\x03\x12\x14\n\x0cMediagroupId\x18\t \x01(\x03\x12\x0f\n\x07ReplyTo\x18\n \x01(\x03\x12\x13\n\x0bThreadStart\x18\x0b \x01(\x03\x12\x18\n\x10\x46romExistingUser\x18\x0c \x01(\x08\x12$\n\tFormating\x18\r \x03(\x0b\x32\x11.orders.Formating\"a\n\tFormating\x12#\n\x04Type\x18\x01 \x01(\x0e\x32\x15.orders.FormatingType\x12\x0e\n\x06Length\x18\x02 \x01(\x05\x12\x0e\n\x06Offset\x18\x03 \x01(\x05\x12\x0f\n\x07\x43ontent\x18\x04 \x01(\t\"\x9e\x01\n\x05Order\x12\x0f\n\x07OrderId\x18\x01 \x01(\x03\x12\n\n\x02Id\x18\x02 \x01(\x03\x12\x0e\n\x06PairId\x18\x03 \x01(\x03\x12\x0e\n\x06Offset\x18\x04 \x01(\x03\x12\x0c\n\x04Link\x18\x05 \x01(\t\x12\x10\n\x08PairLink\x18\x06 \x01(\t\x12\x1f\n\x04Type\x18\x07 \x01(\x0e\x32\x11.orders.OrderType\x12\x17\n\x0fRedirectCounter\x18\x08 \x01(\x05*.\n\nEntityType\x12\x08\n\x04User\x10\x00\x12\x0b\n\x07\x43hannel\x10\x01\x12\t\n\x05Group\x10\x02*r\n\rFormatingType\x12\x08\n\x04\x42old\x10\x00\x12\n\n\x06Strike\x10\x01\x12\n\n\x06Italic\x10\x02\x12\r\n\tUnderline\x10\x03\x12\x08\n\x04\x43ode\x10\x04\x12\x07\n\x03Pre\x10\x05\x12\x0f\n\x0bTextMention\x10\x06\x12\x0c\n\x08TextLink\x10\x07*7\n\tOrderType\x12\t\n\x05\x45mpty\x10\x00\x12\x0b\n\x07History\x10\x01\x12\x12\n\x0eGetFullChannel\x10\x02\x32\xd3\x02\n\nOrderBoard\x12\x31\n\x08GetOrder\x12\x16.google.protobuf.Empty\x1a\r.orders.Order\x12\x32\n\tPostOrder\x12\r.orders.Order\x1a\x16.google.protobuf.Empty\x12\x34\n\nPostEntity\x12\x0e.orders.Entity\x1a\x16.google.protobuf.Empty\x12\x32\n\x0b\x43heckEntity\x12\x0e.orders.Entity\x1a\x13.orders.CheckResult\x12;\n\x0eStreamMessages\x12\x0f.orders.Message\x1a\x16.google.protobuf.Empty(\x01\x12\x37\n\x08GetState\x12\x16.google.protobuf.Empty\x1a\x13.orders.StateReportB\t\xaa\x02\x06\x43ommonb\x06proto3'
  ,
  dependencies=[google_dot_protobuf_dot_empty__pb2.DESCRIPTOR,google_dot_protobuf_dot_timestamp__pb2.DESCRIPTOR,])

_ENTITYTYPE = _descriptor.EnumDescriptor(
  name='EntityType',
  full_name='orders.EntityType',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='User', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='Channel', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='Group', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=1026,
  serialized_end=1072,
)
_sym_db.RegisterEnumDescriptor(_ENTITYTYPE)

EntityType = enum_type_wrapper.EnumTypeWrapper(_ENTITYTYPE)
_FORMATINGTYPE = _descriptor.EnumDescriptor(
  name='FormatingType',
  full_name='orders.FormatingType',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='Bold', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='Strike', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='Italic', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='Underline', index=3, number=3,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='Code', index=4, number=4,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='Pre', index=5, number=5,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='TextMention', index=6, number=6,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='TextLink', index=7, number=7,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=1074,
  serialized_end=1188,
)
_sym_db.RegisterEnumDescriptor(_FORMATINGTYPE)

FormatingType = enum_type_wrapper.EnumTypeWrapper(_FORMATINGTYPE)
_ORDERTYPE = _descriptor.EnumDescriptor(
  name='OrderType',
  full_name='orders.OrderType',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='Empty', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='History', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='GetFullChannel', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=1190,
  serialized_end=1245,
)
_sym_db.RegisterEnumDescriptor(_ORDERTYPE)

OrderType = enum_type_wrapper.EnumTypeWrapper(_ORDERTYPE)
User = 0
Channel = 1
Group = 2
Bold = 0
Strike = 1
Italic = 2
Underline = 3
Code = 4
Pre = 5
TextMention = 6
TextLink = 7
Empty = 0
History = 1
GetFullChannel = 2



_STATEREPORT = _descriptor.Descriptor(
  name='StateReport',
  full_name='orders.StateReport',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='Messages', full_name='orders.StateReport.Messages', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='Entities', full_name='orders.StateReport.Entities', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='Orders', full_name='orders.StateReport.Orders', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='SessionsStorages', full_name='orders.StateReport.SessionsStorages', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='Collectors', full_name='orders.StateReport.Collectors', index=4,
      number=5, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='Users', full_name='orders.StateReport.Users', index=5,
      number=6, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='CPU', full_name='orders.StateReport.CPU', index=6,
      number=7, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='FreeDisk', full_name='orders.StateReport.FreeDisk', index=7,
      number=8, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='MemoryUsed', full_name='orders.StateReport.MemoryUsed', index=8,
      number=9, type=3, cpp_type=2, label=1,
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
  serialized_start=91,
  serialized_end=268,
)


_CHECKRESULT = _descriptor.Descriptor(
  name='CheckResult',
  full_name='orders.CheckResult',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='Result', full_name='orders.CheckResult.Result', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
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
  serialized_start=270,
  serialized_end=299,
)


_ENTITY = _descriptor.Descriptor(
  name='Entity',
  full_name='orders.Entity',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='Id', full_name='orders.Entity.Id', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='PairId', full_name='orders.Entity.PairId', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='Link', full_name='orders.Entity.Link', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='PairLink', full_name='orders.Entity.PairLink', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='FirstName', full_name='orders.Entity.FirstName', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='LastName', full_name='orders.Entity.LastName', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='Desc', full_name='orders.Entity.Desc', index=6,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='Type', full_name='orders.Entity.Type', index=7,
      number=8, type=14, cpp_type=8, label=1,
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
  serialized_start=302,
  serialized_end=455,
)


_MESSAGE = _descriptor.Descriptor(
  name='Message',
  full_name='orders.Message',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='Timestamp', full_name='orders.Message.Timestamp', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='Text', full_name='orders.Message.Text', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='Media', full_name='orders.Message.Media', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='Id', full_name='orders.Message.Id', index=3,
      number=4, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='FromId', full_name='orders.Message.FromId', index=4,
      number=5, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='ForwardFromId', full_name='orders.Message.ForwardFromId', index=5,
      number=6, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='ForwardFromMessageId', full_name='orders.Message.ForwardFromMessageId', index=6,
      number=7, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='ChatId', full_name='orders.Message.ChatId', index=7,
      number=8, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='MediagroupId', full_name='orders.Message.MediagroupId', index=8,
      number=9, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='ReplyTo', full_name='orders.Message.ReplyTo', index=9,
      number=10, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='ThreadStart', full_name='orders.Message.ThreadStart', index=10,
      number=11, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='FromExistingUser', full_name='orders.Message.FromExistingUser', index=11,
      number=12, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='Formating', full_name='orders.Message.Formating', index=12,
      number=13, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=458,
  serialized_end=764,
)


_FORMATING = _descriptor.Descriptor(
  name='Formating',
  full_name='orders.Formating',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='Type', full_name='orders.Formating.Type', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='Length', full_name='orders.Formating.Length', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='Offset', full_name='orders.Formating.Offset', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='Content', full_name='orders.Formating.Content', index=3,
      number=4, type=9, cpp_type=9, label=1,
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
  serialized_start=766,
  serialized_end=863,
)


_ORDER = _descriptor.Descriptor(
  name='Order',
  full_name='orders.Order',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='OrderId', full_name='orders.Order.OrderId', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='Id', full_name='orders.Order.Id', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='PairId', full_name='orders.Order.PairId', index=2,
      number=3, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='Offset', full_name='orders.Order.Offset', index=3,
      number=4, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='Link', full_name='orders.Order.Link', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='PairLink', full_name='orders.Order.PairLink', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='Type', full_name='orders.Order.Type', index=6,
      number=7, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='RedirectCounter', full_name='orders.Order.RedirectCounter', index=7,
      number=8, type=5, cpp_type=1, label=1,
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
  serialized_start=866,
  serialized_end=1024,
)

_ENTITY.fields_by_name['Type'].enum_type = _ENTITYTYPE
_MESSAGE.fields_by_name['Timestamp'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_MESSAGE.fields_by_name['Formating'].message_type = _FORMATING
_FORMATING.fields_by_name['Type'].enum_type = _FORMATINGTYPE
_ORDER.fields_by_name['Type'].enum_type = _ORDERTYPE
DESCRIPTOR.message_types_by_name['StateReport'] = _STATEREPORT
DESCRIPTOR.message_types_by_name['CheckResult'] = _CHECKRESULT
DESCRIPTOR.message_types_by_name['Entity'] = _ENTITY
DESCRIPTOR.message_types_by_name['Message'] = _MESSAGE
DESCRIPTOR.message_types_by_name['Formating'] = _FORMATING
DESCRIPTOR.message_types_by_name['Order'] = _ORDER
DESCRIPTOR.enum_types_by_name['EntityType'] = _ENTITYTYPE
DESCRIPTOR.enum_types_by_name['FormatingType'] = _FORMATINGTYPE
DESCRIPTOR.enum_types_by_name['OrderType'] = _ORDERTYPE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

StateReport = _reflection.GeneratedProtocolMessageType('StateReport', (_message.Message,), {
  'DESCRIPTOR' : _STATEREPORT,
  '__module__' : 'OrderBoard_pb2'
  # @@protoc_insertion_point(class_scope:orders.StateReport)
  })
_sym_db.RegisterMessage(StateReport)

CheckResult = _reflection.GeneratedProtocolMessageType('CheckResult', (_message.Message,), {
  'DESCRIPTOR' : _CHECKRESULT,
  '__module__' : 'OrderBoard_pb2'
  # @@protoc_insertion_point(class_scope:orders.CheckResult)
  })
_sym_db.RegisterMessage(CheckResult)

Entity = _reflection.GeneratedProtocolMessageType('Entity', (_message.Message,), {
  'DESCRIPTOR' : _ENTITY,
  '__module__' : 'OrderBoard_pb2'
  # @@protoc_insertion_point(class_scope:orders.Entity)
  })
_sym_db.RegisterMessage(Entity)

Message = _reflection.GeneratedProtocolMessageType('Message', (_message.Message,), {
  'DESCRIPTOR' : _MESSAGE,
  '__module__' : 'OrderBoard_pb2'
  # @@protoc_insertion_point(class_scope:orders.Message)
  })
_sym_db.RegisterMessage(Message)

Formating = _reflection.GeneratedProtocolMessageType('Formating', (_message.Message,), {
  'DESCRIPTOR' : _FORMATING,
  '__module__' : 'OrderBoard_pb2'
  # @@protoc_insertion_point(class_scope:orders.Formating)
  })
_sym_db.RegisterMessage(Formating)

Order = _reflection.GeneratedProtocolMessageType('Order', (_message.Message,), {
  'DESCRIPTOR' : _ORDER,
  '__module__' : 'OrderBoard_pb2'
  # @@protoc_insertion_point(class_scope:orders.Order)
  })
_sym_db.RegisterMessage(Order)


DESCRIPTOR._options = None

_ORDERBOARD = _descriptor.ServiceDescriptor(
  name='OrderBoard',
  full_name='orders.OrderBoard',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=1248,
  serialized_end=1587,
  methods=[
  _descriptor.MethodDescriptor(
    name='GetOrder',
    full_name='orders.OrderBoard.GetOrder',
    index=0,
    containing_service=None,
    input_type=google_dot_protobuf_dot_empty__pb2._EMPTY,
    output_type=_ORDER,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='PostOrder',
    full_name='orders.OrderBoard.PostOrder',
    index=1,
    containing_service=None,
    input_type=_ORDER,
    output_type=google_dot_protobuf_dot_empty__pb2._EMPTY,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='PostEntity',
    full_name='orders.OrderBoard.PostEntity',
    index=2,
    containing_service=None,
    input_type=_ENTITY,
    output_type=google_dot_protobuf_dot_empty__pb2._EMPTY,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='CheckEntity',
    full_name='orders.OrderBoard.CheckEntity',
    index=3,
    containing_service=None,
    input_type=_ENTITY,
    output_type=_CHECKRESULT,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='StreamMessages',
    full_name='orders.OrderBoard.StreamMessages',
    index=4,
    containing_service=None,
    input_type=_MESSAGE,
    output_type=google_dot_protobuf_dot_empty__pb2._EMPTY,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='GetState',
    full_name='orders.OrderBoard.GetState',
    index=5,
    containing_service=None,
    input_type=google_dot_protobuf_dot_empty__pb2._EMPTY,
    output_type=_STATEREPORT,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_ORDERBOARD)

DESCRIPTOR.services_by_name['OrderBoard'] = _ORDERBOARD

# @@protoc_insertion_point(module_scope)
