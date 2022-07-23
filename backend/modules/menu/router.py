from typing import Union
import uuid

from typing import List
from fastapi import Depends, HTTPException, APIRouter
from fastapi import UploadFile, File
from fastapi.responses import HTMLResponse
from sqlalchemy.orm import Session
from .models import menu_model
from .schemas import schemas
from database import engine, get_db
from aws.bucket import post_bucket
from . import service

menu_model.Base.metadata.create_all(bind=engine)
router = APIRouter(tags=["menu"])

@router.get("/")
async def main():
    return {"Hello from": "FastAPI"}

@router.post("/upload", status_code=200, description="***** Upload JPG asset to S3 *****")
async def upload(file_object: UploadFile=File(...)):
    file_object.filename = f"{uuid.uuid4()}.jpg"
    content = await file_object.read()
    post_bucket(content, file_object.filename)
    return {"filename": file_object.filename}    


@router.post("/menus/", response_model = schemas.Menu) 
def create_menu_info(menu: schemas.MenuCreate, db: Session = Depends(get_db)):
    return service.create_menu(db, menu = menu)


@router.get("/menus/", response_model=List[schemas.Menu])
def read_menu_info(skip: int = 1, limit: int = 10, db: Session = Depends(get_db)):
    menus = service.get_menu(db)
    return menus


@router.get("/menus/main", response_model=List[schemas.Menu])
def read_main_menu(skip: int = 1, limit: int = 10, db: Session = Depends(get_db)):
    menus = service.get_main_menu(db)
    return menus

@router.get("/menus/{menu_id}/")
def read_menu_by_id(menu_id: int, db: Session = Depends(get_db)):
    menus = service.get_menu_by_id(db, menu_id = menu_id)
    return menus


@router.get("/menus/name/{menu_name}/")
def read_menu_by_name(menu_name: str, db: Session = Depends(get_db)):
    menus = service.get_menu_by_name(db, menu_name = menu_name)
    return menus

@router.put("/menus/main/{menu_id}")
def update_menu_by_id(menu_id: int, db: Session = Depends(get_db)):
    response = service.update_main_menu_by_id(db, menu_id = menu_id)
    return response.status_code


@router.delete("/menus/{menu_id}")
def delete_menu_by_id(menu_id: int, db: Session = Depends(get_db)):
    response = service.delete_menu_by_id(db, menu_id = menu_id)
    return response.status_code