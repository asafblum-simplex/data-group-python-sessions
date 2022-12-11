import time

from starlette.applications import Starlette
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.requests import Request
from starlette.responses import JSONResponse, Response

import uvicorn
from starlette.types import ASGIApp

from with_logger import log
from starlette_context import context, middleware, plugins




app = Starlette(debug=True)

@app.middleware("http")
async def foo(request: Request, call_next):
    x = await request.body()
    print(x)
    return call_next(request)


@app.middleware("http")
async def add_process_time_header(request: Request, call_next):
    x = await request.body()
    print(x)
    start_time = time.time()
    response = await call_next(request)
    process_time = time.time() - start_time
    response.headers["X-Process-Time"] = str(process_time)
    return response


@app.route("/")
async def index(request: Request):
    log.info("Log from view")
    return JSONResponse(context.data)


uvicorn.run(app, host="0.0.0.0", port=3000)
