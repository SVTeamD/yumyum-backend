from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.orm import relationship, backref
from sqlalchemy.types import TIMESTAMP
from sqlalchemy.sql import text, func


from database import Base

from sqlalchemy import func
from .store import Store


class Menu(Base):
    __tablename__ = "menus"

    id = Column(Integer, primary_key=True, index=True)
    store_id = Column(Integer, ForeignKey(Store.id))  # Fk1
    name = Column(String(255), index=True)
    cost = Column(String(255))  # 짐시 문자형으로 수정
    photo_url = Column(String(2083))
    is_active = Column(Boolean, nullable=False, default=True)
    is_main_menu = Column(Boolean, nullable=False, default=False)
    created_at = Column(TIMESTAMP, server_default=func.now())
    updated_at = Column(
        TIMESTAMP, server_default=text("CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP")
    )
