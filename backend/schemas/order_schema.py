from pydantic import BaseModel
from datetime import datetime


class OrderBase(BaseModel):  # 주문
    class Config:
        orm_mode = True

class Order(OrderBase):
    user_id: int
    store_id: int
    datetime: datetime
    is_takeout: bool
    cost: int
    is_active: bool


class OrderCreate(OrderBase):
    user_id: int
    store_id: int
    datetime: datetime
    is_takeout: bool
    cost: int


class OrderRead(OrderCreate):
    int: str


class OrderDelete(OrderBase):
    is_active: bool
