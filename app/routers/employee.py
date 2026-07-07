from fastapi import APIRouter, Depends, status
from typing import List
from sqlalchemy.orm import Session
from app.schemas.employee import Create_model, Get_model
from app.database.db import get_db
from app.crud import employee as emp_crud

router = APIRouter(
    prefix="/api/v1/employees",
    tags=["Employee"]  
)

# Employee add API
@router.post("", status_code=status.HTTP_201_CREATED)
def create_employee(payload: Create_model, db: Session = Depends(get_db)):  
    new_emp = emp_crud.create_emp_in_db(db=db, emp_data=payload)
    return new_emp


# Employee fetch API
@router.get("", response_model=List[Get_model])
def get_employee(db: Session = Depends(get_db)):
    emp_list = emp_crud.get_emp_from_db(db=db)
    return emp_list


#Get employee by id
@router.get("{id}", response_model=Get_model)
def get_emp(id:int, db:Session=Depends(get_db)):
    db_employee = emp_crud.get_emp_by_ID_from_db(db=db, id=id)
    return db_employee