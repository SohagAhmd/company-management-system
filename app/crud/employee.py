from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from app.schemas.employee import Create_model, Update_model
from app.models.employee import Employee


# Employee create CURD
def create_emp_in_db(db:Session, emp_data:Create_model):
    new_emp = Employee(
        first_name = emp_data.first_name,
        last_name = emp_data.last_name,
        email = emp_data.email,
        phone = emp_data.phone,
        salary = emp_data.salary,
        job_title = emp_data.job_title,
        hire_date = emp_data.hire_date
    )
    db.add(new_emp)
    db.flush()
    db.commit()
    db.refresh(new_emp)
    return new_emp


# Get all employee CRUD
def get_emp_from_db(db:Session):
    employee_list = db.query(Employee).all()
    return employee_list


#Get employee by ID
def get_emp_by_ID_from_db(id:int, db:Session):
    db_employee = db.query(Employee).filter(Employee.id == id).first()

    if db_employee is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, 
            detail=f"Employee with id {id} not found"
        )
        
    return db_employee


#update employee data
def update_employ(id:int, db:Session, updated_data:Update_model):
    data_from_db = db.query(Employee).filter(Employee.id == id).first()

    if data_from_db is None:
        raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, 
                detail=f"Employee with id {id} not found"
            )

    data_from_db.first_name = updated_data.first_name
    data_from_db.last_name = updated_data.last_name
    data_from_db.email = updated_data.email
    data_from_db.phone = updated_data.phone
    data_from_db.salary = updated_data.salary
    data_from_db.job_title = updated_data.job_title
    data_from_db.hire_date = updated_data.hire_date

    db.add(data_from_db)
    db.commit()
    db.refresh(data_from_db)
    return data_from_db


#Delete employ from db
def delete_employee(id:int, db:Employee):
    employee = db.query(Employee).filter(Employee.id == id).first() 
    if employee is None:
        raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, 
                detail=f"Employee with id {id} not found"
            )

    db.delete(employee)
    db.commit()
