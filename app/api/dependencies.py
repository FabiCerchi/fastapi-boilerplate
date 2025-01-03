"""
This module contains the dependencies for the API.
"""
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session


from app.utils.oauth import OAuth
from app.utils.token import Token
from app.db.database import get_db
from app.repositories.user_respository import UserRepository
from app.repositories.auth_repository import AuthRepository
from app.services.user_service import UserService
from app.services.auth_service import AuthService

# Instancia global para extraer tokens
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/login")

# Instancia de OAuth
oauth_service = OAuth(Token())

def get_current_user(token: str = Depends(oauth2_scheme)):
    """
    Función que inyecta la dependencia para los endpoints.
    """
    try:
        return oauth_service.get_current_user(token)
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail=str(e),
            headers={"WWW-Authenticate": "Bearer"},
        )

def get_user_service(db: Session = Depends(get_db)) -> UserService:
    """
    Function to get user service
    :param db:
    :param UserService:
    """
    repo = UserRepository(db)
    return UserService(repo)

def get_auth_service(db: Session = Depends(get_db)) -> AuthService:
    """
    Function to get auth service
    :param db:
    :param AuthService:
    """
    repo = AuthRepository(db)
    return AuthService(repo)
