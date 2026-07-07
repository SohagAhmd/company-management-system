from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from app.models.department import Department
from app.schemas.department import Create_model, Get_model, Update_model


# Add department
def add_dep(db: Session, payload: Create_model):
    newDep = Department(name=payload.name)
    db.add(newDep)
    db.commit()
    db.refresh(newDep)
    return newDep


# get all Department
def get_Dep(db: Session):
    all_dep = db.query(Department).all()
    return all_dep


# Update Depertment
def update_dep(id: int, db: Session, playload: Update_model):
    dep = db.query(Department).filter(Department.id == id).first()

    if dep is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Department with id {id} not found",
        )

    update_dep.name = playload.name
    db.commit(dep)


# delete dep
def delete_dep(id: int, db: Session):
    dep = db.query(Department).filter(Department.id == id).first()

    if dep is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Department with id {id} not found",
        )

    db.delete(dep)
    db.commit()


# Get department by ID
def get_dep_by_ID(payload: int, db: Session):
    dep = db.query(Department).filter(Department.id == payload).first()

    if dep is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Department with id {payload} not found",
        )
    return dep
