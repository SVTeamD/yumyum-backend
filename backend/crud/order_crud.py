from urllib import response
from models import User, Store, Order
from schemas import schemas
from fastapi import Response
from sqlalchemy.orm import Session
from starlette.responses import Response
from starlette.status import HTTP_201_CREATED, HTTP_204_NO_CONTENT, HTTP_404_NOT_FOUND


# 주문 생성
def create_order(db: Session, order: schemas.OrderCreate):
    db_order = Order(
        user_id=order.user_id,
        store_id=order.store_id,
        datetime=order.datetime,
        is_takeout=order.is_takeout,
        cost=order.cost,
    )
    db.add(db_order)
    db.commit()
    return db_order


# 모든 주문 조회
def get_order(db: Session):
    return db.query(Order).filter(Order.is_active == True).all()


# order id 로 주문 조회
def get_order_by_id(db: Session, order_id: int):
    order = (
        db.query(Order)
        .filter(Order.is_active == True)
        .filter(Order.id == order_id)
        .first()
    )
    if order:
        return order
    else:
        return Response(status_code=HTTP_404_NOT_FOUND)


# user id로 주문 조회
def get_order_by_user_id(db: Session, user_id):  # 주문
    order = (
        db.query(Order)
        .join(User)
        .filter(User.id == user_id)
        .filter(Order.is_active == True)
        .all()
    )
    if order:
        return order
    else:
        return Response(status_code=HTTP_404_NOT_FOUND)


# 가게 아이디로 주문 조회
def get_order_by_store_id(db: Session, store_id):  # 주문
    order = (
        db.query(Order)
        .join(Store)
        .filter(Store.id == store_id)
        .filter(Order.is_active == True)
        .all()
    )
    if order:
        return order
    else:
        return Response(status_code=HTTP_404_NOT_FOUND)


# 주문 삭제
def delete_order_by_id(db: Session, order_id: int):
    order = db.query(Order).filter(Order.id == order_id).update({"is_active": False})

    db.commit()
    return Response(status_code=HTTP_204_NO_CONTENT)
