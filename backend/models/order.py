from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.orm import relationship, backref
from sqlalchemy.types import TIMESTAMP
from sqlalchemy.sql import text, func
from sqlalchemy.dialects.mysql import ENUM


from database import Base

from sqlalchemy import func

from .user import User
from .store import Store


class Order(Base):  # 자식
    __tablename__ = "orders"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey(User.id))  # Fk1
    store_id = Column(Integer, ForeignKey(Store.id))  # Fk2
    datetime = Column(DateTime)
    is_takeout = Column(Boolean, nullable=False)
    cost = Column(Integer)
    is_active = Column(Boolean, nullable=False, default=True)
    created_at = Column(TIMESTAMP, server_default=func.now())
    updated_at = Column(
        TIMESTAMP, server_default=text("CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP")
    )
