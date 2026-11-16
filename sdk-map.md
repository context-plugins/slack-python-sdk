<!-- Generated file — do not edit; regenerated with the SDK. -->

# SDK map — Slack Web API (Python)

> A generated table of contents for this SDK. Consult this map and its sub-pages to learn signatures, error types, and server/auth wiring **by lookup**. Model shapes and enum values are *not* duplicated here — the map names the module declaring each type; read the shape there. Every name is the emitted spelling, so a wrong one fails at import rather than working silently.

|  |  |
| --- | --- |
| SDK display name | Slack Web API |
| Root package | `slack_web_api` |
| Distribution name | `slack-web-api` |
| Requires | Python 3.10 or later |
| API spec version | `1.7.0` |
| Generator | APIMatic |

Staleness check: the API spec version above changes when the SDK is regenerated from a new spec, and the package version is what `pip show` reports for the installed SDK. If a lookup here fails at import, re-read the module named in the row.

All `Source` paths on this map and its sub-pages are relative to the **SDK root** — the directory holding this file and `pyproject.toml` — never to the page that carries them. Open them as-is from the SDK root; if the SDK sits under a subdirectory of a larger repo, prefix that subdirectory.

---

## Getting a client

### Synchronous client

```python
from slack_web_api import SlackWebApiClient
from slack_web_api.auth import SlackAuthScope
from slack_web_api.core import AuthorizationCodeCredentials


def prompt(url: str) -> str:
    return input(f"Open {url}, then paste the code: ")


client = SlackWebApiClient(
    slack_auth=AuthorizationCodeCredentials[SlackAuthScope](
        client_id="YOUR_CLIENT_ID", redirect_uri="YOUR_REDIRECT_URI", prompt_for_authorization_code=prompt
    ),
)

# TODO: call endpoints here -- see api-reference.md

client.close()
```

Alternatively, scope it — `with SlackWebApiClient(...) as client:` closes the pool on exit.

### Asynchronous client

```python
from asyncio import run, to_thread

from slack_web_api import AsyncSlackWebApiClient
from slack_web_api.auth import SlackAuthScope
from slack_web_api.core import AsyncAuthorizationCodeCredentials


async def prompt(url: str) -> str:
    print(f"Open {url}")
    return await to_thread(input, "Paste the code: ")


async def main() -> None:
    client = AsyncSlackWebApiClient(
        slack_auth=AsyncAuthorizationCodeCredentials[SlackAuthScope](
            client_id="YOUR_CLIENT_ID", redirect_uri="YOUR_REDIRECT_URI", prompt_for_authorization_code=prompt
        ),
    )
    # TODO: call endpoints here, awaiting each -- see api-reference.md
    await client.aclose()


run(main())
```

Alternatively, scope it — `async with AsyncSlackWebApiClient(...) as client:` closes the pool on exit.

`AsyncClient` (`slack_web_api/async_client.py`) mirrors `Client` method for method, each endpoint method a coroutine. It takes the same keywords, except that each client accepts only its own transport and — where the **Async Type** column differs — only its own flavour.

`Client` and `AsyncClient` are aliases of `SlackWebApiClient` and `AsyncSlackWebApiClient` — the names tracebacks and `repr()` show; all four import from the root.

`close()` / `aclose()` closes the transport even when you supplied one via `custom_http_client=` / `custom_async_http_client=`, and a closed client cannot be reused.

Every API group is a property on the client (e.g. `client.admin`). Every constructor argument is optional and keyword-only. Sources: `slack_web_api/client.py`, `slack_web_api/async_client.py`:

| Keyword | Sync Type | Async Type | Default |
| --- | --- | --- | --- |
| `server_config` | `ServerConfigOrDict \| None` | `ServerConfigOrDict \| None` | `None` |
| `timeout` | `float` | `float` | `30.0` seconds |
| `retry_options` | `int \| RetryOptionsOrDict \| None` | `int \| RetryOptionsOrDict \| None` | `None` |
| `logging_options` | `LoggingOptionsOrDict \| None` | `LoggingOptionsOrDict \| None` | `None` |
| `hooks` | `Sequence[SdkHook] \| SdkHooksDict \| None` | `Sequence[AsyncSdkHook] \| AsyncSdkHooksDict \| None` | `None` |
| `custom_http_client` | `HttpClient \| None` | — | `None` |
| `custom_async_http_client` | — | `AsyncHttpClient \| None` | `None` |
| `slack_auth` | `AuthorizationCodeCredentialsOrDict[SlackAuthScope] \| None` | `AsyncAuthorizationCodeCredentialsOrDict[SlackAuthScope] \| None` | `None` |
| `slack_auth_token_source` | `RefreshableTokenSource[AuthorizationCodeCredentials[SlackAuthScope]] \| None` | `AsyncRefreshableTokenSource[AsyncAuthorizationCodeCredentials[SlackAuthScope]] \| None` | `None` |

