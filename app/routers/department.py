from pydantic import BaseModel
from datetime import datetime

#Depertment create request model 
class Create_model(BaseModel):
    name: str
    location: str 
    budget: float

#Depertment update request model 
class Update_model(BaseModel):
    name: str
    location: str 
    budget: float

#Depertment fetch response model 
class Get_model(BaseModel):
    id: int
    name: str
    location: str
    budget: float
    created_at: datetime
    updated_at: datetime