from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class User(BaseModel):
    name: str
    age: int


@app.get("/users/{user_id}")
def get_user(user_id: int):
    return {"user_id": user_id}

@app.get("/users/{user_id}/orders/{order_id}")
def get_order(user_id: int, order_id: int):
    return {
        "user_id": user_id,
        "order_id": order_id
    }

@app.get("/products/{product_name}")
def get_product(product_name: str):
    return {"product_name": product_name}

@app.get("/users/{user_id}/profile")
def get_user_profile(user_id: int, active: bool = True):
    return {
        "user_id": user_id,
        "active": active
    }

@app.get("/search")
def search_items(name: str, category: str = "all", limit: int = 10):
    return {
        "name": name,
        "category": category,
        "limit": limit
    }

# DELETE endpoint with path parameter
@app.delete("/users/{user_id}")
def delete_user(user_id: int):
    return {
        "message": "User deleted successfully",
        "user_id": user_id
    }

# PUT endpoint with path parameter and request body
@app.put("/users/{user_id}")
def update_user(user_id: int, user: User):
    return {
        "message": "User updated successfully",
        "user_id": user_id,
        "updated_data": user
    }