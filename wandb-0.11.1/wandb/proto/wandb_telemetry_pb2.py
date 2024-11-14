# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: wandb/proto/wandb_telemetry.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='wandb/proto/wandb_telemetry.proto',
  package='wandb_internal',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=b'\n!wandb/proto/wandb_telemetry.proto\x12\x0ewandb_internal\"\xae\x02\n\x0fTelemetryRecord\x12-\n\x0cimports_init\x18\x01 \x01(\x0b\x32\x17.wandb_internal.Imports\x12/\n\x0eimports_finish\x18\x02 \x01(\x0b\x32\x17.wandb_internal.Imports\x12(\n\x07\x66\x65\x61ture\x18\x03 \x01(\x0b\x32\x17.wandb_internal.Feature\x12\x16\n\x0epython_version\x18\x04 \x01(\t\x12\x13\n\x0b\x63li_version\x18\x05 \x01(\t\x12\x1b\n\x13huggingface_version\x18\x06 \x01(\t\x12 \n\x03\x65nv\x18\x08 \x01(\x0b\x32\x13.wandb_internal.Env\x12%\n\x05label\x18\t \x01(\x0b\x32\x16.wandb_internal.Labels\"\xf3\x01\n\x07Imports\x12\r\n\x05torch\x18\x01 \x01(\x08\x12\r\n\x05keras\x18\x02 \x01(\x08\x12\x12\n\ntensorflow\x18\x03 \x01(\x08\x12\x0e\n\x06\x66\x61stai\x18\x04 \x01(\x08\x12\x0f\n\x07sklearn\x18\x05 \x01(\x08\x12\x0f\n\x07xgboost\x18\x06 \x01(\x08\x12\x10\n\x08\x63\x61tboost\x18\x07 \x01(\x08\x12\x10\n\x08lightgbm\x18\x08 \x01(\x08\x12\x19\n\x11pytorch_lightning\x18\t \x01(\x08\x12\x16\n\x0epytorch_ignite\x18\n \x01(\x08\x12 \n\x18transformers_huggingface\x18\x0b \x01(\x08\x12\x0b\n\x03jax\x18\x0c \x01(\x08\"\xb6\x01\n\x07\x46\x65\x61ture\x12\r\n\x05watch\x18\x01 \x01(\x08\x12\x0e\n\x06\x66inish\x18\x02 \x01(\x08\x12\x0c\n\x04save\x18\x03 \x01(\x08\x12\x0f\n\x07offline\x18\x04 \x01(\x08\x12\x0f\n\x07resumed\x18\x05 \x01(\x08\x12\x0c\n\x04grpc\x18\x06 \x01(\x08\x12\x0e\n\x06metric\x18\x07 \x01(\x08\x12\r\n\x05keras\x18\x08 \x01(\x08\x12\x11\n\tsagemaker\x18\t \x01(\x08\x12\x1c\n\x14\x61rtifact_incremental\x18\n \x01(\x08\"\xa0\x01\n\x03\x45nv\x12\x0f\n\x07jupyter\x18\x01 \x01(\x08\x12\x0e\n\x06kaggle\x18\x02 \x01(\x08\x12\x0f\n\x07windows\x18\x03 \x01(\x08\x12\x0e\n\x06m1_gpu\x18\x04 \x01(\x08\x12\x13\n\x0bstart_spawn\x18\x05 \x01(\x08\x12\x12\n\nstart_fork\x18\x06 \x01(\x08\x12\x18\n\x10start_forkserver\x18\x07 \x01(\x08\x12\x14\n\x0cstart_thread\x18\x08 \x01(\x08\"H\n\x06Labels\x12\x13\n\x0b\x63ode_string\x18\x01 \x01(\t\x12\x13\n\x0brepo_string\x18\x02 \x01(\t\x12\x14\n\x0c\x63ode_version\x18\x03 \x01(\tb\x06proto3'
)




_TELEMETRYRECORD = _descriptor.Descriptor(
  name='TelemetryRecord',
  full_name='wandb_internal.TelemetryRecord',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='imports_init', full_name='wandb_internal.TelemetryRecord.imports_init', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='imports_finish', full_name='wandb_internal.TelemetryRecord.imports_finish', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='feature', full_name='wandb_internal.TelemetryRecord.feature', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='python_version', full_name='wandb_internal.TelemetryRecord.python_version', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='cli_version', full_name='wandb_internal.TelemetryRecord.cli_version', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='huggingface_version', full_name='wandb_internal.TelemetryRecord.huggingface_version', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='env', full_name='wandb_internal.TelemetryRecord.env', index=6,
      number=8, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='label', full_name='wandb_internal.TelemetryRecord.label', index=7,
      number=9, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=54,
  serialized_end=356,
)


_IMPORTS = _descriptor.Descriptor(
  name='Imports',
  full_name='wandb_internal.Imports',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='torch', full_name='wandb_internal.Imports.torch', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='keras', full_name='wandb_internal.Imports.keras', index=1,
      number=2, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='tensorflow', full_name='wandb_internal.Imports.tensorflow', index=2,
      number=3, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='fastai', full_name='wandb_internal.Imports.fastai', index=3,
      number=4, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='sklearn', full_name='wandb_internal.Imports.sklearn', index=4,
      number=5, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='xgboost', full_name='wandb_internal.Imports.xgboost', index=5,
      number=6, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='catboost', full_name='wandb_internal.Imports.catboost', index=6,
      number=7, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='lightgbm', full_name='wandb_internal.Imports.lightgbm', index=7,
      number=8, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='pytorch_lightning', full_name='wandb_internal.Imports.pytorch_lightning', index=8,
      number=9, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='pytorch_ignite', full_name='wandb_internal.Imports.pytorch_ignite', index=9,
      number=10, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='transformers_huggingface', full_name='wandb_internal.Imports.transformers_huggingface', index=10,
      number=11, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='jax', full_name='wandb_internal.Imports.jax', index=11,
      number=12, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=359,
  serialized_end=602,
)


