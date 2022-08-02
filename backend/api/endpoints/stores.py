from typing import List
from fastapi import APIRouter, Depends, UploadFile, File, HTTPException, Form
from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session
from starlette.status import HTTP_201_CREATED, HTTP_204_NO_CONTENT, HTTP_422_UNPROCESSABLE_ENTITY
from pydantic import ValidationError

from utils.clova import Clova
from aws.bucket import post_bucket
from crud import store_crud
from schemas import store_schema, menu_schema
from api.dep import get_db

router = APIRouter()
clova = Clova()

async def checker(data: str = Form(...)):
    try:
        model = store_schema.StoreCreate.parse_raw(data)
    except ValidationError as e:
        raise HTTPException(detail=jsonable_encoder(e.errors()), status_code=HTTP_422_UNPROCESSABLE_ENTITY)
        
    return model

# 가게 전체 조회
@router.get("", response_model=List[store_schema.StoreRead])
def read_stores_info(db: Session = Depends(get_db)):
    stores = store_crud.get_store(db)
    return stores


# 가게 생성
@router.post("", status_code=HTTP_201_CREATED, response_model=store_schema.Store)
async def create_store_info(
    store: store_schema.StoreCreate = Depends(checker),
    store_image: UploadFile = File(...),
    db: Session = Depends(get_db),
):
    store = store_crud.create_store(db, store)
    store_content = await store_image.read()
    store_image.filename = f"{store.id}/store/{store.photo_url}"
    post_bucket(store_content, store_image.filename)
    response = await clova.ocr_transform(store_content, "Store")
    if not response.status:
        return HTTPException(status_code=555, detail="Clova OCR API Error")
    return store  

# Get store by user id
@router.get("/stores", response_model=store_schema.Store)
def get_store_info(store: store_schema.StoreSingleRead, db: Session = Depends(get_db)):
    return store_crud.get_store_by_user(db, store=store)

# 특정 가게 메뉴 조회
@router.get("/{store_id}/menus", response_model=List[menu_schema.Menu])
def read_menu_info(
    store_id, skip: int = 1, limit: int = 10, db: Session = Depends(get_db)
):
    menus = store_crud.get_store_menu(db, store_id=store_id)
    return menus



# 가게 삭제
@router.delete("/{store_id}", status_code=HTTP_204_NO_CONTENT)
def delete_store_by_id(store_id: int, db: Session = Depends(get_db)):
    store_crud.delete_store_by_id(db, store_id=store_id)
