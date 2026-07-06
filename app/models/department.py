from sqlalchemy import Column, Integer, String, Float, DateTime 
from sqlalchemy.sql import func
from app.database.db import Base

class Department(Base):
    __tablename__ = "department"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100), nullable=False)
    location = Column(String(255), nullable=False)
    budget = Column(Float, default=0.0)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())