_FEATURE = _descriptor.Descriptor(
  name='Feature',
  full_name='wandb_internal.Feature',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='watch', full_name='wandb_internal.Feature.watch', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='finish', full_name='wandb_internal.Feature.finish', index=1,
      number=2, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='save', full_name='wandb_internal.Feature.save', index=2,
      number=3, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='offline', full_name='wandb_internal.Feature.offline', index=3,
      number=4, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='resumed', full_name='wandb_internal.Feature.resumed', index=4,
      number=5, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='grpc', full_name='wandb_internal.Feature.grpc', index=5,
      number=6, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='metric', full_name='wandb_internal.Feature.metric', index=6,
      number=7, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='keras', full_name='wandb_internal.Feature.keras', index=7,
      number=8, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='sagemaker', full_name='wandb_internal.Feature.sagemaker', index=8,
      number=9, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='artifact_incremental', full_name='wandb_internal.Feature.artifact_incremental', index=9,
      number=10, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=605,
  serialized_end=787,
)


_ENV = _descriptor.Descriptor(
  name='Env',
  full_name='wandb_internal.Env',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='jupyter', full_name='wandb_internal.Env.jupyter', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='kaggle', full_name='wandb_internal.Env.kaggle', index=1,
      number=2, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='windows', full_name='wandb_internal.Env.windows', index=2,
      number=3, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='m1_gpu', full_name='wandb_internal.Env.m1_gpu', index=3,
      number=4, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='start_spawn', full_name='wandb_internal.Env.start_spawn', index=4,
      number=5, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='start_fork', full_name='wandb_internal.Env.start_fork', index=5,
      number=6, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='start_forkserver', full_name='wandb_internal.Env.start_forkserver', index=6,
      number=7, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='start_thread', full_name='wandb_internal.Env.start_thread', index=7,
      number=8, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=790,
  serialized_end=950,
)


_LABELS = _descriptor.Descriptor(
  name='Labels',
  full_name='wandb_internal.Labels',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='code_string', full_name='wandb_internal.Labels.code_string', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='repo_string', full_name='wandb_internal.Labels.repo_string', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='code_version', full_name='wandb_internal.Labels.code_version', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=952,
  serialized_end=1024,
)

_TELEMETRYRECORD.fields_by_name['imports_init'].message_type = _IMPORTS
_TELEMETRYRECORD.fields_by_name['imports_finish'].message_type = _IMPORTS
_TELEMETRYRECORD.fields_by_name['feature'].message_type = _FEATURE
_TELEMETRYRECORD.fields_by_name['env'].message_type = _ENV
_TELEMETRYRECORD.fields_by_name['label'].message_type = _LABELS
DESCRIPTOR.message_types_by_name['TelemetryRecord'] = _TELEMETRYRECORD
DESCRIPTOR.message_types_by_name['Imports'] = _IMPORTS
DESCRIPTOR.message_types_by_name['Feature'] = _FEATURE
DESCRIPTOR.message_types_by_name['Env'] = _ENV
DESCRIPTOR.message_types_by_name['Labels'] = _LABELS
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

TelemetryRecord = _reflection.GeneratedProtocolMessageType('TelemetryRecord', (_message.Message,), {
  'DESCRIPTOR' : _TELEMETRYRECORD,
  '__module__' : 'wandb.proto.wandb_telemetry_pb2'
  # @@protoc_insertion_point(class_scope:wandb_internal.TelemetryRecord)
  })
_sym_db.RegisterMessage(TelemetryRecord)

Imports = _reflection.GeneratedProtocolMessageType('Imports', (_message.Message,), {
  'DESCRIPTOR' : _IMPORTS,
  '__module__' : 'wandb.proto.wandb_telemetry_pb2'
  # @@protoc_insertion_point(class_scope:wandb_internal.Imports)
  })
_sym_db.RegisterMessage(Imports)

Feature = _reflection.GeneratedProtocolMessageType('Feature', (_message.Message,), {
  'DESCRIPTOR' : _FEATURE,
  '__module__' : 'wandb.proto.wandb_telemetry_pb2'
  # @@protoc_insertion_point(class_scope:wandb_internal.Feature)
  })
_sym_db.RegisterMessage(Feature)

Env = _reflection.GeneratedProtocolMessageType('Env', (_message.Message,), {
  'DESCRIPTOR' : _ENV,
  '__module__' : 'wandb.proto.wandb_telemetry_pb2'
  # @@protoc_insertion_point(class_scope:wandb_internal.Env)
  })
_sym_db.RegisterMessage(Env)

Labels = _reflection.GeneratedProtocolMessageType('Labels', (_message.Message,), {
  'DESCRIPTOR' : _LABELS,
  '__module__' : 'wandb.proto.wandb_telemetry_pb2'
  # @@protoc_insertion_point(class_scope:wandb_internal.Labels)
  })
_sym_db.RegisterMessage(Labels)


# @@protoc_insertion_point(module_scope)