The types those columns name — where each imports from and, for a credentials dict, its keys:

| Type | Import from | Shape |
| --- | --- | --- |
| `ServerConfigOrDict` | `slack_web_api.server` | keys as the Servers & auth tables read |
| `RetryOptionsOrDict` | `slack_web_api.core` | a retry count, `RetryOptions`, or a dict: `max_retries: int` · `initial_delay: float` · `backoff_factor: float` · `max_delay: float` · `max_jitter: float` · `status_codes_to_retry: frozenset[int]` · `http_methods_to_retry: frozenset[HttpMethod]` |
| `LoggingOptionsOrDict` | `slack_web_api.core` | `LoggingOptions` or a dict: `log_request_headers: bool` · `log_response_headers: bool` · `log_request_body: bool` · `body_size_limit: int` · `redaction_placeholder: str` · `unmask_headers: AbstractSet[str]` · `mask_headers: AbstractSet[str]` · `mask_keys: AbstractSet[str]` |
| `SdkHook` | `slack_web_api.core` | protocol — `before_request(request: HttpRequest, context: HookContext) -> HttpRequest` · `after_response(response: HttpResponse, context: HookContext) -> HttpResponse`; subclass it and override either, or pass plain functions as an `SdkHooksDict` |
| `SdkHooksDict` | `slack_web_api.core` | dict — `on_request`: functions `(HttpRequest, HookContext) -> HttpRequest` · `on_response`: functions `(HttpResponse, HookContext) -> HttpResponse`; both optional, the `on_request` ones run first, any other key is ignored |
| `HttpClient` | `slack_web_api.core` | protocol — `send(request: HttpRequest) -> HttpResponse` · `close()`; `send` returns once the head has arrived and never reads the body, and raises `SdkConnectionError` (from `core`; `SdkTimeoutError` for a timeout) when no response arrives, as the response's reads do for a body they cannot deliver, naming the call as `request.method` and `safe_url(request.url)` — anything else it raises is never retried |
| `AuthorizationCodeCredentialsOrDict` | `slack_web_api.core` | `AuthorizationCodeCredentials` or a dict: `client_id: str` · `client_secret: str \| None` · `redirect_uri: str` · `scopes: list[Scope] \| None` · `state: str \| None` · `pkce: PkceMethod \| None = "S256"` · `prompt_for_authorization_code: AuthorizationCodePrompt` |
| `SlackAuthScope` | `slack_web_api.auth` | `Enum` of the declared scopes |
| `RefreshableTokenSource` | `slack_web_api.core` | protocol — `fetch(credentials) -> OAuthTokenRefreshable` · `refresh(credentials, refresh_token) -> OAuthTokenRefreshable \| None` |
| `AuthorizationCodeCredentials` | `slack_web_api.core` | `client_id: str` · `client_secret: str \| None` · `redirect_uri: str` · `scopes: list[Scope] \| None` · `state: str \| None` · `pkce: PkceMethod \| None = "S256"` · `prompt_for_authorization_code: AuthorizationCodePrompt` |
| `AsyncSdkHook` | `slack_web_api.core` | protocol — the same two methods as `async def`, taking `AsyncHookContext` and `AsyncHttpResponse`; `async def` functions go in an `AsyncSdkHooksDict` |
| `AsyncSdkHooksDict` | `slack_web_api.core` | dict — the same two keys, each function `async def`, taking `AsyncHookContext` and, for a response, `AsyncHttpResponse` |
| `AsyncHttpClient` | `slack_web_api.core` | protocol — `async send(request: HttpRequest) -> AsyncHttpResponse` · `async aclose()`; the same obligation, awaited |
| `AsyncAuthorizationCodeCredentialsOrDict` | `slack_web_api.core` | `AsyncAuthorizationCodeCredentials` or a dict: `client_id: str` · `client_secret: str \| None` · `redirect_uri: str` · `scopes: list[Scope] \| None` · `state: str \| None` · `pkce: PkceMethod \| None = "S256"` · `prompt_for_authorization_code: AsyncAuthorizationCodePrompt` |
| `AsyncRefreshableTokenSource` | `slack_web_api.core` | protocol — `async fetch(credentials) -> OAuthTokenRefreshable` · `async refresh(credentials, refresh_token) -> OAuthTokenRefreshable \| None` |
| `AsyncAuthorizationCodeCredentials` | `slack_web_api.core` | `client_id: str` · `client_secret: str \| None` · `redirect_uri: str` · `scopes: list[Scope] \| None` · `state: str \| None` · `pkce: PkceMethod \| None = "S256"` · `prompt_for_authorization_code: AsyncAuthorizationCodePrompt` |

