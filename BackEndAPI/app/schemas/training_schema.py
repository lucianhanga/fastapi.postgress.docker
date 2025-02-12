from pydantic import BaseModel
from typing import Optional
import uuid
from datetime import datetime

class StartTrainingRequest(BaseModel):
    userid: uuid.UUID
    trainingsetid: uuid.UUID

class StopTrainingRequest(BaseModel):
    trainingid: uuid.UUID

class TrainingBase(BaseModel):
    name: str
    base_model: str
    imgs_count: int
    time_taken: float
    start_date: datetime

class TrainingCreate(TrainingBase):
    owner_id: uuid.UUID
    dataset_id: uuid.UUID

class TrainingUpdate(BaseModel):
    name: Optional[str] = None
    base_model: Optional[str] = None
    imgs_count: Optional[int] = None
    time_taken: Optional[float] = None
    start_date: Optional[datetime] = None

class TrainingResponse(TrainingBase):
    id: uuid.UUID
    owner_id: uuid.UUID
    dataset_id: uuid.UUID

    class Config:
        orm_mode = True
