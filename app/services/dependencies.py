from fastapi import Depends
from sqlalchemy.orm import Session

from app.db.database import get_db
from app.repositories.user_respository import UserRepository
from app.repositories.auth_repository import AuthRepository
from app.services.user_service import UserService
from app.services.auth_service import AuthService


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