### Retries — on by default

`retry_options` left at `None` applies the default `RetryOptions` policy below, so an unconfigured client **retries**: a request whose method is in `http_methods_to_retry` is sent again when it gets a status in `status_codes_to_retry`, or no response at all, and the last outcome reaches you only once its retries are spent. A body that cannot be re-sent byte for byte — a streamed file upload — is never retried. `retry_options=0` (or `{"max_retries": 0}`) turns retrying off; a bare count sets `max_retries` and leaves every other field at its default.

`RetryOptions` fields (source: `slack_web_api/core/retries.py`). Pass only the fields you change; each one left out takes its default:

| Field | Type | Default |
| --- | --- | --- |
| `max_retries` | `int` | `3` |
| `initial_delay` | `float` (seconds) | `1.0` |
| `backoff_factor` | `float` | `2.0` |
| `max_delay` | `float` (seconds) | `60.0` |
| `max_jitter` | `float` (seconds) | `0.5` |
| `status_codes_to_retry` | `frozenset[int]` | `frozenset({408, 429, 500, 502, 503, 504})` |
| `http_methods_to_retry` | `frozenset[HttpMethod]` | `frozenset({"GET", "HEAD", "PUT", "OPTIONS"})` |

The wait before retry *n* is `initial_delay × backoff_factor^(n−1)` plus up to `max_jitter` of random delay, the sum capped at `max_delay`; a `Retry-After` header replaces it, trimmed to `max_delay`.

A single call overrides two of these through `request_options` (`slack_web_api/core/request_options.py`): `max_retries` and `status_codes_to_retry`, each merged over the client's policy field by field — `request_options={"max_retries": 0}` turns retrying off for that one call and leaves every other call alone.

### Logging — off by default

Every HTTP exchange is written through the standard `logging` module under the `slack_web_api` logger, and the SDK configures nothing itself. Set that logger's level to turn it on: INFO writes the request line and a 2xx response line, WARNING a non-2xx response line and each retry, ERROR a call that ends in an exception, and DEBUG the header dumps and the request body that the flags below turn on. Or set `SLACK_WEB_API_LOG=info|debug` before the process starts: it sets the level, turns the three flags on for `debug`, and adds a stderr handler only where nothing listens.

`LoggingOptions` fields (source: `slack_web_api/core/logging.py`). Pass only the fields you change; each one left out takes its default, and a name set you pass replaces its default:

| Field | Type | Default |
| --- | --- | --- |
| `log_request_headers` | `bool` | `False` |
| `log_response_headers` | `bool` | `False` |
| `log_request_body` | `bool` | `False` |
| `body_size_limit` | `int` (bytes) | `32768` |
| `redaction_placeholder` | `str` | `"REDACTED"` |
| `unmask_headers` | `AbstractSet[str]` | `frozenset()` |
| `mask_headers` | `AbstractSet[str]` | `frozenset()` |
| `mask_keys` | `AbstractSet[str]` | `frozenset({"sig", "signature", "access_token", "apikey", "api_key", "client_secret", "password", "refresh_token", "code", "assertion", "client_assertion"})` |

A single call is quietened through `request_options` (`slack_web_api/core/request_options.py`): `log_level`, a `logging` level constant, is a floor below which that call's records are not written; it never turns a dump or the body on. A header value prints `REDACTED` unless its name is on the runtime's safe list, a query value unless its key is a paging name, and a form field whose key is in `mask_keys` always; a JSON body prints as sent; a response body is never logged.

