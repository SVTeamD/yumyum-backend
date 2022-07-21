from typing import List, Union

from pydantic import BaseModel


class MenuBase(BaseModel): # 메뉴 테이블
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


class MerchantBase(BaseModel): # merchant 테이블
    id: int
    class Config:
        orm_mode = True

class Merchant(MerchantBase):
    ...

class  MerchantCreate():
    ...

class CategoryBase(BaseModel): # 카테고리 테이블
    id: int
    class Config:
        orm_mode = True

class Category(CategoryBase):
    name: str

class CategoryCreate(Category): 
    pass
    

class CategoryRead(CategoryCreate):
   pass


class StoreBase(BaseModel): # 가게 테이블
    ...
    class Config:
        orm_mode = True


class Store(StoreBase):
    ...


class StoreCreate(BaseModel): 
    merchant_id: int
    menu_id: int
    category_name: str
    location_id: int
    name: str
    photo_url: str

class StoreRead():
    ...

class StoreDelete():
    ...

class LocationBase(BaseModel): # 가게위치 테이블
    ...
    class Config:
        orm_mode = True

class Location(LocationBase):








