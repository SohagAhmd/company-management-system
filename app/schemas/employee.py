from pydantic import BaseModel
from datetime import datetime, date

#Employee create request model
class Create_model(BaseModel):
    first_name: str
    last_name: str
    email: str
    phone: str
    salary: float
    job_title: str
    hire_date: date


#Employee update request model
class Update_model(BaseModel):
    first_name: str
    last_name: str
    email: str
    phone: str
    last_name: str
    email: str
    phone: str
    salary: float
    job_title: str
    hire_date: date
    salary: float
    job_title: str
    hire_date: date


#Employee Fetch response model
class get_model(BaseModel):
    id: int
    first_name: str
    last_name: str
    email: str
    phone: str
    salary: float
    job_title: str
    hire_date: date
    created_at: datetime
    updated_at: datetime