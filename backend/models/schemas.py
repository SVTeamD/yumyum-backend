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


class MenuCreate(MenuBase):
    name: str
    cost: int
    photo_url: str
    is_active: bool


class MenuRead(MenuCreate):
    is_active: bool


#class MenuUpdate(MenuBase):
    # is_active = bool


class MenuDelete(MenuBase):
    is_active: bool


