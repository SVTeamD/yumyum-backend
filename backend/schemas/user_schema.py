from pydantic import BaseModel


class UserBase(BaseModel): 
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

