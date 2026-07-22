from fastapi import FastAPI

# Import SQLAlchemy ORM models to register them with Base before creating tables
# Import API routers to include their endpoints in the main app
from app.routers import department, employee, user

# Initialize the FastAPI application with custom metadata for documentation
app = FastAPI(title="Company Management System API", version="1.0.0")

# Register routers so FastAPI can recognize and expose the defined API endpoints
app.include_router(employee.router)
app.include_router(department.router)
app.include_router(user.router)
# app.include_router(project.router)


# Root endpoint to quickly verify that the server is alive and responding
@app.get("/", tags=["Root"])
def root():
    # Return a structured JSON response instead of plain text for better frontend parsing
    return {"status": "success", "message": "Server is running successfully!"}
