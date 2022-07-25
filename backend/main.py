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
async def upload(file_object: UploadFile=File(...)):
    file_object.filename = f"{uuid.uuid4()}.jpg"
    content = await file_object.read()
    post_bucket(content, file_object.filename)
    return {"filename": file_object.filename}    


@app.post("/users/", response_model=schemas.User) #유저 생성
def create_user_info(user: schemas.UserCreate, db: Session = Depends(get_db)):
    return crud.create_user(db, user = user)



@app.post("/stores/", response_model = schemas.Store)
def create_store_info(store: schemas.StoreCreate, loc: schemas.LocationCreate, db: Session = Depends(get_db)):
    return crud.create_store(db, store = store, loc = loc)


@app.get("/stores/", response_model = List[schemas.Store])
def read_store_info(db: Session = Depends(get_db)):
    stores = crud.get_store(db)
    return stores


@app.get("/stores/{store_id}/menus", response_model = List[schemas.Menu])
def read_menu_info(store_id, skip: int = 1, limit: int = 10, db: Session = Depends(get_db)):
    menus = crud.get_store_menu(db, store_id = store_id)
    return menus

@app.delete("/stores/{store_id}")
def delete_store_by_id(store_id: int, db: Session = Depends(get_db)):
    response = crud.delete_store_by_id(db, store_id = store_id)
    return response.status_code


@app.post("/menus/", response_model = schemas.MenuCreate) # menu api
def create_menu_info(menu: schemas.MenuCreate, db: Session = Depends(get_db)):
    return crud.create_menu(db, menu = menu)


@app.get("/menus/main", response_model=List[schemas.Menu])
def read_main_menu(skip: int = 1, limit: int = 10, db: Session = Depends(get_db)):
    menus = crud.get_main_menu(db)
    return menus

@app.get("/menus/{menu_id}/")
def read_menu_by_id(menu_id: int, db: Session = Depends(get_db)):
    menus = crud.get_menu_by_id(db, menu_id = menu_id)
    return menus


@app.get("/menus/name/{menu_name}/")
def read_menu_by_name(menu_name: str, db: Session = Depends(get_db)):
    menus = crud.get_menu_by_name(db, menu_name = menu_name)
    return menus

@app.put("/menus/main/{menu_id}")
def update_menu_by_id(menu_id: int, db: Session = Depends(get_db)):
    response = crud.update_main_menu_by_id(db, menu_id = menu_id)
    return response.status_code


@app.delete("/menus/{menu_id}")
def delete_menu_by_id(menu_id: int, db: Session = Depends(get_db)):
    response = crud.delete_menu_by_id(db, menu_id = menu_id)
    return response.status_code

@app.post("/orders/", response_model = schemas.OrderCreate) # order
def create_order_info(order: schemas.OrderCreate, db: Session = Depends(get_db)):
    return crud.create_order(db, order = order)

@app.get("/orders/", response_model=List[schemas.Order])
def read_order_info(skip: int = 1, limit: int = 10, db: Session = Depends(get_db)):
    orders = crud.get_order(db)
    return orders

@app.get("/users/{user_id}/orders", response_model = List[schemas.Order])
def read_user_order_info(user_id, skip: int = 1, limit: int = 10, db: Session = Depends(get_db)):
    orders = crud.get_user_order(db, user_id = user_id)
    return orders

@app.get("/stores/{store_id}/orders", response_model = List[schemas.Order])
def read_store_menu_info(store_id, skip: int = 1, limit: int = 10, db: Session = Depends(get_db)):
    orders = crud.get_store_menu(db, store_id = store_id)
    return orders 