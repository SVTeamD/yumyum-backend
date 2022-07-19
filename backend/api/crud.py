from curses import is_term_resized
from unicodedata import name
from fastapi import Response
from sqlalchemy.orm import Session
from sqlalchemy.sql import func
from starlette.responses import Response
from starlette.status import HTTP_204_NO_CONTENT
import datetime
from . import models, schemas



def get_menu(db: Session): 
    return db.query(models.Menu).all()


def get_menu_by_id(db: Session, menu_id: int): 
    return db.query(models.Menu).filter(models.Menu.id == menu_id).first()


def get_menu_by_name(db: Session, menu_name: str): 
    return db.query(models.Menu).filter(models.Menu.name == menu_name).first()


def create_menu(db: Session, menu: schemas.MenuCreate): 
    db_menu = models.Menu(name=menu.name,cost=menu.cost, photo_url=menu.photo_url)
    db.add(db_menu)
    db.commit()
    db.refresh(db_menu)
    return db_menu



def delete_menu(db: Session, menu_name: str): 
    menu = db.query(models.Menu).filter(models.Menu.name == menu_name).first()
    db.delete(menu)
    db.commit()
    return Response(status_code = HTTP_204_NO_CONTENT)