# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/spanner/admin/instance/v1/common.proto
# Protobuf Python Version: 4.25.3
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n-google/spanner/admin/instance/v1/common.proto\x12 google.spanner.admin.instance.v1\x1a\x1fgoogle/protobuf/timestamp.proto\"\x8b\x01\n\x11OperationProgress\x12\x18\n\x10progress_percent\x18\x01 \x01(\x05\x12.\n\nstart_time\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12,\n\x08\x65nd_time\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.Timestamp*w\n\x11\x46ulfillmentPeriod\x12\"\n\x1e\x46ULFILLMENT_PERIOD_UNSPECIFIED\x10\x00\x12\x1d\n\x19\x46ULFILLMENT_PERIOD_NORMAL\x10\x01\x12\x1f\n\x1b\x46ULFILLMENT_PERIOD_EXTENDED\x10\x02\x42\xfd\x01\n$com.google.spanner.admin.instance.v1B\x0b\x43ommonProtoP\x01ZFcloud.google.com/go/spanner/admin/instance/apiv1/instancepb;instancepb\xaa\x02&Google.Cloud.Spanner.Admin.Instance.V1\xca\x02&Google\\Cloud\\Spanner\\Admin\\Instance\\V1\xea\x02+Google::Cloud::Spanner::Admin::Instance::V1b\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.spanner.admin.instance.v1.common_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  _globals['DESCRIPTOR']._options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n$com.google.spanner.admin.instance.v1B\013CommonProtoP\001ZFcloud.google.com/go/spanner/admin/instance/apiv1/instancepb;instancepb\252\002&Google.Cloud.Spanner.Admin.Instance.V1\312\002&Google\\Cloud\\Spanner\\Admin\\Instance\\V1\352\002+Google::Cloud::Spanner::Admin::Instance::V1'
  _globals['_FULFILLMENTPERIOD']._serialized_start=258
  _globals['_FULFILLMENTPERIOD']._serialized_end=377
  _globals['_OPERATIONPROGRESS']._serialized_start=117
  _globals['_OPERATIONPROGRESS']._serialized_end=256
# @@protoc_insertion_point(module_scope)
