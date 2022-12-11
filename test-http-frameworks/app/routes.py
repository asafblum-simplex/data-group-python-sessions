from typing import Callable

from fastapi.routing import APIRoute
from starlette.requests import Request
from starlette.responses import Response

from requests import BaseRequest


class FooRoute(APIRoute):
    pass


class BasicRoute(APIRoute):
    def get_route_handler(self) -> Callable:
        original_route_handler = super().get_route_handler()

        async def custom_route_handler(request: Request) -> Response:
            request = BaseRequest(request.scope, request.receive)
            # log request
            return await original_route_handler(request)  # decides the actual function handler
            # log response

        return custom_route_handler
