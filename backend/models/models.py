from pydantic import BaseModel
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.types import TIMESTAMP
from sqlalchemy.sql import text, func


from .database import Base


class User(Base):
    __tablename__ = "users"

    user_id = Column(Integer, primary_key=True, index=True)  # PK
    name = Column(String(255), index=True)
    gender = Column(String(255), index=True)
    age_range = Column(String(255), index=True)
    phone_num = Column(Integer)
    created_date = Column(Integer)
    created_at = Column(TIMESTAMP, server_default=func.now())
    updated_at = Column(TIMESTAMP, server_default=text(
        'CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP'))


class Customer(Base):
    __tablename__ = "customers"

    customer_id = Column(Integer, primary_key=True, index=True)  # PK
    user_id = Column(Integer, ForeignKey("users.user_id"), index=True)  # FK1


class Merchant(Base):
    __tablename__ = "merchants"

    merchant_id = Column(Integer, primary_key=True, index=True)  # PK
    user_id = Column(Integer, ForeignKey("users.user_id"), index=True)  # FK1


class Menu(Base):
    __tablename__ = "menus"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), index=True)
    cost = Column(Integer)
    photo_url = Column(String(2083))
    created_at = Column(TIMESTAMP, server_default=func.now())
    updated_at = Column(TIMESTAMP, server_default=text('CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP'))
    is_active = Column(Boolean, nullable=False)
    is_main_menu = Column(Boolean, nullable=False)
