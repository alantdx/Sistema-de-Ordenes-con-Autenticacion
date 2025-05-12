from fastapi import FastAPI
from orders import orders_router
from db import Base, engine

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Orders Service")
app.include_router(orders_router)
