from typing import List, Union

from pydantic import BaseModel

class StoreBase(BaseModel): # 가게 테이블
    class Config:
        orm_mode = True


class Store(StoreBase):
    name: str


class StoreCreate(StoreBase):
    name: str


class StoreRead(StoreBase):
    name: str


class MenuBase(BaseModel): # Menu 테이블
    class Config:
        orm_mode = True

class Menu(MenuBase):
    name: str
    cost: int
    photo_url: str
    is_active: bool
    is_main_menu: bool


class MenuCreate(MenuBase):
    store_id: int
    name: str
    cost: int
    photo_url: str

class MenuRead(MenuCreate):
    id: str


class MenuUpdate(MenuBase):
    is_main_menu: bool


class MenuDelete(MenuBase):
    is_active: bool


