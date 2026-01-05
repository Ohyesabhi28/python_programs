from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

import crud
import models
import schemas
from database import engine, get_db

models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="Todo App API")

@app.post("/users", response_model=schemas.UserResponse)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_username(db, user.username)
    if db_user:
        raise HTTPException(status_code=400, detail="Username already exists")
    return crud.create_user(db, user)

@app.get("/users", response_model=List[schemas.UserResponse])
def get_users(db: Session = Depends(get_db)):
    return crud.get_users(db)

@app.get("/users/{user_id}", response_model=schemas.UserResponse)
def get_user(user_id: int, db: Session = Depends(get_db)):
    user = crud.get_user(db, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@app.post("/users/{user_id}/tasks", response_model=schemas.TaskResponse)
def create_task(user_id: int, task: schemas.TaskCreate, db: Session = Depends(get_db)):
    user = crud.get_user(db, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return crud.create_task(db, task, user_id)

@app.get("/users/{user_id}/tasks", response_model=List[schemas.TaskResponse])
def get_user_tasks(user_id: int, db: Session = Depends(get_db)):
    user = crud.get_user(db, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return crud.get_user_tasks(db, user_id)

@app.put("/tasks/{task_id}", response_model=schemas.TaskResponse)
def update_task(task_id: int, task_update: schemas.TaskUpdate, db: Session = Depends(get_db)):
    updated_task = crud.update_task(db, task_id, task_update)
    if not updated_task:
        raise HTTPException(status_code=404, detail="Task not found")
    return updated_task

@app.delete("/tasks/{task_id}")
def delete_task(task_id: int, db: Session = Depends(get_db)):
    deleted_task = crud.delete_task(db, task_id)
    if not deleted_task:
        raise HTTPException(status_code=404, detail="Task not found")
    return {"message": "Task deleted successfully"}

@app.get("/admin/users", response_model=List[schemas.UserResponse])
def admin_get_all_users(db: Session = Depends(get_db)):
    return crud.get_users(db)

@app.get("/admin/tasks", response_model=List[schemas.TaskResponse])
def admin_get_all_tasks(db: Session = Depends(get_db)):
    return crud.get_all_tasks(db)

@app.get("/admin/tasks/{task_id}", response_model=schemas.TaskResponse)
def admin_get_task(task_id: int, db: Session = Depends(get_db)):
    task = crud.get_task(db, task_id)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    return task

@app.get("/admin/users/{user_id}/tasks", response_model=List[schemas.TaskResponse])
def admin_get_user_tasks(user_id: int, db: Session = Depends(get_db)):
    user = crud.get_user(db, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return crud.get_user_tasks(db, user_id)

@app.get("/admin/users/{user_id}/tasks/{task_id}", response_model=schemas.TaskResponse)
def admin_get_user_task(user_id: int, task_id: int, db: Session = Depends(get_db)):
    user = crud.get_user(db, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    
    task = crud.get_task(db, task_id)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    
    if task.user_id != user_id:
        raise HTTPException(status_code=404, detail="Task not found for this user")
        
    return task

@app.get("/")
def health_check():
    return {"message": "Todo App API is running!"}