# # User
# @app.post("/users/", response_model=schemas.User)
# def create_user_info(user: schemas.UserCreate, db: Session = Depends(get_db)):
#     return crud.create_user(db, user=user)


# @app.get("/users/{user_id}/")
# def read_user_by_id(user_id: int, db: Session = Depends(get_db)):
#     users = crud.get_user_by_id(db, user_id=user_id)
#     return users


# @app.delete("/users/delete/{user_id}/")
# def delete_user_by_id(user_id: str, db: Session = Depends(get_db)):
#     response = crud.delete_user(db, user_id=user_id)
#     return response.status_code

# # Order
# @app.post("/orders/", response_model=schemas.Order)
# def create_order_info(order: schemas.OrderCreate, db: Session = Depends(get_db)):
#     return crud.create_order(db, order=order)


# @app.get("/orders/{order_id}/")
# def read_order_by_id(order_id: int, db: Session = Depends(get_db)):
#     orders = crud.get_order_by_id(db, order_id=order_id)
#     return orders


# @app.delete("/orders/{order_id}/")
# def delete_order_by_name(order_id: int, db: Session = Depends(get_db)):
#     response = crud.delete_order(db, order_id=order_id)
#     return response.status_code
from typing import Union
import uuid

from typing import List
from fastapi import Depends, FastAPI, HTTPException
from fastapi import UploadFile, File
from fastapi.responses import HTMLResponse
from sqlalchemy.orm import Session
from models import models, schemas
from api import crud
from models.database import SessionLocal, engine

from aws.bucket import post_bucket

models.Base.metadata.create_all(bind=engine)


app = FastAPI()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/")
async def main():
    return {"Hello from": "FastAPI"}


@app.post("/upload", status_code=200, description="***** Upload JPG asset to S3 *****")
async def upload(file_object: UploadFile = File(...)):
    file_object.filename = f"{uuid.uuid4()}.jpg"
    content = await file_object.read()
    post_bucket(content, file_object.filename)
    return {"filename": file_object.filename}

# user


@app.post("/users/", response_model=schemas.User)  # 유저 생성
def create_user_info(user: schemas.UserCreate, db: Session = Depends(get_db)):
    return crud.create_user(db, user=user)


@app.get("/users/{user_id}/")
def read_user_by_id(user_id: int, db: Session = Depends(get_db)):
    users = crud.get_user_by_id(db, user_id=user_id)
    return users

# store


@app.post("/stores/", response_model=schemas.Store)
def create_store_info(store: schemas.StoreCreate, loc: schemas.LocationCreate, db: Session = Depends(get_db)):
    return crud.create_store(db, store=store, loc=loc)


@app.get("/stores/", response_model=List[schemas.Store])
def read_store_info(db: Session = Depends(get_db)):
    stores = crud.get_store(db)
    return stores


@app.get("/stores/{store_id}/menus", response_model=List[schemas.Menu])
def read_menu_info(store_id, skip: int = 1, limit: int = 10, db: Session = Depends(get_db)):
    menus = crud.get_store_menu(db, store_id=store_id)
    return menus

# menu


@app.post("/menus/", response_model=schemas.MenuCreate)  # menu api
def create_menu_info(menu: schemas.MenuCreate, db: Session = Depends(get_db)):
    return crud.create_menu(db, menu=menu)


@app.get("/menus/main", response_model=List[schemas.Menu])
def read_main_menu(skip: int = 1, limit: int = 10, db: Session = Depends(get_db)):
    menus = crud.get_main_menu(db)
    return menus


@app.get("/menus/{menu_id}/")
def read_menu_by_id(menu_id: int, db: Session = Depends(get_db)):
    menus = crud.get_menu_by_id(db, menu_id=menu_id)
    return menus


@app.get("/menus/name/{menu_name}/")
def read_menu_by_name(menu_name: str, db: Session = Depends(get_db)):
    menus = crud.get_menu_by_name(db, menu_name=menu_name)
    return menus


@app.put("/menus/main/{menu_id}")
def update_menu_by_id(menu_id: int, db: Session = Depends(get_db)):
    response = crud.update_main_menu_by_id(db, menu_id=menu_id)
    return response.status_code


@app.delete("/menus/{menu_id}")
def delete_menu_by_id(menu_id: int, db: Session = Depends(get_db)):
    response = crud.delete_menu_by_id(db, menu_id=menu_id)
    return response.status_code
