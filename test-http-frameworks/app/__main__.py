import uvicorn
from fastapi import FastAPI

from app import root_router
from middlewares import middleware


def create_app():
    app = FastAPI(middleware=middleware)

    app.include_router(root_router.router)
    return app


if __name__ == "__main__":
    app = create_app()

    uvicorn.run(app, host="0.0.0.0", port=8000)
