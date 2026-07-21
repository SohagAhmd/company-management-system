from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from datetime import datetime, timezone
from app.schemas.user import UserCreate, UserLogin, RefreshTokenRequest
from app.models.user import User
from app.models.refresh_token import RefreshToken
from app.core.security.password import hash_password, verify_password
from app.core.security.jwt import create_access_token, create_refresh_token
from jose import JWTError, jwt
from app.core.security.jwt import SECRET_KEY, ALGORITHM


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

    # refresh token
    refresh_token, expires_at = create_refresh_token(data={"sub": str(user.id)})
    refresh_token_obj = RefreshToken(
        user_id=user.id, token=refresh_token, expires_at=expires_at
    )
    db.add(refresh_token_obj)
    db.commit()

    return {
        "access_token": access_token,
        "refresh_token": refresh_token,
        "token_type": "bearer",
        "message": "Login successful",
    }


# refresh_access_token
def refresh_access_token(db: Session, payload: RefreshTokenRequest):
    token = payload.refresh_token
    try:
        payload_data = jwt.decode(
            token,
            SECRET_KEY,
            algorithms=[ALGORITHM],
        )
    except JWTError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid refresh token",
        )

    user_id = payload_data.get("sub")

    if user_id is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid refresh token",
        )

    refresh_token = db.query(RefreshToken).filter(RefreshToken.token == token).first()

    if refresh_token is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Refresh token not found",
        )

    if refresh_token.is_revoked:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Refresh token has been revoked",
        )

    if refresh_token.expires_at.replace(tzinfo=timezone.utc) < datetime.now(
        timezone.utc
    ):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Refresh token expired",
        )

    access_token = create_access_token(data={"sub": str(user_id)})

    return {
        "access_token": access_token,
        "token_type": "bearer",
    }


# log out
def logout(db: Session, refresh_token: str):

    token = db.query(RefreshToken).filter(RefreshToken.token == refresh_token).first()

    if token is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Refresh token not found"
        )

    token.is_revoked = True

    db.commit()

    return {"message": "Logout successful"}
