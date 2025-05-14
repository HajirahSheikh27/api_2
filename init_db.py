# init_db.py

import sys
import os
from app.db.db import engine
from app.models.employee import Employee

# Add the root directory of your project to the sys.path
sys.path.append(os.path.abspath(os.path.dirname(__file__)))

# Create the tables in the database
Employee.metadata.create_all(bind=engine)


