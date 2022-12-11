import json
from typing import Callable

from fastapi import APIRouter
from starlette.requests import Request

from routes import BasicRoute, FooRoute
from models import Item

router = APIRouter()
router.route_class = BasicRoute, FooRoute


class BasicFooRoute(BasicRoute, FooRoute):

    def get_route_handler(self) -> Callable:
        return super(BasicRoute).get_route_handler()


@router.post('/', tags=['root'])
async def create(item: Item, request:Request):
    # async def create(request: Request):
    print("ep")
    # body = request.state.temp_body

    # json_payload = json.loads(request.state.temp_body)
    return {"input": "item", 'json': item}

    # x2 = await request.body()
    # print("ep", item, request)
    # return item


@router.get("/")
async def main():
    return "somebigcontent"
