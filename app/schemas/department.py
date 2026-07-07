from datetime import datetime

from pydantic import BaseModel


# Depertment create request model
class Create_model(BaseModel):
    name: str


# Depertment update request model
class Update_model(BaseModel):
    name: str


# Depertment fetch model
class Get_model(BaseModel):
    id: int
    name: str
    created_at: datetime
    updated_at: datetime
