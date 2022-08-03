import boto3

# 해당 모듈은 버켓 보안을 위해 .gitignore 에 추가되어 있습니다. 추가 문의는 팀 리더에게 해주세요.
from .config import AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY


class Connect:
    def __init__(self):
        self.client = boto3.client(
            "s3",
            aws_access_key_id=AWS_ACCESS_KEY_ID,
            aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
        )

    def __enter__(self):
        return self 

    def connect(self):
        return self.client

    def __exit__(self, exc_type, exc_val, exc_tb):
        ...

