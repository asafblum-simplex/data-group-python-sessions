import json

from starlette.requests import Request
from starlette.types import Scope, Message


class BaseRequest(Request):
    def __init__(self, scope: Scope, receive) -> None:
        super().__init__(scope, receive)
        self.state.body = None
        self.state.body_returned = False

    async def body(self) -> bytes:
        if not self.payload:
            print("getting body")
            # dict shout be byted
            self.payload = self.state.temp_body
            self.payload = json.dumps(self.state.temp_body).encode()
            print("log body", self.payload, self.headers)
            self.has_response = True

        return self.payload

    @property
    def payload(self):
        return self.state.body

    @payload.setter
    def payload(self, value):
        self.state.body = value

    @property
    def has_response(self) -> bool:
        return self.state.body_returned

    @has_response.setter
    def has_response(self, value: bool):
        self.state.body_returned = value
