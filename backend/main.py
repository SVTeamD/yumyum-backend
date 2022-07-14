from typing import Union
import uuid

from fastapi import FastAPI
from fastapi import UploadFile, File
from fastapi.responses import HTMLResponse

from aws.bucket import post_bucket


app = FastAPI()


@app.get("/")
async def main():
    return {"Hello from": "FastAPI"}

@app.post("/upload", status_code=200, description="***** Upload JPG asset to S3 *****")
async def upload(file_object: UploadFile=File(...)):
    file_object.filename = f"{uuid.uuid4()}.jpg"
    content = await file_object.read()
    post_bucket(content, file_object.filename)
    return {"filename": file_object.filename}    