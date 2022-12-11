from dataclasses import dataclass
from typing import Union

from pydantic import BaseModel


# @dataclass
class Item(BaseModel):
    name: str
    price: float
    description: Union[str, None] = None
    tax: Union[float, None] = None
