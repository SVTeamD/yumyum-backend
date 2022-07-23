from fastapi import FastAPI
from modules.menu.router import router as menu_router

def create_app() -> FastAPI:
    app = FastAPI()
    return app

app = create_app()
app.include_router(menu_router)