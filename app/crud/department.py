from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from app.models.department import Department
from app.schemas.department import Create_model, Update_model


# Add department
def add_dep(db: Session, payload: Create_model):
    new_dep = Department(name=payload.name)
    db.add(new_dep)
    db.commit()
    db.refresh(new_dep)
    return new_dep


# Get all Department
def get_Dep(db: Session):
    all_dep = db.query(Department).all()
    return all_dep


# Get department by ID
def get_dep_by_ID(db: Session, dep_id: int):
    dep = db.query(Department).filter(Department.id == dep_id).first()

    if dep is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Department with id {dep_id} not found",
        )
    return dep


# Update Department
def update_dep(db: Session, dep_id: int, payload: Update_model):
    dep = db.query(Department).filter(Department.id == dep_id).first()

    if dep is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Department with id {dep_id} not found",
        )

    dep.name = payload.name
    db.commit()
    db.refresh(dep)
    return dep


# Delete department
def delete_dep(db: Session, dep_id: int):
    dep = db.query(Department).filter(Department.id == dep_id).first()

    if dep is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Department with id {dep_id} not found",
        )

    db.delete(dep)
    db.commit()
    return {"detail": f"Department with id {dep_id} successfully deleted"}
