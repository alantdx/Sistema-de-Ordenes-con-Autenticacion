from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from db import get_db, Order
import schemas

orders_router = APIRouter()

@orders_router.post("/orders")
def create_order(order: schemas.OrderCreate, db: Session = Depends(get_db)):
    db_order = Order(**order.dict())
    db.add(db_order)
    db.commit()
    db.refresh(db_order)
    return db_order

@orders_router.get("/orders")
def list_orders(db: Session = Depends(get_db)):
    return db.query(Order).all()