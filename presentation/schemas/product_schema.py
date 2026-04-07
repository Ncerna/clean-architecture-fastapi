from pydantic import BaseModel

class ProductCreateRequest(BaseModel):
    id: int
    name: str
    price: float
    stock: int


class ProductResponse(BaseModel):
    id: int
    name: str
    price: float
    stock: int