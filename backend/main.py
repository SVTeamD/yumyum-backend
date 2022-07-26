import uuid
from fastapi import  FastAPI
from fastapi import UploadFile, File
from database import Base
from database import engine

from aws.bucket import post_bucket

from api.api import api_router

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="전통시장"
)
app.include_router(api_router, prefix='/api')


@app.post("/upload", status_code=200, description="***** Upload JPG asset to S3 *****")
async def upload(file_object: UploadFile = File(...)):
    file_object.filename = f"{uuid.uuid4()}.jpg"
    content = await file_object.read()
    post_bucket(content, file_object.filename)
    return {"filename": file_object.filename}
