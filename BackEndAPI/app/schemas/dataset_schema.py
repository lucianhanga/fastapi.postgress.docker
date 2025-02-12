from pydantic import BaseModel
from typing import Optional
import uuid

class DatasetBase(BaseModel):
    name: str
    description: Optional[str] = None
    images: str

class DatasetCreate(DatasetBase):
    owner_id: uuid.UUID  # Include owner_id in the creation schema

class DatasetUpdate(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    images: Optional[str] = None

class DatasetResponse(DatasetBase):
    id: uuid.UUID
    owner_id: uuid.UUID  # Include owner_id in the response schema

    class Config:
        orm_mode = True