from pydantic import BaseModel
from typing import Optional, List

class RoleBase(BaseModel):
    name: str

class RoleCreate(RoleBase):
    pass

class RoleResponse(RoleBase):
    id: int
    
    class Config:
        from_attributes = True

class UserBase(BaseModel):
    name: str
    email: str

class UserCreate(UserBase):
    role_ids: List[int] = []

class UserResponse(UserBase):
    id: int
    roles: List[RoleResponse] = []
    
    class Config:
        from_attributes = True

class UserRolesUpdate(BaseModel):
    role_ids: List[int]

class RoleUsersUpdate(BaseModel):
    user_ids: List[int]