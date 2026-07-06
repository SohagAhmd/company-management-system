from fastapi import FastAPI
from app.database.db import engine, Base

# Import SQLAlchemy ORM models to register them with Base before creating tables
from app.models.employee import Employee
from app.models.department import Department
from app.models.project import Project

# Import API routers to include their endpoints in the main app
from app.routers import employee

# Initialize the FastAPI application with custom metadata for documentation
app = FastAPI(
    title="Company Management System API", 
    version="1.0.0"
)

# Register routers so FastAPI can recognize and expose the defined API endpoints
app.include_router(employee.router)

# Automatically create all registered database tables inside the SQLite file
Base.metadata.create_all(bind=engine)

# Root endpoint to quickly verify that the server is alive and responding
@app.get("/", tags=["Root"])
def root():
    # Return a structured JSON response instead of plain text for better frontend parsing
    return {"status": "success", "message": "Server is running successfully!"}
