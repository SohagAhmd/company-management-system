from typing import List

from fastapi import APIRouter, Depends, status, Query
from sqlalchemy.orm import Session

from app.crud import employee as emp_crud
from app.database.db import get_db
from app.models.user import User
from app.schemas.employee import Create_model, Get_model, Update_model, EmployeePaginationResponse
from app.core.security.permissions import require_roles


router = APIRouter(
    prefix="/api/v1/employees",
    tags=["Employee"],
)


# Create Employee
# Access: Admin, HR
@router.post(
    "/",
    response_model=Get_model,
    status_code=status.HTTP_201_CREATED,
)
def create_employee(
    payload: Create_model,
    current_user: User = Depends(require_roles(["admin", "hr"])),
    db: Session = Depends(get_db),
):
    return emp_crud.create_emp_in_db(
        db=db,
        payload=payload,
    )


# Get All Employees
# Access: Admin, HR, User
@router.get(
    "/",response_model=List[EmployeePaginationResponse],
)
def get_employee(
    page: int = Query(1, ge=1),
    size: int = Query(10, ge=1, le=100),
    current_user: User = Depends(require_roles(["admin", "hr", "user"])),
    db: Session = Depends(get_db),
):
    return emp_crud.get_emp_from_db(page=page, size=size, db=db)


# Get Employee By ID
# Access: Admin, HR, User
@router.get(
    "/{id}",
    response_model=Get_model,
)
def get_emp(
    id: int,
    current_user: User = Depends(require_roles(["admin", "hr", "user"])),
    db: Session = Depends(get_db),
):
    return emp_crud.get_emp_by_ID_from_db(
        db=db,
        emp_id=id,
    )


# Update Employee
# Access: Admin, HR
@router.put(
    "/{id}",
    response_model=Get_model,
)
def update_employee(
    id: int,
    payload: Update_model,
    current_user: User = Depends(require_roles(["admin", "hr"])),
    db: Session = Depends(get_db),
):
    return emp_crud.update_employ(
        db=db,
        emp_id=id,
        payload=payload,
    )


# Delete Employee
# Access: Admin Only
@router.delete(
    "/{id}",
    status_code=status.HTTP_200_OK,
)
def delete_employee(
    id: int,
    current_user: User = Depends(require_roles(["admin"])),
    db: Session = Depends(get_db),
):
    emp_crud.delete_employee(
        db=db,
        emp_id=id,
    )

    return {"message": f"Employee with ID {id} is successfully deleted!"}
