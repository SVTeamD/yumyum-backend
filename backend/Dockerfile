FROM python:3.9

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /backend
COPY requirements.txt /backend/

RUN pip install --no-cache-dir --upgrade -r requirements.txt

COPY . /backend/

# CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]
# Fast api 공식 문서에 있는 내용 보고 한거니까, 수정 하셔도 됩니다 :)   alphine 적용하셔도 됩니다 ~!