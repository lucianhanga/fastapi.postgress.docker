from pydantic import BaseModel
import uuid

class StartTrainingRequest(BaseModel):
    userid: uuid.UUID
    trainingsetid: uuid.UUID

class StopTrainingRequest(BaseModel):
    trainingid: uuid.UUID
