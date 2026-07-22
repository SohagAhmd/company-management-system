from datetime import date, datetime
from typing import List

from pydantic import BaseModel, ConfigDict


# Employee create request model
class Create_model(BaseModel):
    first_name: str
    last_name: str
    email: str
    phone: str
    salary: float
    job_title: str
    hire_date: date
    department_id: int


# Employee update request model
class Update_model(BaseModel):
    department_name: str
    first_name: str
    last_name: str
    email: str
    phone: str
    salary: float
    job_title: str
    hire_date: date


# Schema for returning minimal department details within nested relationships.
class DepartmentMinResponse(BaseModel):
    name: str
    id: int

    model_config = ConfigDict(from_attributes=True)


# Employee Fetch response model
class Get_model(BaseModel):
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
    department: DepartmentMinResponse

    model_config = ConfigDict(from_attributes=True)


# Employee Pagination Response
class EmployeePaginationResponse(BaseModel):
    total: int
    items: List[Get_model]