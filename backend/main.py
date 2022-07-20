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


@app.post("/menus/", response_model = schemas.Menu) 
def create_menu_info(menu: schemas.MenuCreate, db: Session = Depends(get_db)):
    return crud.create_menu(db, menu = menu)


@app.get("/menus/", response_model=List[schemas.Menu])
def read_menu_info(skip: int = 1, limit: int = 10, db: Session = Depends(get_db)):
    menus = crud.get_menu(db)
    return menus


@app.get("/menus/{menu_id}/")
def read_menu_by_id(menu_id: int, db: Session = Depends(get_db)):
    menus = crud.get_menu_by_id(db, menu_id = menu_id)
    return menus


@app.get("/menus/name/{menu_name}/")
def read_menu_by_name(menu_name: str, db: Session = Depends(get_db)):
    menus = crud.get_menu_by_name(db, menu_name = menu_name)
    return menus


@app.delete("/menus/{menu_id}")
def delete_menu_by_id(menu_id: int, db: Session = Depends(get_db)):
    response = crud.delete_menu_by_id(db, menu_id = menu_id)
    return response.status_code