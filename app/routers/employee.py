from typing import List

from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from app.core.security.jwt import get_current_user
from app.crud import employee as emp_crud
from app.database.db import get_db
from app.models.user import User
from app.schemas.employee import Create_model, Get_model, Update_model

router = APIRouter(
    prefix="/api/v1/employees",
    tags=["Employee"],
)


# Employee add API
@router.post("/", response_model=Get_model, status_code=status.HTTP_201_CREATED)
def create_employee(
    payload: Create_model,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    return emp_crud.create_emp_in_db(db=db, payload=payload)


# Employee fetch API
@router.get("/", response_model=List[Get_model])
def get_employee(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    return emp_crud.get_emp_from_db(db=db)


# Get employee by ID
@router.get("/{id}", response_model=Get_model)
def get_emp(
    id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    return emp_crud.get_emp_by_ID_from_db(db=db, emp_id=id)


# Update Employee data
@router.put("/{id}", response_model=Get_model)
def update_employee(
    id: int,
    payload: Update_model,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    return emp_crud.update_employ(
        db=db,
        emp_id=id,
        payload=payload,
    )


# Delete Employee
@router.delete("/{id}", status_code=status.HTTP_200_OK)
def delete_employee(
    id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    emp_crud.delete_employee(db=db, emp_id=id)

    return {"message": f"Employee with ID {id} is successfully deleted!"}
