from enum import Enum
from typing import Tuple
from pydantic import BaseModel


class LocationBase(BaseModel):
    class Config:
        orm_mode = True


class Location(LocationBase):  # 위치 테이블
    points: Tuple[float, float]


class LocationCreate(LocationBase):
    points: Tuple[float, float]


class LocationRead(LocationCreate):
    pass


class StoreBase(BaseModel):  # 가게 테이블
    class Config:
        orm_mode = True
        use_enum_values = True


# category
class Category(str, Enum):
    food = "식당"
    meat = "정육점"
    fish = "생선가게"
    fruit = "과일가게"
    side_dish = "반찬가게"
    clothes = "옷가게"
    etc = "기타"


# store


class Store(StoreBase):
    id: str
    user_id: int
    name: str
    category: Category
    location: Tuple[float, float]
    description: str
    photo_url: str
    is_active: bool


class StoreCreate(StoreBase):
    user_id: int
    category: Category
    description: str
    location: Tuple[float, float]


class StoreRead(StoreBase):
    id: int
    category: Category
    name: str
    photo_url: str
    location: Tuple[float, float]

class StoreSingleRead(StoreBase):
    user_id: int
