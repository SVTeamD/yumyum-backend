from fastapi import Response
from sqlalchemy.orm import Session
from sqlalchemy.sql import func
from starlette.responses import Response
from starlette.status import HTTP_204_NO_CONTENT, HTTP_201_CREATED
import datetime
import sys
sys.path.append("..")
from models import models, schemas

def initialize_category(db: Session):
    categories = ["백반집", "생선가게", "정육점"]
    for category in categories:
        db_category = models.Category(name=category)
        db.add(db_category)
    db.commit()
    print("Category initialization complete!")


def get_store(db: Session): # 가게
    return db.query(models.Store).all()


def create_store(db: Session, store: schemas.StoreCreate, menu_id):
    db_menu = db.query(models.Menu).filter(models.User.menu_id == menu_id).first()
    db_store = models.Store(menu_id = db_menu.menu_id)
    db.add(db_store)
    db.commit()
    return db_store



def get_menu(db: Session): # 메뉴
    return db.query(models.Menu).filter(models.Menu.is_active == True).all()


def get_main_menu(db: Session):
    return db.query(models.Menu).filter(models.Menu.is_active == True).filter(models.Menu.is_main_menu == True).all()


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
    db_menu = models.Menu(name = menu.name,
                          cost = menu.cost, 
                          photo_url = menu.photo_url, 
                          is_active = True, 
                          is_main_menu = False)
    db.add(db_menu)
    db.commit()
    # db.refresh(db_menu)
    return db_menu 


def update_main_menu_by_id(db: Session, menu_id: int):
    menu = db.query(models.Menu).filter(models.Menu.id == menu_id).update({'is_main_menu': True })
    db.commit()
    return Response(status_code=HTTP_201_CREATED)



def delete_menu_by_id(db: Session, menu_id: int): 
    menu = db.query(models.Menu).filter(models.Menu.id == menu_id).update({'is_active': False })
    db.commit()
    return Response(status_code = HTTP_204_NO_CONTENT)