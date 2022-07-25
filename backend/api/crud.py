# # User


# def get_user(db: Session, skip: int = 1, limit: int = 10):
#     return db.query(models.User).offset(skip).limit(limit).all()


# def get_user_by_id(db: Session, user_id: int):
#     return db.query(models.User).filter(models.User.user_id == user_id).first()


# def create_user(db: Session, user: schemas.UserCreate):
#     db_user = models.User(user_id=user.user_id,
#                           name=user.name,
#                           gender=user.gender,
#                           age_range=user.age_range,
#                           phone_num=user.phone_num
#                           )
#     db.add(db_user)
#     db.commit()
#     return db_user


# def delete_user(db: Session, user_id: int):
#     user = db.query(models.User).filter_by(
#         models.User.user_id == user_id).first()
#     db.delete(user)
#     db.commit()
#     return Response(status_code=HTTP_204_NO_CONTENT)

# # Store


# def get_store(db: Session, skip: int = 1, limit: int = 10):
#     return db.query(models.Store).offset(skip).limit(limit).all()


# def get_store_by_id(db: Session, store_id, id: int):
#     return db.query(models.Store).filter(models.Store.store_id == store_id).first()


# def create_store(db: Session, store: schemas.StoreCreate, location: schemas.LocationCreate,
#                  merchant_id, menu_id, category_id):
#     db_merchant = db.query(models.Merchant).filter(
#         models.Merchant.merchant_id == merchant_id).first()
#     db_menu = db.query(models.Menu).filter(
#         models.Menu.id == menu_id).first()
#     db_category = db.query(models.Category).filter(
#         models.Category.category_id == category_id).first()
#     # db_location = db.query(models.Location).filter(
#     #     models.Location.location_id == location_id).first()
#     db_location = models.Location(location_id=location.location_id
#                                   #   latitude=location.latitude,
#                                   #   longitude=location.longitude
#                                   )

#     db_store = models.Store(store_id=store.store_id,
#                             merchant_id=db_merchant.mechant_id,
#                             menu_id=db_menu.id,
#                             category_id=db_category.category_id,
#                             location_id=db_location.location_id,
#                             store_name=store.store_name,
#                             store_photo_url=store.store_photo_url
#                             # created_at=store.created_at,
#                             # updated_at=store.updated_at
#                             )
#     db.add(db_store)
#     db.commit()
#     return db_store


# def delete_store(db: Session, store_id: int):
#     store = db.query(models.store).filter_by(
#         models.Store.store_id == store_id).first()
#     db.delete(store)
#     db.commit()
#     return Response(status_code=HTTP_204_NO_CONTENT)

# # order


# def get_order(db: Session, skip: int = 1, limit: int = 10):
#     return db.query(models.Order).offset(skip).limit(limit).all()


# def get_order_by_id(db: Session, order_id: int):
#     return db.query(models.Order).filter(models.Order.order_id == order_id).first()


# def create_order(db: Session, order: schemas.OrderCreate):
#     db_order = models.Order(customer_id=order.customer_id, store_id=order.store_id,
#                             order_datetime=order.order_datetime, order_is_takeout=order.order_is_takeout, order_cost=order.order_cost)
#     db.add(db_order)
#     db.commit()
#     # db.refresh(db_order)
#     return db_order


# def delete_order(db: Session, order_id: int):
#     order = db.query(models.Order).filter_by(
#         models.Order.order_id == order_id).first()
#     db.delete(order)
#     db.commit()
#     return Response(status_code=HTTP_204_NO_CONTENT)

from models import models, schemas
from fastapi import Response
from sqlalchemy.orm import Session
from starlette.responses import Response

# user


def create_user(db: Session, user: schemas.UserCreate):  # 유저 생성
    db_user = models.User()
    db.add(db_user)
    db.commit()
    return db_user


def delete_user_by_id(db: Session, user_id: int):
    user = db.query(models.User).filter(models.User.id ==
                                        user_id).update({'is_active': False})
    db.commit()
    return Response(status_code=HTTP_204_NO_CONTENT)

# store


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


def get_store_menu(db: Session, store_id):  # 메뉴
    menu = db.query(models.Menu).join(models.Store).filter(
        models.Store.id == store_id).filter(models.Menu.is_active == True).all()
    return menu

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