### Hooks — none by default

A hook is caller code run on every attempt of every request, retries and the token requests an OAuth scheme makes included (source: `slack_web_api/core/hooks.py`). `before_request` runs after authentication and before the request line is logged, and returns the request to send: the one it was given, or a `dataclasses.replace` of it. `after_response` runs after the response line and the 401 check and before the retry decision, and returns the response the call acts on. The client's hooks run first, in order, then the call's.

A single call adds hooks through `request_options` (`slack_web_api/core/request_options.py`): `hooks`, a list of hooks or an `SdkHooksDict`, appended to the client's and never replacing them. The client keeps the hooks it was given uncopied, so a list changed after construction is read by the next call. On the async client the per-call options are `AsyncRequestOptions`, whose `hooks` are `AsyncSdkHook` or an `AsyncSdkHooksDict`; a hook of the other flavour is a type error, and nothing is checked at run time.

A hook that raises ends the call with that exception, after any open response is closed. The one exception is `SdkConnectionError` raised from `before_request` naming the call, `safe_url(context.url)`: the attempt is retried as a failed send, under the same method and retry-count rules as a transport failure. Raised from `after_response`, it ends the call like any other exception. On a token request an OAuth scheme makes only the client's hooks run, not the call's, and one that raises reaches you as `AuthSchemeError` with its exception in `scheme_failures`; in an `OR` requirement the next configured scheme is tried first.

---

## Error-handling model (read once — applies to every operation)

Every operation is reached in two response modes:

- **Parsed call.** Returns the decoded payload and raises `ApiError` on an error status, with the decoded body on `.error` and the status on `.status_code`.
- **Raw call.** Reached through `.with_raw_response`; returns `ApiResult` — `Success` or `Failure` — and never raises for an API error. Read `.payload` on a `Success` or `.error` on a `Failure`; both carry `.status_code` and `.headers`.

Everything a call raises derives from `SdkError`, so one `except SdkError` covers any number of calls; every member names the call as `.method` and `.url` and keeps what caused it on `__cause__`. Besides `ApiError`, three members raise in **both** modes: `ResponseDecodeError` for a body its declared type rejects, `SdkConnectionError` for no usable response (`SdkTimeoutError` when it timed out) and `AuthSchemeError` for a credential that could not be applied. `ApiError` and `ResponseDecodeError` are siblings, so `except ApiError` never catches a 2xx that broke its contract.

What `.error` holds is fixed per operation. There are two cases:

- **Case A — typed error.** The operation documents at least one error status, so `slack_web_api/errors/` declares a union alias over the bodies those statuses map to — `RawError` is always its last arm, for any undocumented status — and `.error` is annotated with that alias. Narrow it with a `match` class pattern or `isinstance`. The operation blocks name the alias and the status each arm maps from.
- **Case B — raw error.** The operation documents no error status; `.error` is `RawError` (`slack_web_api/core/results.py`): `status_code: int` · `content: bytes` · `text(encoding="utf-8"): str` · `json(): Any`.

Core runtime types (`slack_web_api/core/`) — public members with their **declared types**, verbatim from source:

| Type | Public members | Source |
| --- | --- | --- |
| `SdkError` — the root of everything a call raises | `method: HttpMethod` · `url: str` — the path rendered, no query; the cause on `__cause__` | `slack_web_api/core/exceptions.py` |
| `ApiError` — raised by every parsed call; `.error` is always `RawError` (no Case A alias in this SDK) | `error: E` · `status_code: int` · `headers: Mapping[str, str]` · `method: HttpMethod` · `url: str` | `slack_web_api/core/exceptions.py` |
| `ResponseDecodeError` — a body its declared type rejects, in both modes | `status_code: int` · `headers: Mapping[str, str]` · `method` · `url` | `slack_web_api/core/exceptions.py` |
| `SdkConnectionError` — no usable response, in both modes | `method` · `url`; the HTTP library's exception on `__cause__` | `slack_web_api/core/exceptions.py` |
| `SdkTimeoutError` — the `SdkConnectionError` that timed out | `timeout: float` · `method` · `url` | `slack_web_api/core/exceptions.py` |
| `AuthSchemeError` — a credential that could not be applied, in both modes | `scheme_failures: tuple[Exception, ...]` · `method` · `url` | `slack_web_api/core/exceptions.py` |
| `ApiResult[T, E]` — returned by every raw call; the `Success[T] \| Failure[E]` union | `payload: T` (on `Success`) · `error: E` (on `Failure`) · `status_code: int` · `headers: Mapping[str, str]` · `method: HttpMethod` · `url: str` (all four on either) | `slack_web_api/core/results.py` |
| `RawError` | `status_code: int` · `content: bytes` · `text(encoding="utf-8"): str` · `json(): Any` | `slack_web_api/core/results.py` |

