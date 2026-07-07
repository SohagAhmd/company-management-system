from fastapi import APIRouter, Depends, status
from typing import List
from sqlalchemy.orm import Session
from app.schemas.department import Create_model, Get_model, Update_model
from app.database.db import get_db
from app.crud import department as dep_crud

router = APIRouter(prefix="/api/v1/department", tags=["Department"])


# add department
@router.post("/", status_code=status.HTTP_201_CREATED)
def add_dep(payload: Create_model, db: Session = Depends(get_db)):
    new_dep = dep_crud.add_dep(db=db, payload=payload)
    return new_dep


# get all department
@router.get("/", response_model=List[Get_model])
def get_all_dep(db: Session = Depends(get_db)):
    dep_list = dep_crud.get_Dep(db=db)
    return dep_list


# get department by id
@router.get("/{id}", response_model=Get_model)
def get_dep_by_id(id: int, db: Session = Depends(get_db)):
    dep = dep_crud.get_dep_by_ID(db=db, payload=id)
    return dep
