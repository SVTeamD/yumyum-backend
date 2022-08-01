import re
import requests
import uuid
import time
import json
import utils.config as config


class ResponseClova:
    status: bool
    message: str
    data: list

    def __init__(self, status: bool, message: str, data: list):
        self.status = status
        self.message = message
        self.data = data


class Clova:
    def __init__(self):
        self.request_json = {
            "images": [
                {
                    "format": "jpg",
                    "name": "demo",
                }
            ],
            "requestId": str(uuid.uuid4()),
            "version": "V2",
            "timestamp": int(round(time.time() * 1000)),
        }
        self.payload = {"message": json.dumps(self.request_json).encode("UTF-8")}
        self.headers = {"X-OCR-SECRET": config.SECRET_KEY}

    def __request_clova_api_file(self, file: bytes):
        try:
            files = [("file", file)]
            response = requests.request(
                "POST",
                config.API_URL,
                headers=self.headers,
                data=self.payload,
                files=files,
            )
            res = json.loads(response.text.encode("utf8"))
            return res
        except:
            return False

    def __preprocess(self, lst: list):
        menu_price_lst = []

        # 가격인지 구분하는 문자열 (추후 추가 가능)
        price_division = "00"

        # 메뉴에 한글이 있는지 전처리
        hangul = re.compile('[가-힣+]')

        for idx, data in enumerate(lst):
            if price_division in data:
                # 제대로 된 메뉴인지 검증
                # 1. 메뉴에 가격이 들어갔는지
                if price_division in lst[idx - 1]:
                    continue

                # 2. 한글이 포함되어 있지 않으면 이상한 메뉴로 판단
                if len(hangul.sub('',lst[idx - 1])) == len(lst[idx - 1]):
                    continue
 
                price = re.sub('[-=+,#/\?:^.@*\"※~ㆍ!』‘|\(\)\[\]`\'…》\”\“\’·]', '', re.split('[()-]', lst[idx])[0])
                menu_price_lst.append((lst[idx - 1], price))

        return menu_price_lst


    def ocr_transform(self, image: bytes):
        """
        image: 이미지
        return : {status: boolean, data: list}
        """
        res = self.__request_clova_api_file(image)
        data = []

        # check s3 image url validate
        if not res:
            message = "s3 image url not validate"
            return ResponseClova(False, message, data)

        # check api_url validate
        if "error" in res:
            return ResponseClova(False, res["error"]["message"], data)

        # check secret_key
        if "code" in res and res["code"] == "0002":
            return ResponseClova(False, res["message"], data)

        for field in res["images"][0]["fields"]:
            data.append(field["inferText"])

        return ResponseClova(True, res["images"][0]["message"], self.__preprocess(data))
