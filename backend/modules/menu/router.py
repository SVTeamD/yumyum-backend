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
from .service import MenuService

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
async def create_menu_info(menu: schemas.MenuCreate, db: Session = Depends(get_db), menu_service: MenuService = Depends(MenuService)):
    return menu_service.create_menu(db, menu = menu)


@router.get("/menus/", response_model=List[schemas.Menu])
async def read_menu_info(skip: int = 1, limit: int = 10, db: Session = Depends(get_db), menu_service: MenuService = Depends(MenuService)):
    menus = await menu_service.get_menu(db)
    return menus


@router.get("/menus/main", response_model=List[schemas.Menu])
async def read_main_menu(skip: int = 1, limit: int = 10, db: Session = Depends(get_db), menu_service: MenuService = Depends(MenuService)):
    menus = menu_service.get_main_menu(db)
    return menus

@router.get("/menus/{menu_id}/")
async def read_menu_by_id(menu_id: int, db: Session = Depends(get_db), menu_service: MenuService = Depends(MenuService)):
    menus = menu_service.get_menu_by_id(db, menu_id = menu_id)
    return menus


@router.get("/menus/name/{menu_name}/")
async def read_menu_by_name(menu_name: str, db: Session = Depends(get_db), menu_service: MenuService = Depends(MenuService)):
    menus = menu_service.get_menu_by_name(db, menu_name = menu_name)
    return menus

@router.put("/menus/main/{menu_id}")
async def update_menu_by_id(menu_id: int, db: Session = Depends(get_db), menu_service: MenuService = Depends(MenuService)):
    response = menu_service.update_main_menu_by_id(db, menu_id = menu_id)
    return response.status_code


@router.delete("/menus/{menu_id}")
async def delete_menu_by_id(menu_id: int, db: Session = Depends(get_db), menu_service: MenuService = Depends(MenuService)):
    response = menu_service.delete_menu_by_id(db, menu_id = menu_id)
    return response.status_code