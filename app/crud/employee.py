# from sqlalchemy.orm import Session
# from app.models.employee import Employee
# from app.schemas.employee import Employee, EmployeeCreate



# def get_employee(db: Session, employee_id: int):
#     return db.query(Employee).filter(Employee.id == employee_id).first()

# def create_employee(db: Session, name: str, job_title: str, email: str):
#     db_employee = Employee(name=name, job_title=job_title, email=email)
#     db.add(db_employee)
#     db.commit()
#     db.refresh(db_employee)
#     return db_employee


from sqlalchemy.orm import Session
from app.schemas.employee import EmployeeCreate
from app.models.employee import Employee
from app.utils.logger import logger


def create_employee(db: Session, name: str, email: str, role: str):
    db_employee = Employee(name=name, email=email, role=role)
    db.add(db_employee)
    db.commit()
    db.refresh(db_employee)
    logger.info(f"Employee created: {db_employee.id} | {name} | {email} | {role}")
    return db_employee


def get_employee(db: Session, employee_id: int):
    employee = db.query(Employee).filter(Employee.id == employee_id).first()
    if employee:
        logger.info(f"Employee retrieved: ID {employee_id}")
    else:
        logger.warning(f"Employee not found: ID {employee_id}")
    return employee


def update_employee(db: Session, employee_id: int, emp_data: EmployeeCreate):
    employee = db.query(Employee).filter(Employee.id == employee_id).first()
    if not employee:
        logger.warning(f"Update failed: Employee ID {employee_id} not found")
        return None
    employee.name = emp_data.name
    employee.email = emp_data.email
    employee.role = emp_data.role
    db.commit()
    db.refresh(employee)
    logger.info(f"Employee updated: ID {employee_id}")
    return employee


def partial_update_employee(db: Session, employee_id: int, emp_data: EmployeeCreate):
    employee = db.query(Employee).filter(Employee.id == employee_id).first()
    if not employee:
        logger.warning(f"Partial update failed: Employee ID {employee_id} not found")
        return None
    if emp_data.name is not None:
        employee.name = emp_data.name
    if emp_data.email is not None:
        employee.email = emp_data.email
    if emp_data.role is not None:
        employee.role = emp_data.role
    db.commit()
    db.refresh(employee)
    logger.info(f"Employee partially updated: ID {employee_id}")
    return employee


def delete_employee(db: Session, employee_id: int):
    employee = db.query(Employee).filter(Employee.id == employee_id).first()
    if not employee:
        logger.warning(f"Delete failed: Employee ID {employee_id} not found")
        return False
    db.delete(employee)
    db.commit()
    logger.info(f"Employee deleted: ID {employee_id}")
    return True
