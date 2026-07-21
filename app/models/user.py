from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.sql import func
from app.database.db import Base
from sqlalchemy.orm import relationship


class User(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
    hashed_pass = Column(String, nullable=False)
    created_at = Column(DateTime, default=func.now())
<<<<<<< Updated upstream
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now())
=======
    updated_at = Column(
        DateTime,
        default=func.now(),
        onupdate=func.now(),
    )

    refresh_tokens = relationship(
        "RefreshToken",
        back_populates="user",
        cascade="all, delete-orphan",
    )
>>>>>>> Stashed changes
