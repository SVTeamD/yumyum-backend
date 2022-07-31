from unicodedata import category
from models import User, Store, Location, Menu, Order
from schemas import schemas
from uuid import uuid4
from fastapi import Response
from sqlalchemy.orm import Session
from starlette.responses import Response
from starlette.status import HTTP_204_NO_CONTENT


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
def get_store(db: Session):  # 가게
    querysets = (
        db.query(*[Store, Location])
        .join(Location)
        .filter(Location.id == Store.location_id)
        .all()
    )
    objects = list()
    for queryset in querysets:
        store, loc = queryset
        print(store.id, loc.points)
        objects.append(
            schemas.StoreRead(
                id=store.id,
                name=store.name,
                category=store.category,
                photo_url=store.photo_url,
                points=loc.points,
            )
        )
    return objects


# 가게 생성 (location table)
def create_store(db: Session, store: schemas.StoreCreate):
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
def delete_store_by_id(db: Session, store_id: int):
    store = db.query(Store).filter(Store.id == store_id).update({"is_active": False})
    db.commit()
    return Response(status_code=HTTP_204_NO_CONTENT)
