from fastapi import HTTPException, status
from abc import abstractmethod
from pydantic import EmailStr
from sqlalchemy.orm import Session
from typing import List, Optional

from app.models.schemas.user import UserCreate, UserUpdate
from app.repositories.irepository import IRepository
from app.models.orm.user import User
from app.core.hashing import Hasher


class IUserRepository(IRepository):
    """
    User repository interface
    """

    @abstractmethod
    def get_user_by_email(self, email: str) -> Optional[User]:
        pass


class UserRepository(IUserRepository):
    """
    User repository Implementation
    """
    def __init__(self, db: Session):
        self.db = db

    def get(self, user_id: int) -> Optional[User]:
        pass

    def get_all(self) -> List[User]:
        pass

    def add(self, user: UserCreate) -> User:
        try:
            new_user = User(
                email=user.email,
                username=user.username,
                password=Hasher.get_password_hash(user.password),
                address= user.address,
            )
            self.db.add(new_user)
            self.db.commit()
            self.db.refresh(new_user)
        except Exception as e:
            self.db.rollback()
            raise HTTPException(
                status_code = status.HTTP_409_CONFLICT,
                detail = f"Failed to create user: {e}"
            )
        return new_user

    def update(self, user_id: int, user: UserUpdate) -> User:
        pass

    def delete(self, user_id: int) -> bool:
        pass

    def get_user_by_email(self, email: EmailStr) -> Optional[User]:
        pass
