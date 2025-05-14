from sqlalchemy.orm import Session
from app.db import Base  # or from ... depending on your structure

from app.schemas.employee import EmployeeCreate

# def create_employee(db: Session, name: str, email: str, role: str):
#     db_employee = Employee(name=name, email=email, role=role)
#     db.add(db_employee)
#     db.commit()
#     db.refresh(db_employee)
#     return db_employee

# def get_employee(db: Session, employee_id: int):
#     return db.query(Employee).filter(Employee.id == employee_id).first()

# def update_employee(db: Session, employee_id: int, emp_data: EmployeeCreate):
#     employee = db.query(Employee).filter(Employee.id == employee_id).first()
#     if not employee:
#         return None
#     employee.name = emp_data.name
#     employee.email = emp_data.email
#     employee.role = emp_data.role
#     db.commit()
#     db.refresh(employee)
#     return employee

# def partial_update_employee(db: Session, employee_id: int, emp_data: EmployeeCreate):
#     employee = db.query(Employee).filter(Employee.id == employee_id).first()
#     if not employee:
#         return None
#     if emp_data.name is not None:
#         employee.name = emp_data.name
#     if emp_data.email is not None:
#         employee.email = emp_data.email
#     if emp_data.role is not None:
#         employee.role = emp_data.role
#     db.commit()
#     db.refresh(employee)
#     return employee

# def delete_employee(db: Session, employee_id: int):
#     employee = db.query(Employee).filter(Employee.id == employee_id).first()
#     if not employee:
#         return False
#     db.delete(employee)
#     db.commit()
#     return True


def create_employee(db: Session, name: str, email: str, role: str):
    if not name or not email or not role:
        raise ValueError("Name, email, and role must not be empty")
    db_employee = Employee(name=name, email=email, role=role)
    db.add(db_employee)
    db.commit()
    db.refresh(db_employee)
    return db_employee


def get_employee(db: Session, employee_id: int):
    if not isinstance(employee_id, int):
        raise ValueError("Employee ID must be an integer")
    return db.query(Employee).filter(Employee.id == employee_id).first()


def update_employee(db: Session, employee_id: int, emp_data: EmployeeCreate):
    if not isinstance(employee_id, int):
        raise ValueError("Employee ID must be an integer")
    if not emp_data.name or not emp_data.email or not emp_data.role:
        raise ValueError("Name, email, and role must not be empty")
    employee = db.query(Employee).filter(Employee.id == employee_id).first()
    if not employee:
        return None
    employee.name = emp_data.name
    employee.email = emp_data.email
    employee.role = emp_data.role
    db.commit()
    db.refresh(employee)
    return employee


def partial_update_employee(db: Session, employee_id: int, emp_data: EmployeeCreate):
    if not isinstance(employee_id, int):
        raise ValueError("Employee ID must be an integer")
    employee = db.query(Employee).filter(Employee.id == employee_id).first()
    if not employee:
        return None
    if emp_data.name is not None:
        employee.name = emp_data.name
    if emp_data.email is not None:
        employee.email = emp_data.email
    if emp_data.role is not None:
        employee.role = emp_data.role
    db.commit()
    db.refresh(employee)
    return employee


def delete_employee(db: Session, employee_id: int):
    if not isinstance(employee_id, int):
        raise ValueError("Employee ID must be an integer")
    employee = db.query(Employee).filter(Employee.id == employee_id).first()
    if not employee:
        return False
    db.delete(employee)
    db.commit()
    return True
