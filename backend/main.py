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

# User


@app.post("/users/", response_model=schemas.User)
def create_user_info(user: schemas.UserCreate, db: Session = Depends(get_db)):
    return crud.create_user(db, user=user)


@app.get("/users/{user_id}/")
def read_user_by_id(user_id: int, db: Session = Depends(get_db)):
    users = crud.get_user_by_id(db, user_id=user_id)
    return users


@app.delete("/users/delete/{user_id}/")
def delete_user_by_id(user_id: str, db: Session = Depends(get_db)):
    response = crud.delete_user(db, user_id=user_id)
    return response.status_code

# Customer


@app.post("/customers/{user_id}", response_model=schemas.Customer)
def create_customer_info(customer: schemas.CustomerCreate, user_id, db: Session = Depends(get_db)):
    return crud.create_customer(db, user_id=user_id, customer=customer)


@app.get("/customers/{user_id}/")
def read_customer_by_id(user_id: int, db: Session = Depends(get_db)):
    customers = crud.get_customer_by_id(db, user_id=user_id)
    return customers


@app.delete("/customers/delete/{customer_id}/")
def delete_customer_by_id(customer_id: str, db: Session = Depends(get_db)):
    response = crud.delete_customer(db, customer_id=customer_id)
    return response.status_code

# Merchant


@app.post("/merchants/{user_id}", response_model=schemas.Merchant)
def create_merchant_info(merchant: schemas.MerchantCreate, user_id, db: Session = Depends(get_db)):
    return crud.create_merchant(db, user_id=user_id, merchant=merchant)


@app.get("/merchants/{user_id}/")
def read_merchant_by_id(user_id: int, db: Session = Depends(get_db)):
    merchants = crud.get_merchant_by_id(db, user_id=user_id)
    return merchants


@app.delete("/merchants/delete/{merchant_id}/")
def delete_merchant_by_id(merchant_id: str, db: Session = Depends(get_db)):
    response = crud.delete_merchant(db, merchant_id=merchant_id)
    return response.status_code

# Menu


@app.post("/menus/", response_model=schemas.Menu)
def create_menu_info(menu: schemas.MenuCreate, db: Session = Depends(get_db)):
    return crud.create_menu(db, menu=menu)


@app.get("/menus/", response_model=List[schemas.Menu])
def read_menu_info(skip: int = 1, limit: int = 10, db: Session = Depends(get_db)):
    menus = crud.get_menu(db)
    return menus


@app.get("/menus/{menu_id}/")
def read_menu_by_id(menu_id: int, db: Session = Depends(get_db)):
    menus = crud.get_menu_by_id(db, menu_id=menu_id)
    return menus


@app.get("/menus/name/{menu_name}/")
def read_menu_by_name(menu_name: str, db: Session = Depends(get_db)):
    menus = crud.get_menu_by_name(db, menu_name=menu_name)
    return menus


@app.delete("/menus/{menu_id}")
def delete_menu_by_id(menu_id: int, db: Session = Depends(get_db)):
    response = crud.delete_menu_by_id(db, menu_id=menu_id)
    return response.status_code
