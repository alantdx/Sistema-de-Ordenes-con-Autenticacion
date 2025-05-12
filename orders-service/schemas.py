from pydantic import BaseModel

class OrderCreate(BaseModel):
    item: str
    quantity: int