from typing import List

from fastapi import Depends, HTTPException, status

from app.core.security.jwt import get_current_user
from app.models.user import User


def require_roles(roles: List[str]):

    def checker(
        current_user: User = Depends(get_current_user),
    ):
        if current_user.role not in roles:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="Permission denied",
            )

        return current_user

    return checker
