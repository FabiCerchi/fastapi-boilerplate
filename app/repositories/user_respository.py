"""
This module contains the user repository class and interface
"""

from abc import abstractmethod
from pydantic import EmailStr
from sqlalchemy.orm import Session
from sqlalchemy import or_
from typing import Optional, Type

from app.core.exceptions import RepositoryError
from app.schemas.user import UserCreate, UserUpdate
from app.repositories.base_repository import IRepository
from app.models.user import User


class IUserRepository(IRepository):
    """
    User repository interface
    """

    @abstractmethod
    def get_user_by_email(self, email: EmailStr) -> Optional[User]:
        """
        Method to get user by email
        :param email: EmailStr
        :return: user | None
        """
        pass

    @abstractmethod
    def get_user_by_username_or_email(self, username: str, email: str) -> Optional[User]:
        """
        Method to get user by username or email
        :param username: str
        :param email: str
        :return: user | None
        """
        pass

    @abstractmethod
    def count(self) -> int:
        """
        Method to count entities
        :return: int
        """
        pass

class UserRepository(IUserRepository):
    """
    User repository Implementation
    """
    def __init__(self, db: Session):
        self.db = db

    def get(self, user_id: int) -> Optional[User]:
        """
        Method to get a user by id
        :param user_id: int
        :return: User
        """
        return self.db.query(User).filter(User.id == user_id).first()

    def get_all(self, limit: int, offset: int) -> list[Type[User]]:
        """
        Method to get all users
        :return: List[User]
        """
        try:
            users = self.db.query(User).offset(offset).limit(limit).all()
        except Exception as e:
            raise RepositoryError(f"Failed to get users: {e}")
        return users

    def count(self) -> int:
        """
        Method to count users
        :return: int
        """
        return self.db.query(User).count()

    def add(self, user: UserCreate) -> User:
        """
        Method to add a new user
        :param user: UserCreate
        :return: User
        """
        try:
            new_user = User(
                email=user.email,
                username=user.username,
                password=user.password,
                address= user.address,
            )
            self.db.add(new_user)
            self.db.commit()
            self.db.refresh(new_user)
        except Exception as e:
            self.db.rollback()
            raise RepositoryError(f"Failed to create user: {e}")
        return new_user

    def update(self, user_id: int, user: UserUpdate) -> User:
        """
        Method to update a user
        :param user_id: int
        :param user: UserUpdate
        :return: User
        """

        user_to_update = self.db.query(User).filter(User.id == user_id).first()
        try:
            for key, value in user.model_dump(exclude_unset=True).items():
                setattr(user_to_update, key, value)
            self.db.commit()
        except Exception as e:
            self.db.rollback()
            raise RepositoryError(f'Failed to update user: {e}')
        return user_to_update

    def delete(self, user_id: int) -> bool:
        """
        Method to delete a user
        :param user_id:
        :return: bool
        """

        user_to_delete = self.db.query(User).filter(User.id == user_id).first()
        try:
            self.db.delete(user_to_delete)
            self.db.commit()
        except Exception as e:
            self.db.rollback()
            raise RepositoryError(f"Failed to delete user: {e}")
        return True

    def get_user_by_email(self, email: EmailStr) -> Optional[User]:
        """
        Method to get user by email
        :param email: EmailStr
        :return: user | None
        """

        return self.db.query(User).filter(User.email == email).first()

    def get_user_by_username_or_email(self, username: str, email: str) -> Optional[User]:
        """
        Method to get user by username or email
        :param username: str
        :param email: str
        :return: user | None
        """

        return self.db.query(User).filter(or_(User.username == username, User.email == email)).first()
