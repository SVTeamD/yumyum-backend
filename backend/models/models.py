from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.orm import relationship, backref
from sqlalchemy.types import TIMESTAMP
from sqlalchemy.sql import text, func
from sqlalchemy.dialects.mysql import ENUM


from .database import Base

from sqlalchemy import func
from sqlalchemy.types import UserDefinedType, Float


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
            return "POINT(%s %s)" % (lng, lat)
        return process

    def result_processor(self, dialect, coltype):
        def process(value):
            if value is None:
                return None
            #m = re.match(r'^POINT\((\S+) (\S+)\)$', value)
            #lng, lat = m.groups()
            lng, lat = value[6:-1].split()  # 'POINT(135.00 35.00)' => ('135.00', '35.00')
            return (float(lat), float(lng))
        return process


class User(Base): # 부모
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)

class Location(Base):
    __tablename__ = "locations"

    id = Column(Integer, primary_key=True, index=True)
    points = Column(Coordinates, nullable=False)



class Store(Base): # 부모
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
    updated_at = Column(TIMESTAMP, server_default=text('CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP'))
    
    user = relationship("User", backref = backref("store", uselist=False))
    menu = relationship("Menu") 
    location = relationship("Location", backref = backref("store", uselist=False))

class Menu(Base):
    __tablename__ = "menus"

    id = Column(Integer, primary_key=True, index=True)
    store_id = Column(Integer, ForeignKey(Store.id)) # Fk1
    name = Column(String(255), index=True)
    cost = Column(Integer)
    photo_url = Column(String(2083))
    is_active = Column(Boolean, nullable=False, default=True)
    is_main_menu = Column(Boolean, nullable=False, default=False)
    created_at = Column(TIMESTAMP, server_default=func.now())
    updated_at = Column(TIMESTAMP, server_default=text('CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP'))
    

class Order(Base): #자식
    __tablename__ = "orders"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey(User.id)) # Fk1
    store_id = Column(Integer, ForeignKey(Store.id)) # Fk2
    datetime = Column(DateTime)
    is_takeout = Column(Boolean, nullable=False)
    cost = Column(Integer)
    is_active = Column(Boolean, nullable=False, default=True)
    created_at = Column(TIMESTAMP, server_default=func.now())
    updated_at = Column(TIMESTAMP, server_default=text('CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP'))

