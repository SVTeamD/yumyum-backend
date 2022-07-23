from typing import List, Union

from pydantic import BaseModel


class MenuBase(BaseModel):
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