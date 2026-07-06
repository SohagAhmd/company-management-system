from sqlalchemy.orm import Session
from app.schemas.employee import Create_model
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


# Employee fetch CURD
def get_emp_from_db(db:Session):
    employee_list = db.query(Employee).all()
    return employee_list
