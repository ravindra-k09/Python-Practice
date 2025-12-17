
from pydantic import BaseModel, HttpUrl
from typing import Literal

class Product(BaseModel):
    id: int
    title: str
    price: float
    description: str
    category: str
    image: HttpUrl
