from typing import List, Union

from pydantic import BaseModel


class MenuBase(BaseModel):
    # id: int
    ...

class Menu(MenuBase):
    name: str
    cost: int
    photo_url: str


class MenuCreate(MenuBase):
    name: str
    cost: int
    photo_url: str


class MenuRead(MenuCreate):
    pass


class MenuDelete(MenuBase):
    pass


    class Config:
        orm_mode = True
