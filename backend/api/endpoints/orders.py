from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from crud import order_crud
from schemas import schemas
from api.dep import get_db

router = APIRouter()


# TODO: 에러 처리

# 주문
@router.post("", response_model=schemas.OrderCreate)
def create_order_info(order: schemas.OrderCreate, db: Session = Depends(get_db)):
    return order_crud.create_order(db, order=order)


# 주문 조회
@router.get("", response_model=List[schemas.Order])
def read_order_info(db: Session = Depends(get_db)):
    orders = order_crud.get_order(db)
    return orders


# 주문 상세 조회
@router.get("/{order_id}")
def read_order_by_id(order_id: int, db: Session = Depends(get_db)):
    order = order_crud.get_order_by_id(db, order_id=order_id)
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
@router.delete("/{order_id}")
def delete_order_by_id(order_id: int, db: Session = Depends(get_db)):
    response = order_crud.delete_order_by_id(db, order_id=order_id)
    return response.status_code
