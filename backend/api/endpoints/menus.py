from typing import List

from fastapi import APIRouter, Depends, HTTPException, UploadFile, File, Form
from starlette.status import HTTP_201_CREATED, HTTP_422_UNPROCESSABLE_ENTITY
from fastapi.encoders import jsonable_encoder
from pydantic import ValidationError
from sqlalchemy.orm import Session

from crud import menu_crud, store_crud
from schemas import schemas
from api.dep import get_db

from utils.clova import Clova
from aws.bucket import post_bucket

router = APIRouter()
clova = Clova()

async def checker(data: str = Form(...)):
    try:
        model = schemas.StoreSingleRead.parse_raw(data)
    except ValidationError as e:
        raise HTTPException(detail=jsonable_encoder(e.errors()), status_code=HTTP_422_UNPROCESSABLE_ENTITY)
        
    return model

@router.post("", status_code=HTTP_201_CREATED)
async def create_menu_info(
    menu: schemas.StoreSingleRead = Depends(checker),
    menu_image: UploadFile = File(...),
    db: Session = Depends(get_db)
):
    store = await store_crud.get_store_by_user(db, store=menu)
    menu_content = await menu_image.read()
    menu_image.filename = f"{store.id}/menu/{store.photo_url}"
    post_bucket(menu_content, menu_image.filename)
    response = clova.ocr_transform(menu_content)
    if not response.status:
        return HTTPException(status_code=555, detail="Clova OCR API Error")
    
    return menu_crud.create_menus(db, store, response.data)



# 메인 메뉴 정보 조회
@router.get("/main", response_model=List[schemas.Menu])
def read_main_menu(db: Session = Depends(get_db)):
    menus = menu_crud.get_main_menu(db)
    return menus


# 메뉴 상세 조회
@router.get("/{menu_id}")
def read_menu_by_id(menu_id: int, db: Session = Depends(get_db)):
    menus = menu_crud.get_menu_by_id(db, menu_id=menu_id)
    return menus


# 메뉴 이름으로 검색
@router.get("/name/{menu_name}")
def read_menu_by_name(menu_name: str, db: Session = Depends(get_db)):
    menus = menu_crud.get_menu_by_name(db, menu_name=menu_name)
    return menus


# 메인 메뉴 만들어주기
@router.put("/main/{menu_id}")
def update_menu_by_id(menu_id: int, db: Session = Depends(get_db)):
    response = menu_crud.update_main_menu_by_id(db, menu_id=menu_id)
    return response.status_code


# 메뉴 삭제
@router.delete("/{menu_id}")
def delete_menu_by_id(menu_id: int, db: Session = Depends(get_db)):
    response = menu_crud.delete_menu_by_id(db, menu_id=menu_id)
    return response.status_code
