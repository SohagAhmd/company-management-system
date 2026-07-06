from fastapi import FastAPI
from app.database.db import engine, Base
from app.models.employee import Employee
from app.models.department import Department
from app.models.project import Project

app = FastAPI()

#assigning all model in bd 
Base.metadata.create_all(bind=engine)

@app.get("/")
def root():
    return "Server is running..."