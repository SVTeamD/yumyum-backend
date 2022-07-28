from fastapi import APIRouter
from api.endpoints import menus, users, stores, orders

api_router = APIRouter()
api_router.include_router(menus.router, prefix="/menus", tags=["menus"])
api_router.include_router(users.router, prefix="/users", tags=["users"])
api_router.include_router(stores.router, prefix="/stores", tags=["stores"])
api_router.include_router(orders.router, prefix="/orders", tags=["orders"])
