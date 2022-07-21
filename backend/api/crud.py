from models import models, schemas
from fastapi import Response
from sqlalchemy.orm import Session
from sqlalchemy.sql import func
from starlette.responses import Response
from starlette.status import HTTP_204_NO_CONTENT
import datetime
import sys
sys.path.append("..")

# User


def get_user(db: Session, skip: int = 1, limit: int = 10):
    return db.query(models.User).offset(skip).limit(limit).all()


def get_user_by_id(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.user_id == user_id).first()


def create_user(db: Session, user: schemas.UserCreate):
    db_user = models.User(user_id=user.user_id,
                          name=user.name,
                          gender=user.gender,
                          age_range=user.age_range,
                          phone_num=user.phone_num
                          )
    db.add(db_user)
    db.commit()
    return db_user


def delete_user(db: Session, user_id: int):
    user = db.query(models.User).filter_by(
        models.User.user_id == user_id).first()
    db.delete(user)
    db.commit()
    return Response(status_code=HTTP_204_NO_CONTENT)

# Customer


def get_customer(db: Session, skip: int = 1, limit: int = 10):
    return db.query(models.Customer).offset(skip).limit(limit).all()


def get_customer_by_id(db: Session, user_id: int):
    return db.query(models.Customer).filter(models.Customer.user_id == user_id).first()


def create_customer(db: Session, customer: schemas.CustomerCreate, user_id):
    db_user = db.query(models.User).filter(
        models.User.user_id == user_id).first()
    db_customer = models.Customer(user_id=db_user.user_id)
    db.add(db_customer)
    db.commit()
    return db_customer


def delete_customer(db: Session, customer_id: int):
    customer = db.query(models.customer).filter_by(
        models.Customer.customer_id == customer_id).first()
    db.delete(customer)
    db.commit()
    return Response(status_code=HTTP_204_NO_CONTENT)

# Merchant


def get_merchant(db: Session, skip: int = 1, limit: int = 10):
    return db.query(models.Merchant).offset(skip).limit(limit).all()


def get_merchant_by_id(db: Session, merchant_id: int):
    return db.query(models.Merchant).filter(models.Merchant.merchant_id == merchant_id).first()


def create_merchant(db: Session, merchant: schemas.MerchantCreate, user_id):
    db_user = db.query(models.User).filter(
        models.User.user_id == user_id).first()
    db_merchant = models.Merchant(user_id=db_user.user_id)
    db.add(db_merchant)
    db.commit()
    return db_merchant


def delete_merchant(db: Session, merchant_id: int):
    merchant = db.query(models.merchant).filter_by(
        models.Merchant.merchant_id == merchant_id).first()
    db.delete(merchant)
    db.commit()
    return Response(status_code=HTTP_204_NO_CONTENT)

# Menu


def get_menu(db: Session):
    return db.query(models.Menu).filter(models.Menu.is_active == True).all()


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
    db_menu = models.Menu(name=menu.name, cost=menu.cost,
                          photo_url=menu.photo_url, is_active=True)
    db.add(db_menu)
    db.commit()
    # db.refresh(db_menu)
    return db_menu


def delete_menu_by_id(db: Session, menu_id: int):
    menu = db.query(models.Menu).filter(models.Menu.id ==
                                        menu_id).update({'is_active': False})
    db.commit()
    return Response(status_code=HTTP_204_NO_CONTENT)
