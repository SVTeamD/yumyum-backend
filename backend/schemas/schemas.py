from enum import Enum
from typing import Tuple
from pydantic import BaseModel
from datetime import datetime


class UserBase(BaseModel):  # 사용자 테이블
    class Config:
        orm_mode = True


class User(UserBase):
    pass


class UserCreate(UserBase):
    name: str
    gender: str
    age_range: str
    phone_num: str
    user_type: bool


class UserRead(UserCreate):
    id: int


class UserDelete(UserBase):
    is_active: bool


# location


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
    name: str
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

# menu


class MenuBase(BaseModel):
    class Config:
        orm_mode = True


class Menu(MenuBase):  # 메뉴
    name: str
    cost: str  # 잠시 str로 수정
    photo_url: str
    is_active: bool
    is_main_menu: bool


class MenuCreate(MenuBase):
    store_id: int
    # s3_image_url: str
    # name: str
    # cost: int
    # photo_url: str

class MenusCreate(MenuBase):
    store_id: int
    name: str
    cost: str
    photo_url: str

class MenuRead(MenuCreate):
    id: str


class MenuUpdate(MenuBase):
    is_main_menu: bool


class MenuDelete(MenuBase):
    is_active: bool


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
