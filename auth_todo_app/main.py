from fastapi import FastAPI, Depends, HTTPException, status, BackgroundTasks
from fastapi.security import OAuth2PasswordRequestForm, OAuth2PasswordBearer
from datetime import timedelta
from jose import JWTError, jwt
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
import models, schemas, crud, auth
from database import engine, get_db
import time

app = FastAPI()

@app.on_event("startup")
async def startup():
    async with engine.begin() as conn:
        await conn.run_sync(models.Base.metadata.create_all)

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")

async def get_current_user(token: str = Depends(oauth2_scheme), db: AsyncSession = Depends(get_db)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, auth.SECRET_KEY, algorithms=[auth.ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
    except JWTError:
        raise credentials_exception
    user = await crud.get_user_by_username(db, username=username)
    if user is None:
        raise credentials_exception
    return user

@app.get("/profile", response_model=schemas.UserResponse)
async def profile(current_user: models.User = Depends(get_current_user)):
    return current_user

async def admin_required(current_user: models.User = Depends(get_current_user)):
    if current_user.role != "admin":
        raise HTTPException(status_code=403, detail="Admin access required")
    return current_user

@app.get("/admin")
async def admin_dashboard(current_user: models.User = Depends(admin_required)):
    return {"message": f"Welcome Admin {current_user.username}"}

@app.get("/admin/users/{user_id}/tasks", response_model=list[schemas.TaskResponse])
async def read_user_tasks_admin(user_id: int, skip: int = 0, limit: int = 100, db: AsyncSession = Depends(get_db), current_user: models.User = Depends(admin_required)):
    return await crud.get_user_tasks(db, user_id=user_id, skip=skip, limit=limit)

def send_welcome_email(email: str, username: str):
    """
    Simulates sending a welcome email in the background.
    """
    print(f"\n[BACKGROUND TASK] Starting to send email to {email}...")
    # Simulate some delay (e.g., connecting to SMTP server)
    time.sleep(2) 
    print(f"[BACKGROUND TASK] Email sent to {email}: 'Welcome to Auth User, {username}!'")
    print(f"[BACKGROUND TASK] Task completed.\n")

@app.get("/")
async def read_root():
    return {"message": "Auth Todo App is running"}

@app.post("/register", response_model=schemas.UserResponse)
async def register(user: schemas.UserCreate, background_tasks: BackgroundTasks, db: AsyncSession = Depends(get_db)):
    existing_user = await crud.get_user_by_username(db, user.username)
    if existing_user:
        raise HTTPException(status_code=400, detail="Username already exists")
    
    new_user = await crud.create_user(db, user)
    
    # Add background task to send welcome email
    background_tasks.add_task(send_welcome_email, new_user.email, new_user.username)
    
    return new_user

@app.post("/login", response_model=schemas.Token)
async def login(form_data: OAuth2PasswordRequestForm = Depends(), db: AsyncSession = Depends(get_db)):
    user = await crud.get_user_by_username(db, form_data.username)
    if not user or not auth.verify_password(form_data.password, user.hashed_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=auth.ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = auth.create_access_token(
        data={"sub": user.username}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}

@app.get("/users", response_model=list[schemas.UserResponse])
async def read_users(skip: int = 0, limit: int = 100, db: AsyncSession = Depends(get_db)):
    # Need to update READ queries if direct DB access was used, but crud.py handles specific queries.
    # For this generic list, we might want a new CRUD function or execute directly.
    # For now, let's keep it simple and just return what we can or implement a simple query.
    # Actually, the original code had: users = db.query(models.User)...
    result = await db.execute(select(models.User).offset(skip).limit(limit))
    return result.scalars().all()

# --- Todo Endpoints ---

@app.post("/tasks", response_model=schemas.TaskResponse)
async def create_task(task: schemas.TaskCreate, db: AsyncSession = Depends(get_db), current_user: models.User = Depends(get_current_user)):
    return await crud.create_user_task(db=db, task=task, user_id=current_user.id)

@app.get("/tasks", response_model=list[schemas.TaskResponse])
async def read_tasks(skip: int = 0, limit: int = 100, db: AsyncSession = Depends(get_db), current_user: models.User = Depends(get_current_user)):
    return await crud.get_user_tasks(db, user_id=current_user.id, skip=skip, limit=limit)
