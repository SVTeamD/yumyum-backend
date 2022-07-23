from fastapi import Response
from sqlalchemy.orm import Session
from sqlalchemy.sql import func
from starlette.responses import Response
from starlette.status import HTTP_204_NO_CONTENT, HTTP_201_CREATED

from .models.menu_model import Menu
from .schemas import schemas

import sys
sys.path.append("..")

class MenuService:
    async def get_menu(self, db: Session):
        return db.query(Menu).filter(Menu.is_active == True).all()


    async def get_main_menu(self, db: Session):
        return db.query(Menu).filter(Menu.is_active == True).filter(Menu.is_main_menu == True).all()


    async def get_menu_by_id(self, db: Session, menu_id: int): 
        menu = db.query(Menu).filter(Menu.is_active == True).filter(Menu.id == menu_id).first()
        if (menu):
            return menu
        else:
            return "삭제된 메뉴입니다!"


    async def get_menu_by_name(self, db: Session, menu_name: str): 
        menu = db.query(Menu).filter(Menu.is_active == True).filter(Menu.name == menu_name).first()
        if (menu):
            return menu
        else:
            return "삭제된 메뉴입니다!"


    async def create_menu(self, db: Session, menu: schemas.MenuCreate): 
        db_menu = Menu(name = menu.name, cost = menu.cost, photo_url = menu.photo_url, is_active = True, is_main_menu = False)
        db.add(db_menu)
        db.commit()
        # db.refresh(db_menu)
        return db_menu 

    async def update_main_menu_by_id(self, db: Session, menu_id: int):
        menu = db.query(Menu).filter(Menu.id == menu_id).update({'is_main_menu': True })
        db.commit()
        return Response(status_code=HTTP_201_CREATED)

    async def delete_menu_by_id(self, db: Session, menu_id: int): 
        menu = db.query(Menu).filter(Menu.id == menu_id).update({'is_active': False })
        db.commit()
        return Response(status_code = HTTP_204_NO_CONTENT)