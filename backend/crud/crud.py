from models import User, Store, Location, Menu, Order
from schemas import schemas
from fastapi import Response
from sqlalchemy.orm import Session
from starlette.responses import Response
from starlette.status import HTTP_201_CREATED, HTTP_204_NO_CONTENT


# user
def get_user_by_id(db: Session, user_id: int):
    user = db.query(User).filter(User.is_active ==
                                        True).filter(User.id == user_id).first()
    if (user):
        return user
    else:
        return "id가 잘못되었습니다"

def create_user(db: Session, user: schemas.UserCreate):  # 유저 생성
    db_user = User(name=user.name,
                          user_type=user.user_type,
                          gender=user.gender,
                          age_range=user.age_range,
                          phone_num=user.phone_num)
    db.add(db_user)
    db.commit()
    return db_user


def delete_user_by_id(db: Session, user_id: int):
    user = db.query(User).filter(User.id ==
                                        user_id).update({'is_active': False})
    db.commit()
    return Response(status_code=HTTP_204_NO_CONTENT)

# user
def get_store(db: Session):  # 가게
    return db.query(Store).all()


def create_store(db: Session, store: schemas.StoreCreate, loc: schemas.LocationCreate):
    location = Location(points=loc.points)
    db.add(location)
    db.commit()
    db_store = Store(user_id=store.user_id,
                            location_id=location.id,
                            name=store.name,
                            category=store.category,
                            description=store.description,
                            photo_url=store.photo_url
                            )

    db.add(db_store)
    db.commit()
    return db_store


def delete_user_by_id(db: Session, user_id: int):
    user = db.query(User).filter(User.id ==
                                        user_id).update({'is_active': False})
    db.commit()
    return Response(status_code=HTTP_204_NO_CONTENT)

# store


def get_store_menu(db: Session, store_id):  # 메뉴
    menu = db.query(Menu).join(Store).filter(
        Store.id == store_id).filter(Menu.is_active == True).all()
    return menu


def delete_store_by_id(db: Session, store_id: int):
    store = db.query(Store).filter(Store.id ==
                                          store_id).update({'is_active': False})
    db.commit()
    return Response(status_code=HTTP_204_NO_CONTENT)

# menu


def get_main_menu(db: Session):
    return db.query(Menu).filter(Menu.is_active == True).filter(Menu.is_main_menu == True).all()


def get_menu_by_id(db: Session, menu_id: int):
    menu = db.query(Menu).filter(Menu.is_active ==
                                        True).filter(Menu.id == menu_id).first()
    if (menu):
        return menu
    else:
        return "삭제된 메뉴입니다!"


def get_menu_by_name(db: Session, menu_name: str):
    menu = db.query(Menu).filter(Menu.is_active ==
                                        True).filter(Menu.name == menu_name).first()
    if (menu):
        return menu
    else:
        return "없는 메뉴입니다"


def create_menu(db: Session, menu: schemas.MenuCreate):
    db_menu = Menu(store_id=menu.store_id,
                          name=menu.name,
                          cost=menu.cost,
                          photo_url=menu.photo_url)
    db.add(db_menu)
    db.commit()
    return db_menu


def update_main_menu_by_id(db: Session, menu_id: int):
    db.query(Menu).filter(Menu.id ==
                                 menu_id).update({'is_main_menu': True})
    db.commit()
    return Response(status_code=HTTP_201_CREATED)


def delete_menu_by_id(db: Session, menu_id: int):
    menu = db.query(Menu).filter(Menu.id ==
                                        menu_id).update({'is_active': False})
    db.commit()
    return Response(status_code=HTTP_204_NO_CONTENT)


def create_order(db: Session, order: schemas.OrderCreate):  # 주문
    db_order = Order(user_id=order.user_id,
                            store_id=order.store_id,
                            datetime=order.datetime,
                            is_takeout=order.is_takeout,
                            cost=order.cost)
    db.add(db_order)
    db.commit()
    return db_order


def get_order(db: Session):  
    return db.query(Order).filter(Order.is_active == True).all()



def get_order_by_id(db: Session, order_id: int):
    order = db.query(Order).filter(Order.is_active ==
                                        True).filter(Order.id == order_id).first()
    if (order):
        return order
    else:
        return "바꾸세요"


def get_order_by_user_id(db: Session, user_id):  # 주문
    order = db.query(Order).join(User).filter(
        User.id == user_id).filter(Order.is_active == True).all()
    if (order):
        return order
    else:
        return "바꾸세요"
    

def get_order_by_store_id(db: Session, store_id):  # 주문
    order = db.query(Order).join(Store).filter(
        Store.id == store_id).filter(Order.is_active == True).all()
    if (order):
        return order
    else:
        return "바꾸세요"


def delete_order_by_id(db: Session, order_id: int):
    order = db.query(Order).filter(Order.id ==
                                          order_id).update({'is_active': False})

    db.commit()
    return Response(status_code=HTTP_204_NO_CONTENT)
