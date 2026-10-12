from __future__ import annotations

from ..auth import AsyncAuthSchemes, AuthSchemes
from ..core import (
    ApiResult,
    AsyncRawClient,
    RawClient,
    RawError,
    RequestOptionsOrDict,
    SecuredRawResponse,
    async_json_decoder,
    json_decoder,
    param,
    raw_error_response,
    unwrap,
)
from ..models.bots_infoschema import BotsInfoschema
from ..models.enums.content_type import ContentTypeOrStr
from ..server.server import Server


class Bots:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = BotsWithRawResponse(client, server, auth)

    def bots_info(
        self,
        token: str,
        content_type: ContentTypeOrStr,
        *,
        bot: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> BotsInfoschema:
        """Gets information about a bot user.

        Args:
            token: Authentication token. Requires scope: ``users:read``
            content_type: Value sent with the request.
            bot: Bot user to get info on
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            When successful, returns bot info by bot ID.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(self._with_raw_response.bots_info(token, content_type, bot=bot, request_options=request_options))

    @property
    def with_raw_response(self) -> BotsWithRawResponse:
        return self._with_raw_response


class AsyncBots:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncBotsWithRawResponse(client, server, auth)

    async def bots_info(
        self,
        token: str,
        content_type: ContentTypeOrStr,
        *,
        bot: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> BotsInfoschema:
        """Gets information about a bot user.

        Args:
            token: Authentication token. Requires scope: ``users:read``
            content_type: Value sent with the request.
            bot: Bot user to get info on
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            When successful, returns bot info by bot ID.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(
            await self._with_raw_response.bots_info(token, content_type, bot=bot, request_options=request_options)
        )

    @property
    def with_raw_response(self) -> AsyncBotsWithRawResponse:
        return self._with_raw_response


class BotsWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def bots_info(
        self,
        token: str,
        content_type: ContentTypeOrStr,
        *,
        bot: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[BotsInfoschema, RawError]:
        """Gets information about a bot user.

        Args:
            token: Authentication token. Requires scope: ``users:read``
            content_type: Value sent with the request.
            bot: Bot user to get info on
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/bots.info"),
            query_params=[param[str]("token", token), param[str | None]("bot", bot)],
            headers=[param[ContentTypeOrStr]("Content-Type", content_type)],
            auth_scheme=self._auth.slack_auth,
            decoder=json_decoder[BotsInfoschema],
            error_mapper=raw_error_response,
            request_options=request_options,
        )


class AsyncBotsWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def bots_info(
        self,
        token: str,
        content_type: ContentTypeOrStr,
        *,
        bot: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[BotsInfoschema, RawError]:
        """Gets information about a bot user.

        Args:
            token: Authentication token. Requires scope: ``users:read``
            content_type: Value sent with the request.
            bot: Bot user to get info on
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/bots.info"),
            query_params=[param[str]("token", token), param[str | None]("bot", bot)],
            headers=[param[ContentTypeOrStr]("Content-Type", content_type)],
            auth_scheme=self._auth.slack_auth,
            decoder=async_json_decoder[BotsInfoschema],
            error_mapper=raw_error_response,
            request_options=request_options,
        )
