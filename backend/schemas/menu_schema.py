from pydantic import BaseModel


class MenuBase(BaseModel):
    class Config:
        orm_mode = True


class Menu(MenuBase):  # 메뉴
    name: str
    cost: str  # 잠시 str로 수정
    photo_url: str
    is_active: bool
    is_main_menu: bool


class MenuCreate(MenuBase):
    store_id: int
    # s3_image_url: str
    # name: str
    # cost: int
    # photo_url: str


class MenusCreate(MenuBase):
    store_id: int
    name: str
    cost: str
    photo_url: str


class MenuRead(MenuCreate):
    id: str


class MenuUpdate(MenuBase):
    is_main_menu: bool


class MenuDelete(MenuBase):
    is_active: bool
