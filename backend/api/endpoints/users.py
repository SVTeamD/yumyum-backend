from typing import Any, List

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from starlette.status import HTTP_201_CREATED, HTTP_422_UNPROCESSABLE_ENTITY
from crud import user_crud
from schemas import schemas
from api.dep import get_db

router = APIRouter()


# TODO: 에러 처리

# 유저 생성
@router.post("", response_model=schemas.User, status_code=HTTP_201_CREATED)
def create_user_info(user: schemas.UserCreate, db: Session = Depends(get_db)):
    return user_crud.create_user(db, user=user)


# 유저 상세 조회
@router.get("/{user_id}")
def read_user_by_id(user_id: int, db: Session = Depends(get_db)):
    users = user_crud.get_user_by_id(db, user_id=user_id)
    return users


# 유저 삭제
@router.delete("/{user_id}")
def delete_user_by_id(user_id: int, db: Session = Depends(get_db)):
    response = user_crud.delete_user_by_id(db, user_id=user_id)
    return response.status_code