Typed error bodies (the arms of a Case A alias) are ordinary models — no special handling. The operation's **Type sources** table gives the module that declares each one; read field names, declared types and JSON aliases there, as for any other model.

```python
try:
    response = client.admin.admin_apps_approve("some example string", ContentType.APPLICATION_X_WWW_FORM_URLENCODED)
except ApiError as e:
    # Case B — raw error: e.error is RawError.
    print(e.status_code, e.error.text())
except ResponseDecodeError as e:
    # Body rejected by its declared type.
    print(f"{e.status_code}: undecodable body ({type(e.__cause__).__name__})")
except SdkTimeoutError as e:
    # No response, body or next event in time.
    print(f"{e.method} {e.url} timed out after {e.timeout} s")
except SdkConnectionError as e:
    # Refused, dropped, or cut off mid-body.
    print(f"{e.method} {e.url} could not connect: {e.__cause__!r}")
except AuthSchemeError as e:
    # A credential could not be applied; one failure per scheme tried.
    for failure in e.scheme_failures:
        print(f"{e.method} {e.url} unauthenticated: {failure}")
except SdkError as e:
    # A member added later.
    print(e)
except Exception as e:
    # Not a call failure: input refused before sending (ValueError), a handler you wrote raising, or a bug here.
    print(f"not a call failure: {e!r}")
    raise e
```

**Raw (`.with_raw_response`) variants: present on every operation** — the same call returns `ApiResult` instead of raising, with the same body on `Failure.error`. Of **253 operations**, **0 are Case A (typed)** and **253 are Case B (raw)**.

---

## Operations — by controller (56 pages, 253 operations)

Each links to a sub-page with one block per operation, headed by its full accessor path: the HTTP verb and route (for a mock, a raw request or a provider-side log — never reconstruct it from the method name), the sync parsed signature with its required positional parameters, each parameter's role and — where it differs — wire name, both return types, and its error case — **Case A** names the alias and the status each arm maps from, **Case B** names `RawError`. Every block also carries a **Type sources** table — every *generated* type it names, with the module that declares it. A runtime type — a file alias, a date/time or byte converter — is not listed there.

**Each block states what is specific to its operation. Everything below holds for every operation, and blocks never restate it — silence means the default applies.**

| Applies to every operation | Stated where |
| --- | --- |
| **Four spellings, one signature** — the same method name and parameters on `Client` and `AsyncClient`, each also reachable through `.with_raw_response`; the async twin is a coroutine to `await`, with the same return types and error case, and where the **Async Type** column differs, pass the type it names | Getting a client |
| **Parsed raises, raw returns** — `ApiError` versus `ApiResult` | Error-handling model |
| **Case B error is always `RawError`** — also the last arm of every Case A alias, where a block's **Error arms** bullet ends in it | Error-handling model |
| **A trailing `request_options`** — keyword-only and optional, for per-call overrides such as a timeout, extra headers, `max_retries`, `status_codes_to_retry`, `log_level` or `hooks`; every signature ends with it | here (`slack_web_api/core/request_options.py`), Retries, Logging, Hooks |
| **Each operation names its own server** — this SDK declares several, so every block carries a **Server** bullet with the server's key in `server_config=` | its block |
| **Parameter names are literal** — signatures are generated code verbatim, and everything behind the bare `*` must be passed by name | here |
| **A parameter's wire name is its Python name** — sent as-is on the path, query string, header or body, unless the block's **Params** bullet carries a wire name beside the role | here |

**The operation's behavioural prose lives on the operation itself**, as the method's docstring in the module named at the top of its page, and again in `api-reference.md` with a per-parameter description and a usage sample. Blocks here give you the contract — names, types, shapes, errors. Where an operation's *semantics* decide what you must pass, that is what the docstring settles; read it there rather than filling it in from memory.

Sub-pages chunk per `###` block: each block is self-contained given the table above, and assumes this page is loaded beside it.

