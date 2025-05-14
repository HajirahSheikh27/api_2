# from fastapi import APIRouter, Depends, HTTPException
# from sqlalchemy.orm import Session
# from app.db import get_db
# from app.models.employee import Employee as EmployeeModel
# from app.schemas.employee import Employee as EmployeeSchema, EmployeeCreate

# router = APIRouter(
#     prefix="/employees",
#     tags=["employees"]
# )

# @router.get("/{employee_id}", response_model=EmployeeSchema)
# def read_employee(employee_id: int, db: Session = Depends(get_db)):
#     employee = db.query(EmployeeModel).filter(EmployeeModel.id == employee_id).first()
#     if employee is None:
#         raise HTTPException(status_code=404, detail="Employee not found")
#     return employee

# @router.post("/", response_model=EmployeeSchema)
# def create_employee(employee: EmployeeCreate, db: Session = Depends(get_db)):
#     db_employee = EmployeeModel(name=employee.name, job_title=employee.job_title, email="placeholder@example.com")
#     db.add(db_employee)
#     db.commit()
#     db.refresh(db_employee)
#     return db_employee


# app/routes/employee.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas.employee import EmployeeCreate, Employee
from app.models import employee as model
from app.db import get_db

router = APIRouter()

router = APIRouter(prefix="/employees", tags=["Employees"])

@router.post("/", response_model=Employee)
def create_new_employee(emp: EmployeeCreate, db: Session = Depends(get_db)):
    return model.create_employee(db=db, name=emp.name, email=emp.email, role=emp.role)

@router.get("/{employee_id}", response_model=Employee)
def read_employee(employee_id: int, db: Session = Depends(get_db)):
    db_employee = model.get_employee(db, employee_id)
    if not db_employee:
        raise HTTPException(status_code=404, detail="Employee not found")
    return db_employee

@router.put("/{employee_id}", response_model=Employee)
def update_employee(employee_id: int, emp: EmployeeCreate, db: Session = Depends(get_db)):
    updated_employee = model.update_employee(db, employee_id, emp)
    if not updated_employee:
        raise HTTPException(status_code=404, detail="Employee not found")
    return updated_employee

@router.patch("/{employee_id}", response_model=Employee)
def partial_update_employee(employee_id: int, emp: EmployeeCreate, db: Session = Depends(get_db)):
    updated_employee = model.partial_update_employee(db, employee_id, emp)
    if not updated_employee:
        raise HTTPException(status_code=404, detail="Employee not found")
    return updated_employee

@router.delete("/{employee_id}")
def delete_employee(employee_id: int, db: Session = Depends(get_db)):
    success = model.delete_employee(db, employee_id)
    if not success:
        raise HTTPException(status_code=404, detail="Employee not found")
    return {"detail": "Employee deleted successfully"}

#Example endpoint: Get all employees
@router.get("/employees")
def get_employees(db: Session = Depends(get_db)):
    employees = db.query(Employee).all()
    return employees