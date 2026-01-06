from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session

import crud
import models
import schemas
from database import engine, get_db

app = FastAPI(title="Many-to-Many FastAPI Project")

# Create tables immediately when the module is imported
models.Base.metadata.create_all(bind=engine)
print("✅ Database tables created successfully!")

@app.get("/")
def health_check():
    return {"message": "Many-to-Many FastAPI is running!"}

@app.post("/roles", response_model=schemas.RoleResponse)
def create_role(role: schemas.RoleCreate, db: Session = Depends(get_db)):
    return crud.create_role(db, role)

@app.get("/roles", response_model=list[schemas.RoleResponse])
def read_roles(db: Session = Depends(get_db)):
    return crud.get_roles(db)

@app.get("/roles/{role_id}", response_model=schemas.RoleResponse)
def read_role(role_id: int, db: Session = Depends(get_db)):
    role = crud.get_role(db, role_id)
    if not role:
        raise HTTPException(status_code=404, detail="Role not found")
    return role

@app.post("/users", response_model=schemas.UserResponse)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    return crud.create_user(db, user)

@app.get("/users", response_model=list[schemas.UserResponse])
def read_users(db: Session = Depends(get_db)):
    return crud.get_users(db)

@app.get("/users/{user_id}", response_model=schemas.UserResponse)
def read_user(user_id: int, db: Session = Depends(get_db)):
    user = crud.get_user(db, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@app.post("/users/{user_id}/roles/{role_id}", response_model=schemas.UserResponse)
def add_role_to_user(user_id: int, role_id: int, db: Session = Depends(get_db)):
    result = crud.add_role_to_user(db, user_id, role_id)
    if result is None:
        raise HTTPException(status_code=404, detail="User not found")
    if result == "ROLE_NOT_FOUND":
        raise HTTPException(status_code=404, detail="Role not found")
    return result

@app.delete("/users/{user_id}/roles/{role_id}", response_model=schemas.UserResponse)
def remove_role_from_user(user_id: int, role_id: int, db: Session = Depends(get_db)):
    result = crud.remove_role_from_user(db, user_id, role_id)
    if result is None:
        raise HTTPException(status_code=404, detail="User not found")
    if result == "ROLE_NOT_FOUND":
        raise HTTPException(status_code=404, detail="Role not found")
    return result

@app.put("/users/{user_id}/roles", response_model=schemas.UserResponse)
def set_user_roles(user_id: int, payload: schemas.UserRolesUpdate, db: Session = Depends(get_db)):
    result = crud.set_user_roles(db, user_id, payload.role_ids)
    if result is None:
        raise HTTPException(status_code=404, detail="User not found")
    if result == "SOME_ROLES_NOT_FOUND":
        raise HTTPException(status_code=404, detail="Some roles not found")
    return result

@app.get("/roles/{role_id}/users", response_model=list[schemas.UserResponse])
def get_users_with_role(role_id: int, db: Session = Depends(get_db)):
    users = crud.get_users_with_role(db, role_id)
    if users is None:
        raise HTTPException(status_code=404, detail="Role not found")
    return users

@app.get("/")
def health_check():
    return {"message": "Many-to-Many FastAPI is running!"}