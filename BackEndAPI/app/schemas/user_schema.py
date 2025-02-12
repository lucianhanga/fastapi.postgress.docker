from pydantic import BaseModel, EmailStr
from typing import Optional
import uuid

class UserBase(BaseModel):
    email: EmailStr
    name: str
    description: Optional[str] = None  # New field

class UserCreate(UserBase):
    pass

class UserUpdate(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None

class UserResponse(UserBase):
    id: uuid.UUID

    class Config:
        orm_mode = True
