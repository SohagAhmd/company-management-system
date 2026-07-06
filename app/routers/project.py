from pydantic import BaseModel
from datetime import datetime, date

#Project cretae request model
class Create_model(BaseModel):
    name: str
    description: str
    deadline: date
    status: str


#Project update request model
class Update_model(BaseModel):
    name: str
    description: str
    deadline: date
    status: str


#Project fetch reponse model
class Get_mode(BaseModel):
    id: int
    name: str
    description: str
    deadline: date
    status: str
    created_at: datetime
    updated_at: datetime
