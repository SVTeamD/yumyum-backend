from pydantic import BaseModel
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.types import TIMESTAMP
from sqlalchemy.sql import text, func



from .database import Base


class Store(Base):
    __tablename__ = "Stores"

    id = Column(Integer, primary_key=True, index=True)
    store_name = Column(String(100))

class Menu(Base):
    __tablename__ = "menus"

    id = Column(Integer, primary_key=True, index=True)
    store_id = Column(Integer, ForeignKey(Store.id)) # Fk1
    name = Column(String(255), index=True)
    cost = Column(Integer)
    photo_url = Column(String(2083))
    created_at = Column(TIMESTAMP, server_default=func.now())
    updated_at = Column(TIMESTAMP, server_default=text('CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP'))
    is_active = Column(Boolean, nullable=False)
    is_main_menu = Column(Boolean, nullable=False)

