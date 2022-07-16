from typing import List

import boto3
from .config import S3_Bucket
from .connection import connect

def post_bucket(image_file: str, key_name: str):
    client = connect()
    client.put_object(
        Body=image_file, 
        Bucket=S3_Bucket,
        Key=key_name,
        ContentType="image.jpeg"
    )