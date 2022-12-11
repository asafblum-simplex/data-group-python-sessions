from fastapi import HTTPException
from starlette.middleware import Middleware
from starlette.middleware.base import BaseHTTPMiddleware


class SaveBodyMiddleware(BaseHTTPMiddleware):
    def __init__(self, app):
        super().__init__(app)

    async def dispatch(self, request, call_next):
        print(f"middleware save body", "before")

        payload = await request.json()
        request.state.temp_body = payload
        res = await call_next(request)
        print(f"middleware save body", "after", res)
        return res


class BasicMiddleware(BaseHTTPMiddleware):
    def __init__(self, app, order: int):
        super().__init__(app)
        self.order = order

    async def dispatch(self, request, call_next):
        print(f"middleware-{self.order}", "before")

        payload = await request.json()
        print(payload)

        res = await call_next(request)
        print(f"middleware-{self.order}", "after", res)
        return res


middleware = [
    # Middleware(UpgradeRequest),
    Middleware(SaveBodyMiddleware),
    Middleware(BasicMiddleware, order=1),
    Middleware(BasicMiddleware, order=2),
    Middleware(BasicMiddleware, order=3),
]
