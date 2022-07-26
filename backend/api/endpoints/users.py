from typing import Any, List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from crud import crud
from schemas import schemas
from api.dep import get_db

router = APIRouter()


# TODO: 에러 처리

# 유저 생성
@router.post("", response_model=schemas.User)
def create_user_info(user: schemas.UserCreate, db: Session = Depends(get_db)):
    return crud.create_user(db, user=user)


# 유저 상세 조회
@router.get("/{user_id}")
def read_user_by_id(user_id: int, db: Session = Depends(get_db)):
    users = crud.get_user_by_id(db, user_id=user_id)
    return users


# 유저 삭제
@router.delete("/{user_id}")
def delete_user_by_id(user_id: int, db: Session = Depends(get_db)):
    response = crud.delete_user_by_id(db, user_id=user_id)
    return response.status_code