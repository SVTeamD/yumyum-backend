from models import User
from schemas import schemas
from fastapi import Response, HTTPException
from sqlalchemy.orm import Session
from starlette.responses import Response
from starlette.status import HTTP_201_CREATED, HTTP_204_NO_CONTENT, HTTP_404_NOT_FOUND


# user
# id로 user 검색
def get_user_by_id(db: Session, user_id: int):
    user = (
        db.query(User).filter(User.is_active == True).filter(User.id == user_id).first()
    )
    if user:
        return user
    else:
        return Response(status_code=HTTP_404_NOT_FOUND)


# user 생성
def create_user(db: Session, user: schemas.UserCreate):  # 유저 생성
    for db_user in db.query(User).filter(User.phone_num == user.phone_num).all():
        if db_user.user_type == user.user_type:
            return HTTPException(status_code=409, detail="중복된 사용자 입니다.")
    db_user = User(
        name=user.name,
        user_type=user.user_type,
        gender=user.gender,
        age_range=user.age_range,
        phone_num=user.phone_num,
    )
    db.add(db_user)
    db.commit()
    return db_user


# user 삭제
def delete_user_by_id(db: Session, user_id: int):
    user = db.query(User).filter(User.id == user_id).update({"is_active": False})
    db.commit()
    return Response(status_code=HTTP_204_NO_CONTENT)
