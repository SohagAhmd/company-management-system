from fastapi import APIRouter, Depends, status
from typing import List
from sqlalchemy.orm import Session

from app.schemas.department import Create_model, Get_model, Update_model
from app.database.db import get_db
from app.crud import department as dep_crud
from app.core.security.permissions import require_roles
from app.models.user import User


router = APIRouter(prefix="/api/v1/department", tags=["Department"])


# Create Department
# Access: Admin, HR
@router.post(
    "/",
    response_model=Get_model,
    status_code=status.HTTP_201_CREATED,
)
def add_dep(
    payload: Create_model,
    current_user: User = Depends(require_roles(["admin", "hr"])),
    db: Session = Depends(get_db),
):
    new_dep = dep_crud.add_dep(db=db, payload=payload)
    return new_dep


# Get All Departments
# Access: Admin, HR, User
@router.get("/", response_model=List[Get_model])
def get_all_dep(
    current_user: User = Depends(require_roles(["admin", "hr", "user"])),
    db: Session = Depends(get_db),
):
    dep_list = dep_crud.get_Dep(db=db)
    return dep_list


# Get Department By ID
# Access: Admin, HR, User
@router.get("/{id}", response_model=Get_model)
def get_dep_by_id(
    id: int,
    current_user: User = Depends(require_roles(["admin", "hr", "user"])),
    db: Session = Depends(get_db),
):
    dep = dep_crud.get_dep_by_ID(db=db, dep_id=id)
    return dep


# Update Department
# Access: Admin, HR
@router.put("/{id}", response_model=Get_model)
def update_dep(
    id: int,
    payload: Update_model,
    current_user: User = Depends(require_roles(["admin", "hr"])),
    db: Session = Depends(get_db),
):
    updated_dep = dep_crud.update_dep(db=db, dep_id=id, payload=payload)
    return updated_dep


# Delete Department
# Access: Admin Only
@router.delete("/{id}", status_code=status.HTTP_200_OK)
def delete_dep(
    id: int,
    current_user: User = Depends(require_roles(["admin"])),
    db: Session = Depends(get_db),
):
    result = dep_crud.delete_dep(db=db, dep_id=id)
    return result
