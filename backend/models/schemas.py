from typing import List, Union

from pydantic import BaseModel





class StoreBase(BaseModel): # 가게 테이블
    id: int
    class Config:
        orm_mode = True


class Store(StoreBase):
    name = str


class StoreCreate(StoreBase):
    name = str


class StoreRead(StoreCreate):
    pass


class MenuBase(BaseModel): # Menu 테이블
    id: int
    class Config:
        orm_mode = True

class Menu(MenuBase):
    name: str
    cost: int
    photo_url: str
    is_active: bool
    is_main_menu: bool


class MenuCreate(MenuBase):
    name: str
    cost: int
    photo_url: str
    is_active: bool
    is_main_menu: bool

class MenuRead(MenuCreate):
    pass


class MenuUpdate(MenuBase):
    is_main_menu: bool


class MenuDelete(MenuBase):
    is_active: bool


