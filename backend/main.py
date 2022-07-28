import uuid
from fastapi import FastAPI
from fastapi import UploadFile, File
from fastapi.middleware.cors import CORSMiddleware

from database import Base
from database import engine

from aws.bucket import post_bucket
from api.api import api_router

Base.metadata.create_all(bind=engine)

origins = [
    "http://localhost",
    "http://localhost:3000",
    "http://localhost:8080",
]
app = FastAPI(title="전통시장")
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(api_router, prefix="/api")


@app.post("/upload", status_code=200, description="***** Upload JPG asset to S3 *****")
async def upload(file_object: UploadFile = File(...)):
    file_object.filename = f"{uuid.uuid4()}.jpg"
    content = await file_object.read()
    post_bucket(content, file_object.filename)
    return {"filename": file_object.filename}
