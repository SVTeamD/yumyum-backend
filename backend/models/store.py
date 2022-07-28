from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.orm import relationship, backref
from sqlalchemy.types import TIMESTAMP
from sqlalchemy.sql import text, func
from sqlalchemy.dialects.mysql import ENUM


from database import Base

from sqlalchemy import func
from sqlalchemy.types import UserDefinedType, Float

from .user import User
from .location import Location


class Store(Base):
    __tablename__ = "stores"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey(User.id))
    location_id = Column(Integer, ForeignKey(Location.id))

    name = Column(String(100))
    category = Column(ENUM("식당", "생선가게", "정육점", "과일가게", "반찬가게", "옷가게", "기타"))
    description = Column(String(255))
    photo_url = Column(String(255))
    is_active = Column(Boolean, nullable=False, default=True)
    created_at = Column(TIMESTAMP, server_default=func.now())
    updated_at = Column(
        TIMESTAMP, server_default=text("CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP")
    )

    user = relationship("User", backref=backref("store", uselist=False))
    menu = relationship("Menu")
    location = relationship("Location", backref=backref("store", uselist=False))