| Controller | Class | Ops | Page |
| --- | --- | --- | --- |
| `client.admin` | `Admin` / `AsyncAdmin` | 56 | [map/operations/admin.md](map/operations/admin.md) |
| `client.admin_apps` | `AdminApps` / `AsyncAdminApps` | 2 | [map/operations/admin_apps.md](map/operations/admin_apps.md) |
| `client.admin_apps_approved` | `AdminAppsApproved` / `AsyncAdminAppsApproved` | 1 | [map/operations/admin_apps_approved.md](map/operations/admin_apps_approved.md) |
| `client.admin_apps_requests` | `AdminAppsRequests` / `AsyncAdminAppsRequests` | 1 | [map/operations/admin_apps_requests.md](map/operations/admin_apps_requests.md) |
| `client.admin_apps_restricted` | `AdminAppsRestricted` / `AsyncAdminAppsRestricted` | 1 | [map/operations/admin_apps_restricted.md](map/operations/admin_apps_restricted.md) |
| `client.admin_conversations` | `AdminConversations` / `AsyncAdminConversations` | 13 | [map/operations/admin_conversations.md](map/operations/admin_conversations.md) |
| `client.admin_conversations_ekm` | `AdminConversationsEkm` / `AsyncAdminConversationsEkm` | 1 | [map/operations/admin_conversations_ekm.md](map/operations/admin_conversations_ekm.md) |
| `client.admin_conversations_restrict_access` | `AdminConversationsRestrictAccess` / `AsyncAdminConversationsRestrictAccess` | 3 | [map/operations/admin_conversations_restrict_access.md](map/operations/admin_conversations_restrict_access.md) |
| `client.admin_emoji` | `AdminEmoji` / `AsyncAdminEmoji` | 5 | [map/operations/admin_emoji.md](map/operations/admin_emoji.md) |
| `client.admin_invite_requests` | `AdminInviteRequests` / `AsyncAdminInviteRequests` | 3 | [map/operations/admin_invite_requests.md](map/operations/admin_invite_requests.md) |
| `client.admin_invite_requests_approved` | `AdminInviteRequestsApproved` / `AsyncAdminInviteRequestsApproved` | 1 | [map/operations/admin_invite_requests_approved.md](map/operations/admin_invite_requests_approved.md) |
| `client.admin_invite_requests_denied` | `AdminInviteRequestsDenied` / `AsyncAdminInviteRequestsDenied` | 1 | [map/operations/admin_invite_requests_denied.md](map/operations/admin_invite_requests_denied.md) |
| `client.admin_teams` | `AdminTeams` / `AsyncAdminTeams` | 2 | [map/operations/admin_teams.md](map/operations/admin_teams.md) |
| `client.admin_teams_admins` | `AdminTeamsAdmins` / `AsyncAdminTeamsAdmins` | 1 | [map/operations/admin_teams_admins.md](map/operations/admin_teams_admins.md) |
| `client.admin_teams_owners` | `AdminTeamsOwners` / `AsyncAdminTeamsOwners` | 1 | [map/operations/admin_teams_owners.md](map/operations/admin_teams_owners.md) |
| `client.admin_teams_settings` | `AdminTeamsSettings` / `AsyncAdminTeamsSettings` | 6 | [map/operations/admin_teams_settings.md](map/operations/admin_teams_settings.md) |
| `client.admin_usergroups` | `AdminUsergroups` / `AsyncAdminUsergroups` | 4 | [map/operations/admin_usergroups.md](map/operations/admin_usergroups.md) |
| `client.admin_users` | `AdminUsers` / `AsyncAdminUsers` | 8 | [map/operations/admin_users.md](map/operations/admin_users.md) |
| `client.admin_users_session` | `AdminUsersSession` / `AsyncAdminUsersSession` | 2 | [map/operations/admin_users_session.md](map/operations/admin_users_session.md) |
| `client.api2` | `Api2` / `AsyncApi2` | 1 | [map/operations/api2.md](map/operations/api2.md) |
| `client.apps` | `Apps` / `AsyncApps` | 8 | [map/operations/apps.md](map/operations/apps.md) |
| `client.apps_event_authorizations` | `AppsEventAuthorizations` / `AsyncAppsEventAuthorizations` | 1 | [map/operations/apps_event_authorizations.md](map/operations/apps_event_authorizations.md) |
| `client.apps_permissions` | `AppsPermissions` / `AsyncAppsPermissions` | 2 | [map/operations/apps_permissions.md](map/operations/apps_permissions.md) |
| `client.apps_permissions_resources` | `AppsPermissionsResources` / `AsyncAppsPermissionsResources` | 1 | [map/operations/apps_permissions_resources.md](map/operations/apps_permissions_resources.md) |
| `client.apps_permissions_scopes` | `AppsPermissionsScopes` / `AsyncAppsPermissionsScopes` | 1 | [map/operations/apps_permissions_scopes.md](map/operations/apps_permissions_scopes.md) |
| `client.apps_permissions_users` | `AppsPermissionsUsers` / `AsyncAppsPermissionsUsers` | 2 | [map/operations/apps_permissions_users.md](map/operations/apps_permissions_users.md) |
| `client.auth_api` | `AuthApi` / `AsyncAuthApi` | 2 | [map/operations/auth_api.md](map/operations/auth_api.md) |
| `client.bots` | `Bots` / `AsyncBots` | 1 | [map/operations/bots.md](map/operations/bots.md) |
| `client.calls` | `Calls` / `AsyncCalls` | 6 | [map/operations/calls.md](map/operations/calls.md) |
| `client.calls_participants` | `CallsParticipants` / `AsyncCallsParticipants` | 2 | [map/operations/calls_participants.md](map/operations/calls_participants.md) |
| `client.chat` | `Chat` / `AsyncChat` | 10 | [map/operations/chat.md](map/operations/chat.md) |
| `client.chat_scheduled_messages` | `ChatScheduledMessages` / `AsyncChatScheduledMessages` | 1 | [map/operations/chat_scheduled_messages.md](map/operations/chat_scheduled_messages.md) |
| `client.conversations` | `Conversations` / `AsyncConversations` | 18 | [map/operations/conversations.md](map/operations/conversations.md) |
| `client.dialog` | `Dialog` / `AsyncDialog` | 1 | [map/operations/dialog.md](map/operations/dialog.md) |
| `client.dnd` | `Dnd` / `AsyncDnd` | 5 | [map/operations/dnd.md](map/operations/dnd.md) |
| `client.emoji` | `Emoji` / `AsyncEmoji` | 1 | [map/operations/emoji.md](map/operations/emoji.md) |
| `client.files` | `Files` / `AsyncFiles` | 13 | [map/operations/files.md](map/operations/files.md) |
| `client.files_comments` | `FilesComments` / `AsyncFilesComments` | 1 | [map/operations/files_comments.md](map/operations/files_comments.md) |
| `client.files_remote` | `FilesRemote` / `AsyncFilesRemote` | 6 | [map/operations/files_remote.md](map/operations/files_remote.md) |
| `client.migration` | `Migration` / `AsyncMigration` | 1 | [map/operations/migration.md](map/operations/migration.md) |
| `client.oauth` | `Oauth` / `AsyncOauth` | 3 | [map/operations/oauth.md](map/operations/oauth.md) |
| `client.oauth_v2` | `OauthV2` / `AsyncOauthV2` | 1 | [map/operations/oauth_v2.md](map/operations/oauth_v2.md) |
| `client.pins` | `Pins` / `AsyncPins` | 3 | [map/operations/pins.md](map/operations/pins.md) |
| `client.reactions` | `Reactions` / `AsyncReactions` | 4 | [map/operations/reactions.md](map/operations/reactions.md) |
| `client.reminders` | `Reminders` / `AsyncReminders` | 5 | [map/operations/reminders.md](map/operations/reminders.md) |
| `client.rtm` | `Rtm` / `AsyncRtm` | 1 | [map/operations/rtm.md](map/operations/rtm.md) |
| `client.search` | `Search` / `AsyncSearch` | 1 | [map/operations/search.md](map/operations/search.md) |
| `client.stars` | `Stars` / `AsyncStars` | 3 | [map/operations/stars.md](map/operations/stars.md) |
| `client.team_api` | `TeamApi` / `AsyncTeamApi` | 5 | [map/operations/team_api.md](map/operations/team_api.md) |
| `client.team_profile` | `TeamProfile` / `AsyncTeamProfile` | 1 | [map/operations/team_profile.md](map/operations/team_profile.md) |
| `client.usergroups` | `Usergroups` / `AsyncUsergroups` | 7 | [map/operations/usergroups.md](map/operations/usergroups.md) |
| `client.usergroups_users` | `UsergroupsUsers` / `AsyncUsergroupsUsers` | 2 | [map/operations/usergroups_users.md](map/operations/usergroups_users.md) |
| `client.users` | `Users` / `AsyncUsers` | 12 | [map/operations/users.md](map/operations/users.md) |
| `client.users_profile` | `UsersProfile` / `AsyncUsersProfile` | 2 | [map/operations/users_profile.md](map/operations/users_profile.md) |
| `client.views` | `Views` / `AsyncViews` | 4 | [map/operations/views.md](map/operations/views.md) |
| `client.workflows` | `Workflows` / `AsyncWorkflows` | 3 | [map/operations/workflows.md](map/operations/workflows.md) |

