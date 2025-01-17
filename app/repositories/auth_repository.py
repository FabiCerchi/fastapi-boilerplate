"""
This module contains the repository class for the authentication feature.
"""
from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from app.schemas.auth import Login
from app.models.user import User
from app.utils.hashing import Hasher
from app.utils.token import Token
from app.schemas.token import TokenResponse


class AuthRepository:
    """
    Auth repository class
    """
    def __init__(self, db: Session):
        self.db = db

    def auth_user(self, login: Login) -> TokenResponse:
        user = self.db.query(User).filter(User.username == login.username).first()

        if not user:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Invalid credentials"
            )

        if not Hasher.verify_password(login.password, user.password):
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid credentials"
            )

        try:
            token = Token.generate_token(
                data = {"sub": user.username, "id": user.id, "is_superuser": user.is_superuser, "active": user.active}
            )
        except Exception as e:
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail=f"Failed to generate token: {e}"
            )

        token = TokenResponse(access_token=token, token_type="bearer")
        return token
