from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session

import crud
import models
import schemas
from database import engine, get_db

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

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

@app.put("/users/{user_id}", response_model=schemas.UserResponse)
def update_user(user_id: int, user: schemas.UserUpdate, db: Session = Depends(get_db)):
    updated = crud.update_user(db, user_id, user)
    if not updated:
        raise HTTPException(status_code=404, detail="User not found")
    return updated

@app.get("/")
def health_check():
    return {"message": "API is running!"}

@app.delete("/users/{user_id}")
def delete_user(user_id: int, db: Session = Depends(get_db)):
    crud.delete_user(db, user_id)
    return {"message": "User deleted"}

# Product endpoints
@app.post("/products", response_model=schemas.ProductResponse)
def create_product(product: schemas.ProductCreate, db: Session = Depends(get_db)):
    return crud.create_product(db, product)

@app.get("/products", response_model=list[schemas.ProductResponse])
def read_products(db: Session = Depends(get_db)):
    return crud.get_products(db)

@app.get("/products/{product_id}", response_model=schemas.ProductResponse)
def read_product(product_id: int, db: Session = Depends(get_db)):
    product = crud.get_product(db, product_id)
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    return product

@app.put("/products/{product_id}", response_model=schemas.ProductResponse)
def update_product(product_id: int, product: schemas.ProductUpdate, db: Session = Depends(get_db)):
    updated = crud.update_product(db, product_id, product)
    if not updated:
        raise HTTPException(status_code=404, detail="Product not found")
    return updated

@app.delete("/products/{product_id}")
def delete_product(product_id: int, db: Session = Depends(get_db)):
    deleted = crud.delete_product(db, product_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Product not found")
    return {"message": "Product deleted successfully"}

# Profile endpoints
@app.post("/users/{user_id}/profile", response_model=schemas.ProfileResponse)
def create_profile(user_id: int, profile: schemas.ProfileCreate, db: Session = Depends(get_db)):
    # Check if user exists
    user = crud.get_user(db, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    
    # Check if profile already exists
    existing_profile = crud.get_profile_by_user_id(db, user_id)
    if existing_profile:
        raise HTTPException(status_code=400, detail="Profile already exists for this user")
    
    return crud.create_profile(db, profile, user_id)

@app.get("/users/{user_id}/profile", response_model=schemas.ProfileResponse)
def get_profile(user_id: int, db: Session = Depends(get_db)):
    profile = crud.get_profile_by_user_id(db, user_id)
    if not profile:
        raise HTTPException(status_code=404, detail="Profile not found")
    return profile

@app.put("/users/{user_id}/profile", response_model=schemas.UserResponse)
def update_profile(
    user_id: int,
    profile: schemas.ProfileCreate,
    db: Session = Depends(get_db)
):
    return crud.update_profile(db, user_id, profile)

@app.delete("/users/{user_id}/profile")
def delete_profile(user_id: int, db: Session = Depends(get_db)):
    deleted = crud.delete_profile(db, user_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Profile not found")
    return {"message": "Profile deleted successfully"}

# Bidirectional Author endpoints
@app.post("/authors", response_model=schemas.AuthorResponse)
def create_author(author: schemas.AuthorCreate, db: Session = Depends(get_db)):
    return crud.create_author(db, author)

@app.get("/authors", response_model=list[schemas.AuthorResponse])
def read_authors(db: Session = Depends(get_db)):
    return crud.get_authors(db)

@app.get("/authors/{author_id}", response_model=schemas.AuthorResponse)
def read_author(author_id: int, db: Session = Depends(get_db)):
    author = crud.get_author(db, author_id)
    if not author:
        raise HTTPException(status_code=404, detail="Author not found")
    return author

@app.put("/authors/{author_id}", response_model=schemas.AuthorResponse)
def update_author(author_id: int, author: schemas.AuthorUpdate, db: Session = Depends(get_db)):
    updated = crud.update_author(db, author_id, author)
    if not updated:
        raise HTTPException(status_code=404, detail="Author not found")
    return updated

@app.delete("/authors/{author_id}")
def delete_author(author_id: int, db: Session = Depends(get_db)):
    deleted = crud.delete_author(db, author_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Author not found")
    return {"message": "Author deleted successfully"}

# AuthorBio endpoints (bidirectional)
@app.post("/authors/{author_id}/bio", response_model=schemas.AuthorBioResponse)
def create_author_bio(author_id: int, bio: schemas.AuthorBioCreate, db: Session = Depends(get_db)):
    # Check if author exists
    author = crud.get_author(db, author_id)
    if not author:
        raise HTTPException(status_code=404, detail="Author not found")
    
    # Check if bio already exists
    existing_bio = crud.get_author_bio_by_author_id(db, author_id)
    if existing_bio:
        raise HTTPException(status_code=400, detail="Bio already exists for this author")
    
    return crud.create_author_bio(db, bio, author_id)

@app.get("/authors/{author_id}/bio", response_model=schemas.AuthorBioResponse)
def get_author_bio(author_id: int, db: Session = Depends(get_db)):
    bio = crud.get_author_bio_by_author_id(db, author_id)
    if not bio:
        raise HTTPException(status_code=404, detail="Author bio not found")
    return bio

@app.put("/authors/{author_id}/bio", response_model=schemas.AuthorResponse)
def update_author_bio(author_id: int, bio: schemas.AuthorBioCreate, db: Session = Depends(get_db)):
    updated = crud.update_author_bio(db, author_id, bio)
    if not updated:
        raise HTTPException(status_code=404, detail="Author not found")
    return updated

@app.delete("/authors/{author_id}/bio")
def delete_author_bio(author_id: int, db: Session = Depends(get_db)):
    deleted = crud.delete_author_bio(db, author_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Author bio not found")
    return {"message": "Author bio deleted successfully"}