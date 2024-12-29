from fastapi import Depends
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.repositories.user_respository import UserRepository
from app.services.user_service import UserService

def get_user_service(db: Session = Depends(get_db)) -> UserService:
    """
    Function to get user service
    :param db:
    :param UserService:
    """
    repo = UserRepository(db)
    return UserService(repo)
