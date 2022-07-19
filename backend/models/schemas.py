from typing import List, Union

from pydantic import BaseModel


class MenuBase(BaseModel):
    class Config:
        orm_mode = True

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


