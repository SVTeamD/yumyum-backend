from typing import List, Union

from decimal import Decimal
from pydantic import BaseModel

# User


class UserBase(BaseModel):
    user_id: int

    class Config:
        orm_mode = True


class User(UserBase):
    name: str
    gender: str
    age_range: str
    phone_num: str
    # created_at: str
    # updated_at: str


class UserCreate(UserBase):
    name: str
    gender: str
    age_range: str
    phone_num: str


class UserRead(User):
    pass


class UserDelete(UserBase):
    pass

# # Customer


# class CustomerBase(BaseModel):

#     class Config:
#         orm_mode = True


# class Customer(CustomerBase):
#     user_id: int
#     customer_id: int


# class CustomerCreate(CustomerBase):
#     pass


# class CustomerRead(CustomerBase):
#     pass


# class CustomerDelete(Customer):
#     pass

# # Merchant


# class MerchantBase(BaseModel):

#     class Config:
#         orm_mode = True


# class Merchant(MerchantBase):
#     user_id: int
#     merchant_id: int


# class MerchantCreate(MerchantBase):
#     pass


# class MerchantRead(MerchantBase):
#     pass


# class MerchantDelete(Merchant):
#     pass

# Menu


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


class MenuDelete(MenuBase):
    is_active: bool

# Category


class CategoryBase(BaseModel):
    category_id: int

    class Config:
        orm_mode = True


class Category(CategoryBase):
    category_name: str


class CategoryCreate(CategoryBase):
    category_name: str


class CategoryRead(CategoryBase):
    pass


class CategoryDelete(CategoryBase):
    pass

# Location


class LocationBase(BaseModel):
    location_id: int

    class Config:
        orm_mode = True


class Location(LocationBase):
    pass
    # latitude: Decimal
    # longitude: Decimal


class LocationCreate(Location):
    pass


class LocationRead(Location):
    pass


class LocationDelete(LocationBase):
    pass

# Store


class StoreBase(BaseModel):

    class Config:
        orm_mode = True


class Store(StoreBase):
    store_id: int
    merchant_id: int
    menu_id: int
    category_id: int
    location_id: int

    store_name: str
    store_photo_url: str


class StoreCreate(StoreBase):
    store_name: str
    store_photo_url: str


class StoreRead(StoreBase):
    pass


class StoreDelete(StoreBase):
    pass

# Order


class OrderBase(BaseModel):
    order_id: int
    customer_id: int
    store_id: int

    class Config:
        orm_mode = True


class Order(OrderBase):
    order_datetime: int
    order_is_takeout: bool
    order_cost: int


class OrderCreate(Order):
    pass


class OrderRead(Order):
    pass


class OrderDelete(Order):
    pass
