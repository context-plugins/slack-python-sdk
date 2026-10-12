from __future__ import annotations

from uuid import UUID, uuid4

from ..auth import AsyncAuthSchemes, AuthSchemes
from ..core import (
    ApiResult,
    AsyncRawClient,
    RawClient,
    RawError,
    RequestOptionsOrDict,
    SecuredRawResponse,
    async_json_decoder,
    form_body,
    json_decoder,
    param,
    raw_error_response,
    unwrap,
)
from ..models.defaultsuccesstemplate import Defaultsuccesstemplate
from ..models.enums.content_type import ContentTypeOrStr
from ..server.server import Server


class CallsParticipants:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = CallsParticipantsWithRawResponse(client, server, auth)

    def calls_participants_add(
        self,
        token: str,
        content_type: ContentTypeOrStr,
        id_: str,
        users: str,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> Defaultsuccesstemplate:
        """Registers new participants added to a Call.

        Args:
            token: Authentication token. Requires scope: ``calls:write``
            content_type: Value sent with the request.
            id_: ``id`` returned by the /methods/calls.add method.
            users: The list of users to add as participants in the Call. `Read more on how to specify users here
                </apis/calls#users>`__.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Typical success response

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(
            self._with_raw_response.calls_participants_add(
                token, content_type, id_, users, request_options=request_options
            ),
        )

    def calls_participants_remove(
        self,
        token: str,
        content_type: ContentTypeOrStr,
        id_: str,
        users: str,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> Defaultsuccesstemplate:
        """Registers participants removed from a Call.

        Args:
            token: Authentication token. Requires scope: ``calls:write``
            content_type: Value sent with the request.
            id_: ``id`` returned by the /methods/calls.add method.
            users: The list of users to remove as participants in the Call. `Read more on how to specify users here
                </apis/calls#users>`__.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Typical success response

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(
            self._with_raw_response.calls_participants_remove(
                token, content_type, id_, users, request_options=request_options
            ),
        )

    @property
    def with_raw_response(self) -> CallsParticipantsWithRawResponse:
        return self._with_raw_response


class AsyncCallsParticipants:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncCallsParticipantsWithRawResponse(client, server, auth)

    async def calls_participants_add(
        self,
        token: str,
        content_type: ContentTypeOrStr,
        id_: str,
        users: str,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> Defaultsuccesstemplate:
        """Registers new participants added to a Call.

        Args:
            token: Authentication token. Requires scope: ``calls:write``
            content_type: Value sent with the request.
            id_: ``id`` returned by the /methods/calls.add method.
            users: The list of users to add as participants in the Call. `Read more on how to specify users here
                </apis/calls#users>`__.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Typical success response

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(
            await self._with_raw_response.calls_participants_add(
                token, content_type, id_, users, request_options=request_options
            ),
        )

    async def calls_participants_remove(
        self,
        token: str,
        content_type: ContentTypeOrStr,
        id_: str,
        users: str,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> Defaultsuccesstemplate:
        """Registers participants removed from a Call.

        Args:
            token: Authentication token. Requires scope: ``calls:write``
            content_type: Value sent with the request.
            id_: ``id`` returned by the /methods/calls.add method.
            users: The list of users to remove as participants in the Call. `Read more on how to specify users here
                </apis/calls#users>`__.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Typical success response

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(
            await self._with_raw_response.calls_participants_remove(
                token, content_type, id_, users, request_options=request_options
            ),
        )

    @property
    def with_raw_response(self) -> AsyncCallsParticipantsWithRawResponse:
        return self._with_raw_response


class CallsParticipantsWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def calls_participants_add(
        self,
        token: str,
        content_type: ContentTypeOrStr,
        id_: str,
        users: str,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[Defaultsuccesstemplate, RawError]:
        """Registers new participants added to a Call.

        Args:
            token: Authentication token. Requires scope: ``calls:write``
            content_type: Value sent with the request.
            id_: ``id`` returned by the /methods/calls.add method.
            users: The list of users to add as participants in the Call. `Read more on how to specify users here
                </apis/calls#users>`__.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/calls.participants.add"),
            headers=[
                param[str]("token", token),
                param[ContentTypeOrStr]("Content-Type", content_type),
                param[UUID]("Idempotency-Key", uuid4()),
            ],
            body=form_body(param[str]("id", id_), param[str]("users", users)),
            auth_scheme=self._auth.slack_auth,
            decoder=json_decoder[Defaultsuccesstemplate],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def calls_participants_remove(
        self,
        token: str,
        content_type: ContentTypeOrStr,
        id_: str,
        users: str,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[Defaultsuccesstemplate, RawError]:
        """Registers participants removed from a Call.

        Args:
            token: Authentication token. Requires scope: ``calls:write``
            content_type: Value sent with the request.
            id_: ``id`` returned by the /methods/calls.add method.
            users: The list of users to remove as participants in the Call. `Read more on how to specify users here
                </apis/calls#users>`__.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/calls.participants.remove"),
            headers=[
                param[str]("token", token),
                param[ContentTypeOrStr]("Content-Type", content_type),
                param[UUID]("Idempotency-Key", uuid4()),
            ],
            body=form_body(param[str]("id", id_), param[str]("users", users)),
            auth_scheme=self._auth.slack_auth,
            decoder=json_decoder[Defaultsuccesstemplate],
            error_mapper=raw_error_response,
            request_options=request_options,
        )


class AsyncCallsParticipantsWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def calls_participants_add(
        self,
        token: str,
        content_type: ContentTypeOrStr,
        id_: str,
        users: str,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[Defaultsuccesstemplate, RawError]:
        """Registers new participants added to a Call.

        Args:
            token: Authentication token. Requires scope: ``calls:write``
            content_type: Value sent with the request.
            id_: ``id`` returned by the /methods/calls.add method.
            users: The list of users to add as participants in the Call. `Read more on how to specify users here
                </apis/calls#users>`__.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/calls.participants.add"),
            headers=[
                param[str]("token", token),
                param[ContentTypeOrStr]("Content-Type", content_type),
                param[UUID]("Idempotency-Key", uuid4()),
            ],
            body=form_body(param[str]("id", id_), param[str]("users", users)),
            auth_scheme=self._auth.slack_auth,
            decoder=async_json_decoder[Defaultsuccesstemplate],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def calls_participants_remove(
        self,
        token: str,
        content_type: ContentTypeOrStr,
        id_: str,
        users: str,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[Defaultsuccesstemplate, RawError]:
        """Registers participants removed from a Call.

        Args:
            token: Authentication token. Requires scope: ``calls:write``
            content_type: Value sent with the request.
            id_: ``id`` returned by the /methods/calls.add method.
            users: The list of users to remove as participants in the Call. `Read more on how to specify users here
                </apis/calls#users>`__.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/calls.participants.remove"),
            headers=[
                param[str]("token", token),
                param[ContentTypeOrStr]("Content-Type", content_type),
                param[UUID]("Idempotency-Key", uuid4()),
            ],
            body=form_body(param[str]("id", id_), param[str]("users", users)),
            auth_scheme=self._auth.slack_auth,
            decoder=async_json_decoder[Defaultsuccesstemplate],
            error_mapper=raw_error_response,
            request_options=request_options,
        )
