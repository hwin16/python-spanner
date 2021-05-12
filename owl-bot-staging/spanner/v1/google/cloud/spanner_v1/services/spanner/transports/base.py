# -*- coding: utf-8 -*-
# Copyright 2020 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import abc
from typing import Awaitable, Callable, Dict, Optional, Sequence, Union
import packaging.version
import pkg_resources

import google.auth  # type: ignore
import google.api_core  # type: ignore
from google.api_core import exceptions as core_exceptions  # type: ignore
from google.api_core import gapic_v1    # type: ignore
from google.api_core import retry as retries  # type: ignore
from google.auth import credentials as ga_credentials  # type: ignore

from google.cloud.spanner_v1.types import commit_response
from google.cloud.spanner_v1.types import result_set
from google.cloud.spanner_v1.types import spanner
from google.cloud.spanner_v1.types import transaction
from google.protobuf import empty_pb2  # type: ignore

try:
    DEFAULT_CLIENT_INFO = gapic_v1.client_info.ClientInfo(
        gapic_version=pkg_resources.get_distribution(
            'google-cloud-spanner',
        ).version,
    )
except pkg_resources.DistributionNotFound:
    DEFAULT_CLIENT_INFO = gapic_v1.client_info.ClientInfo()

try:
    # google.auth.__version__ was added in 1.26.0
    _GOOGLE_AUTH_VERSION = google.auth.__version__
except AttributeError:
    try:  # try pkg_resources if it is available
        _GOOGLE_AUTH_VERSION = pkg_resources.get_distribution("google-auth").version
    except pkg_resources.DistributionNotFound:  # pragma: NO COVER
        _GOOGLE_AUTH_VERSION = None

_API_CORE_VERSION = google.api_core.__version__