---

## Models — where they live, how to build them

**Shapes live only in the source.** Every module under `slack_web_api/models/` declares one type plus its input companion, and every module under `slack_web_api/errors/` one alias plus the mapper that builds it; no two share a name. Take a type's module from the operation's **Type sources** table. When no retrieved chunk names it, the module is the type name in snake_case under the kind's directory below (`ApImethodusersGetPresence` ↔ `ap_imethodusers_get_presence.py`). Never grep for a type.

| Group | Count | Directory (module = `<type_name>.py`) |
| --- | --- | --- |
| Models (`SdkBaseModel` pydantic classes) | 357 | `slack_web_api/models/` |
| Enums (`Enum` over `str`) — Python member names + wire values | 89 | `slack_web_api/models/enums/` |

Conventions: a model is a `SdkBaseModel` (pydantic) class; a field whose wire name differs from its Python name carries it as `Field(alias=…)` (`type_` ↔ `"type"`) — read the alias off the field rather than deriving it. An omittable field is annotated `Optional[T]` and defaults to `UNSET`, and one that may also be explicitly null is `OptionalNullable[T]`; both come from `core` and neither is `typing.Optional` — there is no `None` arm unless the spec declared the property nullable, so passing `None` to the first is a type error rather than a value that serializes.

Every model and enum also has an **input companion**, exported beside it from the same package (`ApImethodusersGetPresence` ↔ `ApImethodusersGetPresenceDict`). Wherever a signature names the companion you may pass either the model instance or a plain dict with the same keys, whichever reads better at the call site. An enum is a real `Enum` subclass over `str`; its companion is spelled `<Name>OrStr` or `<Name>OrInt` (`AdminConversationsArchiveErrorEnum` ↔ `AdminConversationsArchiveErrorEnumOrStr`) and additionally accepts a wire value this SDK version does not know.

