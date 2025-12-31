from pydantic import BaseModel
from typing import Optional

# Unidirectional schemas (User -> Profile)
class UserCreate(BaseModel):
    email: str
    name: str

class UserUpdate(BaseModel):
    email: str
    name: str

class UserResponse(UserCreate):
    id: int
    
    class Config:
        from_attributes = True

class ProfileCreate(BaseModel):
    age: int
    address: str
    user_id: int

class ProfileResponse(BaseModel):
    id: int
    age: int
    address: str
    user: UserResponse
    
    class Config:
        from_attributes = True

# Bidirectional schemas (Author <-> AuthorBio)
class AuthorBase(BaseModel):
    name: str
    email: str

class AuthorBioBase(BaseModel):
    biography: str
    birth_year: int
    country: str

class AuthorBioCreate(AuthorBioBase):
    pass

class AuthorBioResponse(AuthorBioBase):
    id: int
    author_id: int
    
    class Config:
        from_attributes = True

class AuthorCreate(AuthorBase):
    bio: Optional[AuthorBioCreate] = None

class AuthorUpdate(AuthorBase):
    pass

class AuthorResponse(AuthorBase):
    id: int
    bio: Optional[AuthorBioResponse] = None
    
    class Config:
        from_attributes = True

class ProductBase(BaseModel):
    name: str
    description: str
    price: float
    category: str

class ProductCreate(ProductBase):
    pass

class ProductUpdate(ProductBase):
    pass

class ProductResponse(ProductBase):
    id: int
    
    class Config:
        from_attributes = True