class SpannerTransport(abc.ABC):
    """Abstract transport class for Spanner."""

    AUTH_SCOPES = (
        'https://www.googleapis.com/auth/cloud-platform',
        'https://www.googleapis.com/auth/spanner.data',
    )

    DEFAULT_HOST: str = 'spanner.googleapis.com'
    def __init__(
            self, *,
            host: str = DEFAULT_HOST,
            credentials: ga_credentials.Credentials = None,
            credentials_file: Optional[str] = None,
            scopes: Optional[Sequence[str]] = None,
            quota_project_id: Optional[str] = None,
            client_info: gapic_v1.client_info.ClientInfo = DEFAULT_CLIENT_INFO,
            **kwargs,
            ) -> None:
        """Instantiate the transport.

        Args:
            host (Optional[str]):
                 The hostname to connect to.
            credentials (Optional[google.auth.credentials.Credentials]): The
                authorization credentials to attach to requests. These
                credentials identify the application to the service; if none
                are specified, the client will attempt to ascertain the
                credentials from the environment.
            credentials_file (Optional[str]): A file with credentials that can
                be loaded with :func:`google.auth.load_credentials_from_file`.
                This argument is mutually exclusive with credentials.
            scopes (Optional[Sequence[str]]): A list of scopes.
            quota_project_id (Optional[str]): An optional project to use for billing
                and quota.
            client_info (google.api_core.gapic_v1.client_info.ClientInfo):
                The client info used to send a user-agent string along with
                API requests. If ``None``, then default info will be used.
                Generally, you only need to set this if you're developing
                your own client library.
        """
        # Save the hostname. Default to port 443 (HTTPS) if none is specified.
        if ':' not in host:
            host += ':443'
        self._host = host

        scopes_kwargs = self._get_scopes_kwargs(self._host, scopes)

        # Save the scopes.
        self._scopes = scopes or self.AUTH_SCOPES

        # If no credentials are provided, then determine the appropriate
        # defaults.
        if credentials and credentials_file:
            raise core_exceptions.DuplicateCredentialArgs("'credentials_file' and 'credentials' are mutually exclusive")

        if credentials_file is not None:
            credentials, _ = google.auth.load_credentials_from_file(
                                credentials_file,
                                **scopes_kwargs,
                                quota_project_id=quota_project_id
                            )

        elif credentials is None:
            credentials, _ = google.auth.default(**scopes_kwargs, quota_project_id=quota_project_id)

        # Save the credentials.
        self._credentials = credentials

    # TODO(busunkim): These two class methods are in the base transport
    # to avoid duplicating code across the transport classes. These functions
    # should be deleted once the minimum required versions of google-api-core
    # and google-auth are increased.

    # TODO: Remove this function once google-auth >= 1.25.0 is required
    @classmethod
    def _get_scopes_kwargs(cls, host: str, scopes: Optional[Sequence[str]]) -> Dict[str, Optional[Sequence[str]]]:
        """Returns scopes kwargs to pass to google-auth methods depending on the google-auth version"""

        scopes_kwargs = {}

        if _GOOGLE_AUTH_VERSION and (
            packaging.version.parse(_GOOGLE_AUTH_VERSION)
            >= packaging.version.parse("1.25.0")
        ):
            scopes_kwargs = {"scopes": scopes, "default_scopes": cls.AUTH_SCOPES}
        else:
            scopes_kwargs = {"scopes": scopes or cls.AUTH_SCOPES}

        return scopes_kwargs

    # TODO: Remove this function once google-api-core >= 1.26.0 is required
    @classmethod
    def _get_self_signed_jwt_kwargs(cls, host: str, scopes: Optional[Sequence[str]]) -> Dict[str, Union[Optional[Sequence[str]], str]]:
        """Returns kwargs to pass to grpc_helpers.create_channel depending on the google-api-core version"""

        self_signed_jwt_kwargs: Dict[str, Union[Optional[Sequence[str]], str]] = {}

        if _API_CORE_VERSION and (
            packaging.version.parse(_API_CORE_VERSION)
            >= packaging.version.parse("1.26.0")
        ):
            self_signed_jwt_kwargs["default_scopes"] = cls.AUTH_SCOPES
            self_signed_jwt_kwargs["scopes"] = scopes
            self_signed_jwt_kwargs["default_host"] = cls.DEFAULT_HOST
        else:
            self_signed_jwt_kwargs["scopes"] = scopes or cls.AUTH_SCOPES

        return self_signed_jwt_kwargs

    def _prep_wrapped_messages(self, client_info):
        # Precompute the wrapped methods.
        self._wrapped_methods = {
            self.create_session: gapic_v1.method.wrap_method(
                self.create_session,
                default_retry=retries.Retry(
initial=0.25,maximum=32.0,multiplier=1.3,                    predicate=retries.if_exception_type(
                        core_exceptions.ServiceUnavailable,
                    ),
                    deadline=30.0,
                ),
                default_timeout=30.0,
                client_info=client_info,
            ),
            self.batch_create_sessions: gapic_v1.method.wrap_method(
                self.batch_create_sessions,
                default_retry=retries.Retry(
initial=0.25,maximum=32.0,multiplier=1.3,                    predicate=retries.if_exception_type(
                        core_exceptions.ServiceUnavailable,
                    ),
                    deadline=60.0,
                ),
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.get_session: gapic_v1.method.wrap_method(
                self.get_session,
                default_retry=retries.Retry(
initial=0.25,maximum=32.0,multiplier=1.3,                    predicate=retries.if_exception_type(
                        core_exceptions.ServiceUnavailable,
                    ),
                    deadline=30.0,
                ),
                default_timeout=30.0,
                client_info=client_info,
            ),
            self.list_sessions: gapic_v1.method.wrap_method(
                self.list_sessions,
                default_retry=retries.Retry(
initial=0.25,maximum=32.0,multiplier=1.3,                    predicate=retries.if_exception_type(
                        core_exceptions.ServiceUnavailable,
                    ),
                    deadline=3600.0,
                ),
                default_timeout=3600.0,
                client_info=client_info,
            ),
            self.delete_session: gapic_v1.method.wrap_method(
                self.delete_session,
                default_retry=retries.Retry(
initial=0.25,maximum=32.0,multiplier=1.3,                    predicate=retries.if_exception_type(
                        core_exceptions.ServiceUnavailable,
                    ),
                    deadline=30.0,
                ),
                default_timeout=30.0,
                client_info=client_info,
            ),
            self.execute_sql: gapic_v1.method.wrap_method(
                self.execute_sql,
                default_retry=retries.Retry(
initial=0.25,maximum=32.0,multiplier=1.3,                    predicate=retries.if_exception_type(
                        core_exceptions.ServiceUnavailable,
                    ),
                    deadline=30.0,
                ),
                default_timeout=30.0,
                client_info=client_info,
            ),
            self.execute_streaming_sql: gapic_v1.method.wrap_method(
                self.execute_streaming_sql,
                default_timeout=3600.0,
                client_info=client_info,
            ),
            self.execute_batch_dml: gapic_v1.method.wrap_method(
                self.execute_batch_dml,
                default_retry=retries.Retry(
initial=0.25,maximum=32.0,multiplier=1.3,                    predicate=retries.if_exception_type(
                        core_exceptions.ServiceUnavailable,
                    ),
                    deadline=30.0,
                ),
                default_timeout=30.0,
                client_info=client_info,
            ),
            self.read: gapic_v1.method.wrap_method(
                self.read,
                default_retry=retries.Retry(
initial=0.25,maximum=32.0,multiplier=1.3,                    predicate=retries.if_exception_type(
                        core_exceptions.ServiceUnavailable,
                    ),
                    deadline=30.0,
                ),
                default_timeout=30.0,
                client_info=client_info,
            ),
            self.streaming_read: gapic_v1.method.wrap_method(
                self.streaming_read,
                default_timeout=3600.0,
                client_info=client_info,
            ),
            self.begin_transaction: gapic_v1.method.wrap_method(
                self.begin_transaction,
                default_retry=retries.Retry(
initial=0.25,maximum=32.0,multiplier=1.3,                    predicate=retries.if_exception_type(
                        core_exceptions.ServiceUnavailable,
                    ),
                    deadline=30.0,
                ),
                default_timeout=30.0,
                client_info=client_info,
            ),
            self.commit: gapic_v1.method.wrap_method(
                self.commit,
                default_retry=retries.Retry(
initial=0.25,maximum=32.0,multiplier=1.3,                    predicate=retries.if_exception_type(
                        core_exceptions.ServiceUnavailable,
                    ),
                    deadline=3600.0,
                ),
                default_timeout=3600.0,
                client_info=client_info,
            ),
            self.rollback: gapic_v1.method.wrap_method(
                self.rollback,
                default_retry=retries.Retry(
initial=0.25,maximum=32.0,multiplier=1.3,                    predicate=retries.if_exception_type(
                        core_exceptions.ServiceUnavailable,
                    ),
                    deadline=30.0,
                ),
                default_timeout=30.0,
                client_info=client_info,
            ),
            self.partition_query: gapic_v1.method.wrap_method(
                self.partition_query,
                default_retry=retries.Retry(
initial=0.25,maximum=32.0,multiplier=1.3,                    predicate=retries.if_exception_type(
                        core_exceptions.ServiceUnavailable,
                    ),
                    deadline=30.0,
                ),
                default_timeout=30.0,
                client_info=client_info,
            ),
            self.partition_read: gapic_v1.method.wrap_method(
                self.partition_read,
                default_retry=retries.Retry(
initial=0.25,maximum=32.0,multiplier=1.3,                    predicate=retries.if_exception_type(
                        core_exceptions.ServiceUnavailable,
                    ),
                    deadline=30.0,
                ),
                default_timeout=30.0,
                client_info=client_info,
            ),
         }

    @property
    def create_session(self) -> Callable[
            [spanner.CreateSessionRequest],
            Union[
                spanner.Session,
                Awaitable[spanner.Session]
            ]]:
        raise NotImplementedError()

    @property
    def batch_create_sessions(self) -> Callable[
            [spanner.BatchCreateSessionsRequest],
            Union[
                spanner.BatchCreateSessionsResponse,
                Awaitable[spanner.BatchCreateSessionsResponse]
            ]]:
        raise NotImplementedError()

    @property
    def get_session(self) -> Callable[
            [spanner.GetSessionRequest],
            Union[
                spanner.Session,
                Awaitable[spanner.Session]
            ]]:
        raise NotImplementedError()

    @property
    def list_sessions(self) -> Callable[
            [spanner.ListSessionsRequest],
            Union[
                spanner.ListSessionsResponse,
                Awaitable[spanner.ListSessionsResponse]
            ]]:
        raise NotImplementedError()

    @property
    def delete_session(self) -> Callable[
            [spanner.DeleteSessionRequest],
            Union[
                empty_pb2.Empty,
                Awaitable[empty_pb2.Empty]
            ]]:
        raise NotImplementedError()

    @property
    def execute_sql(self) -> Callable[
            [spanner.ExecuteSqlRequest],
            Union[
                result_set.ResultSet,
                Awaitable[result_set.ResultSet]
            ]]:
        raise NotImplementedError()

    @property
    def execute_streaming_sql(self) -> Callable[
            [spanner.ExecuteSqlRequest],
            Union[
                result_set.PartialResultSet,
                Awaitable[result_set.PartialResultSet]
            ]]:
        raise NotImplementedError()

    @property
    def execute_batch_dml(self) -> Callable[
            [spanner.ExecuteBatchDmlRequest],
            Union[
                spanner.ExecuteBatchDmlResponse,
                Awaitable[spanner.ExecuteBatchDmlResponse]
            ]]:
        raise NotImplementedError()

    @property
    def read(self) -> Callable[
            [spanner.ReadRequest],
            Union[
                result_set.ResultSet,
                Awaitable[result_set.ResultSet]
            ]]:
        raise NotImplementedError()

    @property
    def streaming_read(self) -> Callable[
            [spanner.ReadRequest],
            Union[
                result_set.PartialResultSet,
                Awaitable[result_set.PartialResultSet]
            ]]:
        raise NotImplementedError()

    @property
    def begin_transaction(self) -> Callable[
            [spanner.BeginTransactionRequest],
            Union[
                transaction.Transaction,
                Awaitable[transaction.Transaction]
            ]]:
        raise NotImplementedError()

    @property
    def commit(self) -> Callable[
            [spanner.CommitRequest],
            Union[
                commit_response.CommitResponse,
                Awaitable[commit_response.CommitResponse]
            ]]:
        raise NotImplementedError()

    @property
    def rollback(self) -> Callable[
            [spanner.RollbackRequest],
            Union[
                empty_pb2.Empty,
                Awaitable[empty_pb2.Empty]
            ]]:
        raise NotImplementedError()

    @property
    def partition_query(self) -> Callable[
            [spanner.PartitionQueryRequest],
            Union[
                spanner.PartitionResponse,
                Awaitable[spanner.PartitionResponse]
            ]]:
        raise NotImplementedError()

    @property
    def partition_read(self) -> Callable[
            [spanner.PartitionReadRequest],
            Union[
                spanner.PartitionResponse,
                Awaitable[spanner.PartitionResponse]
            ]]:
        raise NotImplementedError()


__all__ = (
    'SpannerTransport',
)
