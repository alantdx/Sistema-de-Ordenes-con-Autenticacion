from fastapi import FastAPI
from auth import auth_router
from db import Base, engine

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Auth Service")
app.include_router(auth_router)