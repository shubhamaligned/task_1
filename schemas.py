from pydantic import BaseModel
from typing import List, Optional

class ProductCreate(BaseModel):
    name: str
    description: Optional[str] = None
    price: float

class ProductUpdate(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None

class ProductResponse(ProductCreate):
    id: int

    class Config:
        orm_mode = True

class OrderCreate(BaseModel):
    customer_id: int
    product_ids: List[int]

class OrderUpdate(BaseModel):
    status: str

class OrderResponse(BaseModel):
    id: int
    customer_id: int
    status: str
    product_ids: List[int]

    class Config:
        orm_mode = True
