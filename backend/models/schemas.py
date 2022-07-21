from typing import List, Union

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

# Customer


class CustomerBase(BaseModel):

    class Config:
        orm_mode = True


class Customer(CustomerBase):
    user_id: int
    customer_id: int


class CustomerCreate(CustomerBase):
    pass


class CustomerRead(CustomerBase):
    pass


class CustomerDelete(Customer):
    pass

# Merchant


class MerchantBase(BaseModel):

    class Config:
        orm_mode = True


class Merchant(MerchantBase):
    user_id: int
    merchant_id: int


class MerchantCreate(MerchantBase):
    pass


class MerchantRead(MerchantBase):
    pass


class MerchantDelete(Merchant):
    pass

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


# class MenuUpdate(MenuBase):
    # is_active = bool


class MenuDelete(MenuBase):
    is_active: bool
