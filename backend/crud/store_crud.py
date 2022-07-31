from typing import List
from models import User, Store, Menu
from schemas import schemas
from uuid import uuid4
from fastapi import Response
from sqlalchemy.orm import Session
from starlette.responses import Response
from starlette.status import HTTP_204_NO_CONTENT, HTTP_425_TOO_EARLY


# 가게 메뉴 정보 받기
def get_store_menu(db: Session, store_id):  # 메뉴
    menu = (
        db.query(Menu)
        .join(Store)
        .filter(Store.id == store_id)
        .filter(Menu.is_active == True)
        .all()
    )
    return menu


# 가게 전체 조회
def get_store(db: Session) -> List[Store]:  # 가게
    return db.query(Store).filter(Store.is_active == True).all()


async def get_store_by_user(db: Session, store: schemas.StoreSingleRead):
    store_user = db.query(Store).join(User).filter(User.id == store.user_id).filter(User.is_active == True).first()
    if store_user:
        return store_user 
    return HTTP_425_TOO_EARLY

# 가게 생성 (location table)
def create_store(db: Session, store: schemas.StoreCreate) -> Store:
    db_store = Store(
        user_id=store.user_id,
        location=store.location,
        name=store.name,
        category=store.category,
        description=store.description,
        photo_url=f"{uuid4()}.jpg",
    )

    db.add(db_store)
    db.commit()
    return db_store


# 가게 삭제
def delete_store_by_id(db: Session, store_id: int) -> Response:
    store = db.query(Store).filter(Store.id == store_id).update({"is_active": False})
    db.commit()
    return Response(status_code=HTTP_204_NO_CONTENT)
