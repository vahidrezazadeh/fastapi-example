from fastapi import Request, Response
from starlette.middleware.base import BaseHTTPMiddleware, RequestResponseEndpoint

from utils.log import log
from utils.timezones import timezone_utils


class LoggerMiddleware(BaseHTTPMiddleware):
    """Record request log middleware"""

    async def dispatch(self, request: Request, call_next: RequestResponseEndpoint) -> Response:
        start_time = timezone_utils.get_timezone_datetime()
        response = await call_next(request)
        end_time = timezone_utils.get_timezone_datetime()
        log.info(f'{response.status_code} {request.client.host} {request.method} {request.url} {end_time - start_time}')
        return response