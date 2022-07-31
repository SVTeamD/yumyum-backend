from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, backref
from sqlalchemy.types import TIMESTAMP
from sqlalchemy.sql import text, func
from sqlalchemy.dialects.mysql import ENUM
from sqlalchemy.types import UserDefinedType

from database import Base



from .user import User


class Coordinates(UserDefinedType):
    def get_col_spec(self):
        return "GEOMETRY"

    def bind_expression(self, bindvalue):
        return func.ST_GeomFromText(bindvalue, type_=self)

    def column_expression(self, col):
        return func.ST_AsText(col, type_=self)

    def bind_processor(self, dialect):
        def process(value):
            if value is None:
                return None
            assert isinstance(value, tuple)
            lat, lng = value
            return "POINT(%s %s)" % (lat, lng)

        return process

    def result_processor(self, dialect, coltype):
        def process(value):
            if value is None:
                return None
                
            lat, lng = value[6:-1].split()
            return (float(lat), float(lng))

        return process



class Store(Base):
    __tablename__ = "stores"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey(User.id))
    location = Column(Coordinates, nullable=False)
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
