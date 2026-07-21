from fastapi import APIRouter, status, Depends
from sqlalchemy.orm import Session

from app.database.db import get_db
from app.schemas.user import UserCreate, UserLogin, RefreshTokenRequest
from app.crud import user as user_crud


router = APIRouter(prefix="/auth", tags=["Authentication"])


@router.post("/sign-up", status_code=status.HTTP_201_CREATED)
def sign_up(payload: UserCreate, db: Session = Depends(get_db)):
    return user_crud.create_user(db=db, payload=payload)


@router.post("/login", status_code=status.HTTP_200_OK)
def login(payload: UserLogin, db: Session = Depends(get_db)):
    return user_crud.log_in(db=db, payload=payload)


@router.post("/refresh", status_code=status.HTTP_200_OK)
def refresh_access_token(payload: RefreshTokenRequest, db: Session = Depends(get_db)):
    return user_crud.refresh_access_token(db=db, payload=payload)


@router.post("/logout", status_code=status.HTTP_200_OK)
def logout(payload: RefreshTokenRequest, db: Session = Depends(get_db)):
    return user_crud.logout(db=db, refresh_token=payload.refresh_token)
