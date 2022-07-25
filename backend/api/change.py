# @app.post("/orders/", response_model=schemas.orderCreate)  # order api
# def create_order_info(order: schemas.orderCreate, db: Session = Depends(get_db)):
#     return crud.create_order(db, order=order)


# @app.get("/orders/main", response_model=List[schemas.order])
# def read_main_order(skip: int = 1, limit: int = 10, db: Session = Depends(get_db)):
#     orders = crud.get_main_order(db)
#     return orders


# @app.get("/orders/{order_id}/")
# def read_order_by_id(order_id: int, db: Session = Depends(get_db)):
#     orders = crud.get_order_by_id(db, order_id=order_id)
#     return orders


# @app.get("/orders/name/{order_name}/")
# def read_order_by_name(order_name: str, db: Session = Depends(get_db)):
#     orders = crud.get_order_by_name(db, order_name=order_name)
#     return orders


# @app.put("/orders/main/{order_id}")
# def update_order_by_id(order_id: int, db: Session = Depends(get_db)):
#     response = crud.update_main_order_by_id(db, order_id=order_id)
#     return response.status_code


# @app.delete("/orders/{order_id}")
# def delete_order_by_id(order_id: int, db: Session = Depends(get_db)):
#     response = crud.delete_order_by_id(db, order_id=order_id)
#     return response.status_code
