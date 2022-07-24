from pydantic import BaseModel
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, DECIMAL
from decimal import Decimal
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


# class Customer(Base):
#     __tablename__ = "customers"

#     customer_id = Column(Integer, primary_key=True, index=True)  # PK
#     user_id = Column(Integer, ForeignKey("users.user_id"), index=True)  # FK1


# class Merchant(Base):
#     __tablename__ = "merchants"

#     merchant_id = Column(Integer, primary_key=True, index=True)  # PK
#     user_id = Column(Integer, ForeignKey("users.user_id"), index=True)  # FK1


class Menu(Base):
    __tablename__ = "menus"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), index=True)
    cost = Column(Integer)
    photo_url = Column(String(2083))
    created_at = Column(TIMESTAMP, server_default=func.now())
    updated_at = Column(TIMESTAMP, server_default=text(
        'CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP'))
    is_active = Column(Boolean, nullable=False)


class Category(Base):
    __tablename__ = "categories"

    category_id = Column(Integer, primary_key=True, index=True)  # PK
    category_name = Column(String(255), index=True)


class Location(Base):
    __tablename__ = "locations"

    location_id = Column(Integer, primary_key=True, index=True)  # PK
    # latitude = Column(DECIMAL, index=True)
    # longitude = Column(DECIMAL, index=True)


class Store(Base):
    __tablename__ = "stores"

    store_id = Column(Integer, primary_key=True, index=True)  # PK
    merchant_id = Column(Integer, ForeignKey(
        "merchants.merchant_id"), index=True)  # FK1
    id = Column(Integer, ForeignKey("menus.id"), index=True)  # FK2
    category_id = Column(Integer, ForeignKey(
        "categories.category_id"), index=True)  # FK3
    location_id = Column(Integer, ForeignKey(
        "locations.location_id"), index=True)  # FK4
    store_name = Column(String(255), index=True)
    store_photo_url = Column(String(255), index=True)
    created_at = Column(TIMESTAMP, server_default=func.now())
    updated_at = Column(TIMESTAMP, server_default=text(
        'CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP'))

    menus = relationship("Menu", backref="store")


class Order(Base):
    __tablename__ = "orders"

    order_id = Column(Integer, primary_key=True, index=True)  # PK
    customer_id = Column(Integer, ForeignKey(
        "customers.customer_id"), index=True)  # FK1
    store_id = Column(Integer, ForeignKey(
        "stores.store_id"), index=True)  # FK2
    order_datetime = Column(Integer)
    order_is_takeout = Column(Boolean)
    order_cost = Column(Integer)
