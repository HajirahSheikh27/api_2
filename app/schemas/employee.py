# # app/schemas/employee.py

# from pydantic import BaseModel, EmailStr

# class EmployeeCreate(BaseModel):
#     name: str
#     email: EmailStr
#     role: str

# class Employee(EmployeeCreate):
#     id: int

#     class Config:
#         orm_mode = True


# app/schemas/employee.py

from pydantic import BaseModel, EmailStr

class EmployeeCreate(BaseModel):
    name: str
    email: EmailStr
    role: str

class Employee(EmployeeCreate):
    id: int

    class Config:
        from_attributes = True
