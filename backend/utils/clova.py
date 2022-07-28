import requests
import uuid
import time
import json
import utils.config as config
from urllib.request import urlopen 

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
            'images': [
                {
                    'format': 'jpg',
                    'name': 'demo',
                }
            ],
            'requestId': str(uuid.uuid4()),
            'version': 'V2',
            'timestamp': int(round(time.time() * 1000))
        }
        self.payload = {'message': json.dumps(self.request_json).encode('UTF-8')}
        self.headers = {
        'X-OCR-SECRET': config.SECRET_KEY
        }
 
    def __request_clova_api(self, url: str):
        try:
            file = urlopen(url).read()
            files = [('file', file)]
            response = requests.request('POST', config.API_URL, headers=self.headers, data = self.payload, files = files)
            res = json.loads(response.text.encode('utf8'))
            return res
        except:
            return False

    def __preprocess(self, lst: list):
        menu_price_lst = []

        # 가격인지 구분하는 문자열 (추후 추가 가능)
        price_division = '00'

        # 문자열에서 구분점 지워줌
        for idx, data in enumerate(lst):
            lst[idx] = data.replace(',','').replace('.','').replace(':','')

        for idx, data in enumerate(lst):
            if price_division in data:
                menu_price_lst.append((lst[idx-1], lst[idx]))
              
        return menu_price_lst

        
    def ocr_transform(self, image_url: str):
        '''
        image_url : s3 이미지 url 경로
        return : {status: boolean, data: list}
        '''
        res = self.__request_clova_api(image_url)
        data = []

        # check s3 image url validate
        if not res:
            message = 's3 image url not validate'
            return ResponseClova(False, message, data)

        # check api_url validate
        if 'error' in res:
            return ResponseClova(False, res['error']['message'], data)

        # check secret_key
        if 'code' in res and res['code'] == '0002':
            return ResponseClova(False, res['message'], data)

        for field in res['images'][0]['fields']:
            data.append(field['inferText'])

        return ResponseClova(True, res['images'][0]['message'], self.__preprocess(data))

        

        
        