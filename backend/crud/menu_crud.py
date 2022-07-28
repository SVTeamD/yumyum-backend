from models import User, Store, Location, Menu, Order
from schemas import schemas
from fastapi import Response
from sqlalchemy.orm import Session
from starlette.responses import Response
from starlette.status import HTTP_201_CREATED, HTTP_204_NO_CONTENT





# 메인 메뉴 조회
def get_main_menu(db: Session):
    return db.query(Menu).filter(Menu.is_active == True).filter(Menu.is_main_menu == True).all()


# 아이디로 메뉴 조회
def get_menu_by_id(db: Session, menu_id: int):
    menu = db.query(Menu).filter(Menu.is_active ==
                                        True).filter(Menu.id == menu_id).first()
    if (menu):
        return menu
    else:
        return "없는 메뉴입니다!"


# 이름으로 메뉴 조회 (elastic search)
def get_menu_by_name(db: Session, menu_name: str):
    menu = db.query(Menu).filter(Menu.is_active ==
                                        True).filter(Menu.name == menu_name).first()
    if (menu):
        return menu
    else:
        return "없는 메뉴입니다"


# 메뉴 생성
def create_menu(db: Session, name: str, cost: str, menu: schemas.MenuCreate):
    db_menu = Menu(store_id=menu.store_id,
                          name=name,
                          cost=cost,
                          photo_url="")
    db.add(db_menu)
    db.commit()
    return db_menu


# 메인 메뉴로 만들어주기
def update_main_menu_by_id(db: Session, menu_id: int):
    db.query(Menu).filter(Menu.id ==
                                 menu_id).update({'is_main_menu': True})
    db.commit()
    return Response(status_code=HTTP_201_CREATED)


# 메뉴 삭제
def delete_menu_by_id(db: Session, menu_id: int):
    menu = db.query(Menu).filter(Menu.id ==
                                        menu_id).update({'is_active': False})
    db.commit()
    return Response(status_code=HTTP_204_NO_CONTENT)
