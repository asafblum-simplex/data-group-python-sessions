import json
from typing import Callable

from fastapi import APIRouter
from starlette.requests import Request

from routes import BasicRoute
from models import Item

router = APIRouter()
router.route_class = BasicRoute


@router.post('/', tags=['root'])
async def create(r: Request, item: Item):
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
