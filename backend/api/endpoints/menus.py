from typing import Any, List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from crud import menu_crud
from schemas import schemas
from api.dep import get_db

from utils.clova import Clova

router = APIRouter()


# TODO: 에러 처리

# 메뉴 생성
@router.post("")  # menu api
def create_menu_info(menu: schemas.MenuCreate, db: Session = Depends(get_db)):
    # clova 함수 호출
    # 데이터 하나하나 저장

    clova = Clova()
    response = clova.ocr_transform(menu.s3_image_url)
    # 실패
    if not response.status:
        raise HTTPException(status_code=500, detail="Clova OCR API Error")

    # 중복이면 안넣어야 함
    create_menu_info = {}
    for idx, data in enumerate(response.data):
        name, cost = data
        existed_menu = menu_crud.get_menu_by_id_and_name(db, menu.store_id, name)
        # 존재하지 않는 메뉴이므로 새로 생성해야함
        if not existed_menu:
            create_menu_info[idx + 1] = menu_crud.create_menu(db, name, cost, menu=menu)
        else:
            # 존재하는데, 삭제된 메뉴이므로 is_active = true로 변경
            if not existed_menu.is_active:
                menu_crud.restore_menu_by_id(db, existed_menu.id)

    return {}


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
