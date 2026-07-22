from datetime import datetime, timedelta, timezone

from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt
from sqlalchemy.orm import Session

from app.database.db import get_db
from app.models.user import User

SECRET_KEY = "09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 15
ACCESS_TOKEN_EXPIRE_DAYS = 30


# Access Token Generation
def create_access_token(data: dict):
    to_encode = data.copy()

    expire = datetime.now(timezone.utc) + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)

    to_encode.update({"exp": expire})

    access_token = jwt.encode(
        claims=to_encode,
        key=SECRET_KEY,
        algorithm=ALGORITHM,
    )

    return access_token


# Refresh Token Generation
def create_refresh_token(data: dict):
    to_encode = data.copy()
    expire = datetime.now(timezone.utc) + timedelta(days=ACCESS_TOKEN_EXPIRE_DAYS)
    to_encode.update({"exp": expire})
    refresh_token = jwt.encode(claims=to_encode, algorithm=ALGORITHM, key=SECRET_KEY)

    return refresh_token, expire


# Extract JWT Token From Authorization Header
oauth2_scheme = OAuth2PasswordBearer(
    tokenUrl="/login",
)


# Authentication Exception
credentials_exception = HTTPException(
    status_code=status.HTTP_401_UNAUTHORIZED,
    detail="Invalid authentication credentials",
)


# Get Current Authenticated User
def get_current_user(
    token: str = Depends(oauth2_scheme),
    db: Session = Depends(get_db),
):
    try:
        payload = jwt.decode(
            token=token,
            key=SECRET_KEY,
            algorithms=[ALGORITHM],
        )

        user_id = payload.get("sub")

        if user_id is None:
            raise credentials_exception

    except JWTError:
        raise credentials_exception

    user = db.query(User).filter(User.id == int(user_id)).first()

    if not user:
        raise credentials_exception

    return user
