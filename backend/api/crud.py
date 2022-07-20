from fastapi import Response
from sqlalchemy.orm import Session
from sqlalchemy.sql import func
from starlette.responses import Response
from starlette.status import HTTP_204_NO_CONTENT
import datetime
import sys
sys.path.append("..")
from models import models, schemas

def get_menu(db: Session):
    return db.query(models.Menu).filter(models.Menu.is_active == True).all()


def get_menu_by_id(db: Session, menu_id: int): 
    menu = db.query(models.Menu).filter(models.Menu.is_active == True).filter(models.Menu.id == menu_id).first()
    if (menu):
       return menu
    else:
       return "삭제된 메뉴입니다!"


def get_menu_by_name(db: Session, menu_name: str): 
    menu = db.query(models.Menu).filter(models.Menu.is_active == True).filter(models.Menu.name == menu_name).first()
    if (menu):
        return menu
    else:
        return "삭제된 메뉴입니다!"


def create_menu(db: Session, menu: schemas.MenuCreate): 
    db_menu = models.Menu(name = menu.name, cost = menu.cost, photo_url = menu.photo_url, is_active = True)
    db.add(db_menu)
    db.commit()
    # db.refresh(db_menu)
    return db_menu


def delete_menu_by_id(db: Session, menu_id: int): 
    menu = db.query(models.Menu).filter(models.Menu.id == menu_id).update({'is_active': False })
    db.commit()
    return Response(status_code = HTTP_204_NO_CONTENT)