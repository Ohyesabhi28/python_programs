from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    name: str
    description: str = None
    price: float
    tax: float = None

@app.get("/")
def read_root():
    return {"message": "Hello FastAPI"}

@app.post("/items/")
def create_item(item: Item):
    return {"message": "Item created successfully", "item": item}

