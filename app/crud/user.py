from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from app.schemas.user import UserCreate, UserLogin
from app.models.user import User
from app.core.security.password import hash_password, verify_password
from app.core.security.jwt import create_access_token


# Create User
def create_user(db: Session, payload: UserCreate):
    existing_user = db.query(User).filter(User.email == payload.email).first()
    # Hasing plain password
    hash_pass = hash_password(payload.password)

    print(payload.password)
    print(type(payload.password))

    if existing_user is not None:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="Email already registered"
        )

    new_user = User(
        name=payload.name,
        email=payload.email,
        hashed_pass=hash_pass,
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


# log in User
def log_in(db: Session, payload: UserLogin):
    user = db.query(User).filter(User.email == payload.email).first()

    if not user or not verify_password(payload.password, user.hashed_pass):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid email or password"
        )

    access_token = create_access_token(data={"sub": str(user.id)})

    return {
        "access_token": access_token,
        "token_type": "bearer",
        "message": "Login successful",
    }
