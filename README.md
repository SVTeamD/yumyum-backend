## **Backend**

This is a backend setup for SVTeamD.  
전통시장 활성화 플랫폼

<br>

## **Installation** 
- Clone the repository using this command.
    ```sh
    $ git clone https://github.com/SVTeamD/yumyum-backend.git
    ```

<br>

## **System Architecture**
![sysarch](https://user-images.githubusercontent.com/102022609/182135088-a0c6409c-6a7e-4f85-8603-bb92e98339bd.png)


<br>

## **Tech stack**
| 분류  |  기술                                                                 |
| --   | --------------------------------------------------------------------- |
| Frontend | ![REACT](https://img.shields.io/badge/react-61DAFB?style=for-the-badge&logo=react&logoColor=black) ![Axios](https://img.shields.io/badge/Axios-black?style=for-the-badge&logo=Axios&logoColor=black)    |
| Backend | ![Fastapi](https://img.shields.io/badge/fastapi-009688?style=for-the-badge&logo=Fastapi&logoColor=black) ![Uvicorn](https://img.shields.io/badge/Uvicorn-009688?style=for-the-badge&logo=Uvicorn&logoColor=black) ![Swagger](https://img.shields.io/badge/swagger-gray?style=for-the-badge&logo=Swagger&logoColor=green) ![Docker](https://img.shields.io/badge/docker-000000?style=for-the-badge&logo=docker&logoColor=blue) ![clova](https://img.shields.io/badge/clova-green?style=for-the-badge&logo=naver&logoColor=00DB9B) ![Elasticsearch](https://img.shields.io/badge/Elasticsearch-005571?style=for-the-badge&logo=Elasticsearch&logoColor=04B4AE)    |
| DB | ![MYSQL](https://img.shields.io/badge/mysql-4479A1?style=for-the-badge&logo=mysql&logoColor=white)      |                   
| CI/CD | ![GitHubActions](https://img.shields.io/badge/GitHubActions-9cf?style=for-the-badge&logo=GitHubActions&logoColor=blue)         
| Infra | ![Nginx](https://img.shields.io/badge/nginx-inactive?style=for-the-badge&logo=nginx&logoColor=009639) ![S3](https://img.shields.io/badge/S3-orange?style=for-the-badge&logo=AmazonS3&logoColor=569A31) ![EC2](https://img.shields.io/badge/EC2-white?style=for-the-badge&logo=AmazonEC2&logoColor=FF9900)     |
| Monitoring| ![Prometheus](https://img.shields.io/badge/Prometheus-white?style=for-the-badge&logo=Prometheus&logoColor=E6522C) ![Grafana](https://img.shields.io/badge/Grafana-white?style=for-the-badge&logo=Grafana&logoColor=F46800) ![Alertmanager](https://img.shields.io/badge/Alertmanager-black?style=for-the-badge&logo=Alertmanager&logoColor=F46800) ![Slack-Bot](https://img.shields.io/badge/Slack_Bot-black?style=for-the-badge&logo=Slack-Bot&logoColor=F46800)     |

<br>

## **Swagger**

### Menus

- `POST` /api/menus/    → 메뉴 등록
    - Params:
        - menu: object
        - menu_image: string(binary)
    - Status Code
        - 201
        - 422
- `GET` /api/menus/main/  → 메인 메뉴의 상세 정보 보여줌
    - Responses:
        - name: string
        - cost: string
        - photo_url: string
        - is_active: true
        - is_main_menu: true
    - Status Code
        - 200
- `GET` /api/menus/{menu_id} → 사용자가 원하는 메뉴의 상세 정보 보여줌
    - params:
        - menu_id: integer(path)
    - Responses::
        - string
    - Status Code
        - 200
        - 422
    
- `DELETE` /api/menus/{menu_id} → 특정 메뉴를 삭제처리(is_active == False)
    - Params
        - name_id: int
    - Status Code
        - 200
        - 422
- `GET` /api/menus/name/{menu_name} → 메뉴명으로 메뉴 상세정보를 검색
    - Params
        - menu_name: string
    - Status Code
        - 200
        - 422
- `PUT` /api/menus/main/{menu_id} → 메인 메뉴를 지정하기 위함
    - Params
        - menu_id: int
    - Status Code
        - 200
        - 422

### Users

- `POST` /api/users/ → 신규 사용자 등록
    - Params
        - None
    - Status Code
        - 201
        - 422
- `GET` /api/users/{user_id} → 특정 사용자 정보 보여줌
    - Prarms
        - user_id: int
    - Status Code
        - 200
        - 422
- `DELETE`/api/users/{user_id} → 특정 사용자를 삭제처리(is_active=False)
    - Params
        - user_id: int
    - Status Code
        - 200
        - 422

### Stores

- `GET` /api/stores/ → 등록된 모든 상점을 호출하기 위함
    - Params
        - None
    - Status Code
        - 200
- `POST` /api/stores/ → 가게를 등록하기 위함
    - Params
        - store: object
        - loc: object
        - store_image: string($binary)
    - Status Code
        - 201
        - 422
- `GET` /api/stores/{store_id}/menus → 특정 가게 메뉴를 호출하기 위함
    - Params
        - store_id: int
        - skip: int
        - limit: int
    - Status Code
        - 200
        - 422
- `DELETE` /api/stores/{store_id} → 특정 가게를 삭제처리(is_active=False) 하기 위함
    - Params
        - store_id: int
    - Status Code
        - 200
        - 422

### Orders

- `GET` /api/orders/ → 모든 주문을 보여줌
    - Params:
        - None
    - Status Code
        - 200
- `POST` /api/orders/ → 새로운 주문을 등록
    - Params
        - user_id: int
        - store_id: int
        - datetime: Datetime
        - is_takeout: true
        - cost: int
    - Status Code
        - 201
        - 422
- `GET` /api/orders/{order_id} → 특정 주문 상세 내용을 가져오기 위함
    - Params
        - order_id: integer
    - Status Code
        - 201
        - 422
- `DELETE` /api/orders/{order_id} → 주문을 취소하기 위함
    - Params
        - order_id: integer
    - Status Code
        - 200
        - 422
- `GET` /api/orders/user/{user_id} → 특정 사용자의 주문 상세를 확인하기 위함
    - Params
        - user_id: int
    - Status Code
        - 200
        - 422
- `GET` /api/orders/store/{store_id} → 특정 가게의 모든 주문을 확인하기 위함
    - Params
        - store_id: int
    - Status Code
        - 200
        - 422
        
<br>

## How to start

- Clone the repository using this command.
   ```sh
   $ git clone docker compose up -d
   ```
   
<br>

## **Directory**
```sh
.
├── alertmanager
├── backend
│   ├── api
│   │   └── endpoints
│   ├── aws
│   ├── crud
│   ├── models
│   ├── schemas
│   └── utils
├── grafana
├── prometheus
├── proxy
├── settings
│   └── prod
└── volumes
└── logstash
├── config
│   └── queries
└── pipeline
```
<br>

## **👨‍👨‍👧‍👦 Members**
| 이름  | 개발분야 |    소개페이지                |  
| -----| -------|------------------------- |
|홍성민 | Front-end, Back-End, Devops| [Github](https://github.com/KKodiac)   |
|김주원 | Front-end, Back-end| [Github](https://github.com/juwon5272)   |
|김인철 | Front-end, Back-end, Devops| [Github](https://github.com/kimich1218)   |
|최현정 | Back-end|[Github](https://github.com/ChoiPilkyu)   |
|김주희 | Front-end| [Github](https://github.com/edi54)   |
|한상우 | Back-end,Devops| [Github](https://github.com/sktkddn777)   |
  
  
  
