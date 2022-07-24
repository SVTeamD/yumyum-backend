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

# # Customer


# @app.post("/customers/{user_id}", response_model=schemas.Customer)
# def create_customer_info(customer: schemas.CustomerCreate, user_id, db: Session = Depends(get_db)):
#     return crud.create_customer(db, user_id=user_id, customer=customer)


# @app.get("/customers/{user_id}/")
# def read_customer_by_id(user_id: int, db: Session = Depends(get_db)):
#     customers = crud.get_customer_by_id(db, user_id=user_id)
#     return customers


# @app.delete("/customers/delete/{customer_id}/")
# def delete_customer_by_id(customer_id: str, db: Session = Depends(get_db)):
#     response = crud.delete_customer(db, customer_id=customer_id)
#     return response.status_code

# # Merchant


# @app.post("/merchants/{user_id}", response_model=schemas.Merchant)
# def create_merchant_info(merchant: schemas.MerchantCreate, user_id, db: Session = Depends(get_db)):
#     return crud.create_merchant(db, user_id=user_id, merchant=merchant)


# @app.get("/merchants/{user_id}/")
# def read_merchant_by_id(user_id: int, db: Session = Depends(get_db)):
#     merchants = crud.get_merchant_by_id(db, user_id=user_id)
#     return merchants


# @app.delete("/merchants/delete/{merchant_id}/")
# def delete_merchant_by_id(merchant_id: str, db: Session = Depends(get_db)):
#     response = crud.delete_merchant(db, merchant_id=merchant_id)
#     return response.status_code

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

# Category


@app.post("/categories/", response_model=schemas.Category)
def create_category_info(category: schemas.CategoryCreate, db: Session = Depends(get_db)):
    return crud.create_category(db, category=category)


@app.get("/categories/{category_id}/")
def read_category_by_id(category_id: int, db: Session = Depends(get_db)):
    categories = crud.get_category_by_id(db, category_id=category_id)
    return categories


@app.delete("/categories/{category_id}/")
def delete_category_by_name(category_id: int, db: Session = Depends(get_db)):
    response = crud.delete_category(db, category_id=category_id)
    return response.status_code

# Location


@app.post("/locations/", response_model=schemas.Location)
def create_location_info(location: schemas.LocationCreate, db: Session = Depends(get_db)):
    return crud.create_location(db, location=location)


@app.get("/locations/{location_id}/")
def read_location_by_id(location_id: int, db: Session = Depends(get_db)):
    locations = crud.get_location_by_id(db, location_id=location_id)
    return locations


@app.delete("/locations/{location_id}/")
def delete_location_by_name(location_id: int, db: Session = Depends(get_db)):
    response = crud.delete_order(db, location_id=location_id)
    return response.status_code

 # Store


@app.post("/customers/{user_id}", response_model=schemas.Customer)
def create_customer_info(customer: schemas.CustomerCreate, user_id, db: Session = Depends(get_db)):
    return crud.create_customer(db, user_id=user_id, customer=customer)

# @app.post("/stores/", response_model=schemas.Store)
# def create_store_info(store: schemas.StoreCreate, db: Session = Depends(get_db)):
#     return crud.create_store(db, store=store)


@app.post("/stores/{merchant_id}/{menu_id}/{category_id}/{location_id}", response_model=schemas.Store)
def create_store_info(store: schemas.StoreCreate, merchant_id, menu_id, category_id, location_id, db: Session = Depends(get_db)):
    return crud.create_store(db, merchant_id=merchant_id, menu_id=menu_id, category_id=category_id, location_id=location_id, store=store)


@app.get("/stores/{store_id}/")
def read_store_by_id(store_id: int, db: Session = Depends(get_db)):
    stores = crud.get_store_by_id(db, store_id=store_id)
    return stores


@app.delete("/stores/{store_id}/")
def delete_store_by_name(store_id: int, db: Session = Depends(get_db)):
    response = crud.delete_store(db, store_id=store_id)
    return response.status_code

# Order


@app.post("/orders/", response_model=schemas.Order)
def create_order_info(order: schemas.OrderCreate, db: Session = Depends(get_db)):
    return crud.create_order(db, order=order)


@app.get("/orders/{order_id}/")
def read_order_by_id(order_id: int, db: Session = Depends(get_db)):
    orders = crud.get_order_by_id(db, order_id=order_id)
    return orders


@app.delete("/orders/{order_id}/")
def delete_order_by_name(order_id: int, db: Session = Depends(get_db)):
    response = crud.delete_order(db, order_id=order_id)
    return response.status_code
