from fastapi import HTTPException, status
from sqlalchemy.orm import Session, selectinload
from sqlalchemy import func
from app.models.employee import Employee
from app.schemas.employee import Create_model, Update_model


# Employee create CRUD
def create_emp_in_db(db: Session, payload: Create_model):
    new_emp = Employee(
        first_name=payload.first_name,
        last_name=payload.last_name,
        email=payload.email,
        phone=payload.phone,
        salary=payload.salary,
        job_title=payload.job_title,
        hire_date=payload.hire_date,
        department_id=payload.department_id,
    )
    db.add(new_emp)
    db.flush()
    db.commit()
    db.refresh(new_emp)
    return new_emp


# Get all employee CRUD
def get_emp_from_db(page: int, size: int, db: Session):
    offset = (page - 1) * size

    db_employee_list = (
        db.query(Employee)
        .options(selectinload(Employee.department))
        .offset(offset)
        .limit(size)
        .all()
    )

    total_data = (
        db.query(func.count(Employee.id))
        .scalar()
    )

    return {
        "total": total_data,
        "items": db_employee_list
    }


# Get employee by ID
def get_emp_by_ID_from_db(db: Session, emp_id: int):
    db_employee = db.query(Employee).filter(Employee.id == emp_id).first()

    if db_employee is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Employee with id {emp_id} not found",
        )

    return db_employee


# Update employee data
def update_employ(db: Session, emp_id: int, payload: Update_model):
    data_from_db = db.query(Employee).filter(Employee.id == emp_id).first()

    if data_from_db is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Employee with id {emp_id} not found",
        )

    data_from_db.first_name = payload.first_name
    data_from_db.last_name = payload.last_name
    data_from_db.email = payload.email
    data_from_db.phone = payload.phone
    data_from_db.salary = payload.salary
    data_from_db.job_title = payload.job_title
    data_from_db.hire_date = payload.hire_date
    data_from_db.department_id = payload.department_id

    db.add(data_from_db)
    db.commit()
    db.refresh(data_from_db)
    return data_from_db


# Delete employee from db
def delete_employee(db: Session, emp_id: int):
    employee = db.query(Employee).filter(Employee.id == emp_id).first()

    if employee is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Employee with id {emp_id} not found",
        )

    db.delete(employee)
    db.commit()
    return {"detail": f"Employee with id {emp_id} successfully deleted"}
