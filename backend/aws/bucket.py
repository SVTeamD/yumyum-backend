from botocore.exceptions import ClientError
from .config import S3_BUCKET
from .connection import connect


def post_bucket(image_file: str, key_name: str):
    with connect() as client:
        try:
            obj = client.put_object(
                Body=image_file, Bucket=S3_BUCKET, Key=key_name, ContentType="image.jpeg"
            )
            obj.wait_until_exists()
        except ClientError as e:
            print("Error during image upload. {}".format(e.response["Error"]["Code"]))
