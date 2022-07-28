from typing import Any, List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from crud import store_crud
from schemas import schemas
from api.dep import get_db

router = APIRouter()


# TODO: 에러 처리

# 가게 전체 조회
@router.get("", response_model=List[schemas.StoreRead])
def read_store_info(db: Session = Depends(get_db)):
    stores = store_crud.get_store(db)
    return stores


# 가게 생성
@router.post("", response_model=schemas.Store)
def create_store_info(
    store: schemas.StoreCreate,
    loc: schemas.LocationCreate,
    db: Session = Depends(get_db),
):
    return store_crud.create_store(db, store=store, loc=loc)


# TODO: 추가 하기
# @router.get("/stores/{store_id}", response_model=List[schemas.Store])
# def read_store_info(db: Session = Depends(get_db)):
#     stores = crud.get_store(db)
#     return stores

# 특정 가게 메뉴 조회
@router.get("/{store_id}/menus", response_model=List[schemas.Menu])
def read_menu_info(
    store_id, skip: int = 1, limit: int = 10, db: Session = Depends(get_db)
):
    menus = store_crud.get_store_menu(db, store_id=store_id)
    return menus


# 가게 삭제
@router.delete("/{store_id}")
def delete_store_by_id(store_id: int, db: Session = Depends(get_db)):
    response = store_crud.delete_store_by_id(db, store_id=store_id)
    return response.status_code
