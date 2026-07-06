from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from app.schemas.employee import Create_model
from app.database.db import get_db
from app.crud import employee as emp_crud

router = APIRouter(
    prefix="/api/v1/employees",
    tags=["Employee"]  
)

@router.post("", status_code=status.HTTP_201_CREATED)
def create_employee(payload: Create_model, db: Session = Depends(get_db)):  
    new_emp = emp_crud.create_emp_in_db(db=db, emp_data=payload)
    return new_emp
