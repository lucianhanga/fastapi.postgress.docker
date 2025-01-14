from pydantic import BaseModel
from typing import Optional
import uuid

class DatasetBase(BaseModel):
    name: str
    description: Optional[str] = None
    images: str

class DatasetCreate(DatasetBase):
    pass

class DatasetUpdate(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    images: Optional[str] = None

class DatasetResponse(DatasetBase):
    id: uuid.UUID

    class Config:
        orm_mode = True