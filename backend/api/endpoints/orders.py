from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from starlette.status import HTTP_201_CREATED, HTTP_204_NO_CONTENT

from crud import order_crud
from schemas import order_schema
from api.dep import get_db

router = APIRouter()


# TODO: 에러 처리

# 주문
@router.post("", response_model=order_schema.OrderCreate, status_code=HTTP_201_CREATED)
def create_order_info(order: order_schema.OrderCreate, db: Session = Depends(get_db)):
    return order_crud.create_order(db, order=order)


# 주문 조회
@router.get("", response_model=List[order_schema.Order])
def read_order_info(db: Session = Depends(get_db)):
    orders = order_crud.get_order(db)
    return orders


# 주문 상세 조회
@router.get("/{user_id}")
def read_order_by_id(user_id: int, db: Session = Depends(get_db)):
    order = order_crud.get_order_by_id(db, user_id=user_id)
    return order


# 유저 주문 조회
@router.get("/user/{user_id}")
def read_order_by_user_id(user_id: int, db: Session = Depends(get_db)):
    orders = order_crud.get_order_by_user_id(db, user_id=user_id)
    return orders


# 가게 주문 조회
@router.get("/store/{store_id}")
def read_order_by_store_id(store_id: int, db: Session = Depends(get_db)):
    orders = order_crud.get_order_by_store_id(db, store_id=store_id)
    return orders


# 주문 삭제
@router.delete("/{order_id}", status_code=HTTP_204_NO_CONTENT)
def delete_order_by_id(order_id: int, db: Session = Depends(get_db)):
    order_crud.delete_order_by_id(db, order_id=order_id)

