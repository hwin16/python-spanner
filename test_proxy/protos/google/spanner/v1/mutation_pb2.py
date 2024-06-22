# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/spanner/v1/mutation.proto
# Protobuf Python Version: 4.25.3
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2
from google.spanner.v1 import keys_pb2 as google_dot_spanner_dot_v1_dot_keys__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n google/spanner/v1/mutation.proto\x12\x11google.spanner.v1\x1a\x1fgoogle/api/field_behavior.proto\x1a\x1cgoogle/protobuf/struct.proto\x1a\x1cgoogle/spanner/v1/keys.proto\"\xd5\x03\n\x08Mutation\x12\x33\n\x06insert\x18\x01 \x01(\x0b\x32!.google.spanner.v1.Mutation.WriteH\x00\x12\x33\n\x06update\x18\x02 \x01(\x0b\x32!.google.spanner.v1.Mutation.WriteH\x00\x12=\n\x10insert_or_update\x18\x03 \x01(\x0b\x32!.google.spanner.v1.Mutation.WriteH\x00\x12\x34\n\x07replace\x18\x04 \x01(\x0b\x32!.google.spanner.v1.Mutation.WriteH\x00\x12\x34\n\x06\x64\x65lete\x18\x05 \x01(\x0b\x32\".google.spanner.v1.Mutation.DeleteH\x00\x1aX\n\x05Write\x12\x12\n\x05table\x18\x01 \x01(\tB\x03\xe0\x41\x02\x12\x0f\n\x07\x63olumns\x18\x02 \x03(\t\x12*\n\x06values\x18\x03 \x03(\x0b\x32\x1a.google.protobuf.ListValue\x1aM\n\x06\x44\x65lete\x12\x12\n\x05table\x18\x01 \x01(\tB\x03\xe0\x41\x02\x12/\n\x07key_set\x18\x02 \x01(\x0b\x32\x19.google.spanner.v1.KeySetB\x03\xe0\x41\x02\x42\x0b\n\toperationB\xb0\x01\n\x15\x63om.google.spanner.v1B\rMutationProtoP\x01Z5cloud.google.com/go/spanner/apiv1/spannerpb;spannerpb\xaa\x02\x17Google.Cloud.Spanner.V1\xca\x02\x17Google\\Cloud\\Spanner\\V1\xea\x02\x1aGoogle::Cloud::Spanner::V1b\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.spanner.v1.mutation_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  _globals['DESCRIPTOR']._options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\025com.google.spanner.v1B\rMutationProtoP\001Z5cloud.google.com/go/spanner/apiv1/spannerpb;spannerpb\252\002\027Google.Cloud.Spanner.V1\312\002\027Google\\Cloud\\Spanner\\V1\352\002\032Google::Cloud::Spanner::V1'
  _globals['_MUTATION_WRITE'].fields_by_name['table']._options = None
  _globals['_MUTATION_WRITE'].fields_by_name['table']._serialized_options = b'\340A\002'
  _globals['_MUTATION_DELETE'].fields_by_name['table']._options = None
  _globals['_MUTATION_DELETE'].fields_by_name['table']._serialized_options = b'\340A\002'
  _globals['_MUTATION_DELETE'].fields_by_name['key_set']._options = None
  _globals['_MUTATION_DELETE'].fields_by_name['key_set']._serialized_options = b'\340A\002'
  _globals['_MUTATION']._serialized_start=149
  _globals['_MUTATION']._serialized_end=618
  _globals['_MUTATION_WRITE']._serialized_start=438
  _globals['_MUTATION_WRITE']._serialized_end=526
  _globals['_MUTATION_DELETE']._serialized_start=528
  _globals['_MUTATION_DELETE']._serialized_end=605
# @@protoc_insertion_point(module_scope)