Import paths by content type (`from <package> import <Name>`):

| Contents | Import from |
| --- | --- |
| Client (root) | `slack_web_api` |
| Operation controllers | `slack_web_api.apis` |
| Models | `slack_web_api.models` |
| Enums | `slack_web_api.models.enums` |
| Core runtime (`SdkError`, `ApiError`, `ApiResult`, `RawError`, …) | `slack_web_api.core` |

---

## Servers & auth

**OAuth2 (authorization code).** Pass `slack_auth` your client id, redirect URI and authorization code; authorization is at `/authorize` and tokens come from `/oauth.v2.access`, both on the `default` server. Scopes are the `SlackAuthScope` alias.

Operation blocks name their scheme in an **Auth** bullet; an operation whose spec declares no scheme carries no such bullet.

- `AND` — every scheme listed must be configured for the call to succeed.
- `OR` — any one of the schemes listed can be used; the first one you configured is the one sent, in the order listed.

A scheme you did not configure is skipped silently rather than raising, and the request is sent anyway — so an authentication failure can mean no credential was sent rather than a bad one.

**One environment.** The spec declares a single environment, so no `environment` keyword exists and there is nothing to select.

**2 servers.** Base-URL templates and override points (`slack_web_api/server/server_config.py`):

| Server | Base URL | Override point |
| --- | --- | --- |
| `default` | `https://slack.com/api` | `{"default": {"base_url": …}}` |
| `auth_server` | `https://slack.com/oauth/v2` | `{"auth_server": {"base_url": …}}` |

Override any of these by passing `server_config=` a dict nested exactly as the columns above read — `{"default": {"base_url": …}}` — with each row's variables sitting beside its `base_url`.

