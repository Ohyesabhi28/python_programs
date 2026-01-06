from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class User(BaseModel):
    name: str
    age: int


@app.get("/")
def home():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
def say_hello(name: str):
    return {"message": f"Hello {name}!"}


@app.post("/message")
def post_message(message: dict):
    return {"received": message, "status": "success"}
#
 POST endpoint for creating users
@app.post("/users")
def create_user(user: User):
    return {
        "message": "User created successfully",
        "user": user
    }