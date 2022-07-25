<<<<<<< HEAD
from models import models, schemas
from fastapi import Response
from sqlalchemy.orm import Session
from starlette.responses import Response
from starlette.status import HTTP_201_CREATED, HTTP_204_NO_CONTENT


=======
>>>>>>> UserCusMer
# user


def get_user_by_id(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()


def create_user(db: Session, user: schemas.UserCreate):  # 유저 생성
    db_user = models.User(name=user.name,
                          user_type=user.user_type,
                          gender=user.gender,
                          age_range=user.age_range,
                          phone_num=user.phone_num)
    db.add(db_user)
    db.commit()
    return db_user


def delete_user_by_id(db: Session, user_id: int):
    user = db.query(models.User).filter(models.User.id ==
                                        user_id).update({'is_active': False})
    db.commit()
    return Response(status_code=HTTP_204_NO_CONTENT)

# user


def get_store(db: Session):  # 가게
    return db.query(models.Store).all()


def create_store(db: Session, store: schemas.StoreCreate, loc: schemas.LocationCreate):
    location = models.Location(points=loc.points)
    db.add(location)
    db.commit()
    db_store = models.Store(user_id=store.user_id,
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
    user = db.query(models.User).filter(models.User.id ==
                                        user_id).update({'is_active': False})
    db.commit()
    return Response(status_code=HTTP_204_NO_CONTENT)

# store



def get_store_menu(db: Session, store_id):  # 메뉴
    menu = db.query(models.Menu).join(models.Store).filter(
        models.Store.id == store_id).filter(models.Menu.is_active == True).all()
    return menu


def delete_store_by_id(db: Session, store_id: int):
    store = db.query(models.Store).filter(models.Store.id ==
                                          store_id).update({'is_active': False})
    db.commit()
    return Response(status_code=HTTP_204_NO_CONTENT)

# menu

def get_main_menu(db: Session):
    return db.query(models.Menu).filter(models.Menu.is_active == True).filter(models.Menu.is_main_menu == True).all()


def get_menu_by_id(db: Session, menu_id: int):
    menu = db.query(models.Menu).filter(models.Menu.is_active ==
                                        True).filter(models.Menu.id == menu_id).first()
    if (menu):
        return menu
    else:
        return "삭제된 메뉴입니다!"


def get_menu_by_name(db: Session, menu_name: str):
    menu = db.query(models.Menu).filter(models.Menu.is_active ==
                                        True).filter(models.Menu.name == menu_name).first()
    if (menu):
        return menu
    else:
        return "삭제된 메뉴입니다!"


def create_menu(db: Session, menu: schemas.MenuCreate):
    db_menu = models.Menu(store_id=menu.store_id,
                          name=menu.name,
                          cost=menu.cost,
                          photo_url=menu.photo_url)
    db.add(db_menu)
    db.commit()
    return db_menu


def update_main_menu_by_id(db: Session, menu_id: int):
    db.query(models.Menu).filter(models.Menu.id ==
                                 menu_id).update({'is_main_menu': True})
    db.commit()
    return Response(status_code=HTTP_201_CREATED)


def delete_menu_by_id(db: Session, menu_id: int):
    menu = db.query(models.Menu).filter(models.Menu.id ==
                                        menu_id).update({'is_active': False})
    db.commit()
    return Response(status_code=HTTP_204_NO_CONTENT)

# order


def get_main_order(db: Session):
    return db.query(models.Order).filter(models.Order.is_active == True).filter(models.Order.is_main_order == True).all()


def get_order_by_id(db: Session, order_id: int):
    order = db.query(models.Order).filter(models.Order.is_active ==
                                          True).filter(models.Order.id == order_id).first()
    if (order):
        return order
    else:
        return "삭제된 주문입니다!"


def create_order(db: Session, order: schemas.OrderCreate):
    db_order = models.Order(user_id=order.user_id,
                            store_id=order.store_id,
                            datetime=order.datetime,
                            is_takeout=order.is_takeout,
                            cost=order.cost)
    db.add(db_order)
    db.commit()
    return db_order


def delete_order_by_id(db: Session, order_id: int):
    order = db.query(models.Order).filter(models.Order.id ==
                                          order_id).update({'is_active': False})

    db.commit()
    return Response(status_code=HTTP_204_NO_CONTENT)
