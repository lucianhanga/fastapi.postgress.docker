from pydantic import BaseModel, EmailStr
from typing import Optional
import uuid

class UserBase(BaseModel):
    email: EmailStr
    name: str
    description: Optional[str] = None  # New field

class UserCreate(UserBase):
    pass

class UserResponse(UserBase):
    id: uuid.UUID

    class Config:
        orm_mode = True
