# app/main.py
# from fastapi import FastAPI
# from app.routes import employee
# from app.models import employee  # make sure this imports your models


# app = FastAPI(
#     title="Employee Management System",
#     description="A FastAPI-based backend to manage employees.",
#     version="1.0.0"
# )

# app.include_router(employee.router)



from fastapi import FastAPI
from app.routes import employee  # Import the employee router

app = FastAPI()

# Include the employee router
app.include_router(employee.router)

# You can include other routers here as well
