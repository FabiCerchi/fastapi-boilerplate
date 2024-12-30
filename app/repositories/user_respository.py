"""
This module contains the user repository class and interface
"""
from abc import abstractmethod
from fastapi import HTTPException, status
from pydantic import EmailStr
from sqlalchemy.orm import Session
from typing import Optional, Type

from app.schemas.user import UserCreate, UserUpdate
from app.repositories.base_repository import IRepository
from app.models.user import User
from app.utils.hashing import Hasher


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


class UserRepository(IUserRepository):
    """
    User repository Implementation
    """
    def __init__(self, db: Session):
        self.db = db

    def get(self, user_id: int) -> User:
        """
        Method to get a user by id
        :param user_id: int
        :return: User
        """
        user = self.db.query(User).filter(User.id == user_id).first()
        if not user:
            raise HTTPException(
                status_code = status.HTTP_404_NOT_FOUND,
                detail = f"User with id {user_id} not found"
            )
        return user

    def get_all(self) -> list[Type[User]]:
        """
        Method to get all users
        :return: List[User]
        """
        users = self.db.query(User).all()
        return users

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
        """
        Method to update a user
        :param user_id: int
        :param user: UserUpdate
        :return: User
        """
        user_to_update = self.db.query(User).filter(User.id == user_id).first()
        if not user_to_update:
            raise HTTPException(
                status_code = status.HTTP_404_NOT_FOUND,
                detail = f"User with id {user_id} not found"
            )
        try:
            user_to_update.email = user.email
            user_to_update.username = user.username
            user_to_update.address = user.address
            self.db.commit()
            self.db.refresh(user_to_update)
        except Exception as e:
            self.db.rollback()
            raise HTTPException(
                status_code = status.HTTP_409_CONFLICT,
                detail = f"Failed to update user: {e}"
            )
        return user_to_update

    def delete(self, user_id: int) -> bool:
        """
        Method to delete a user
        :param user_id:
        :return: bool
        """

        user_to_delete = self.db.query(User).filter(User.id == user_id).first()
        if not user_to_delete:
            raise HTTPException(
                status_code = status.HTTP_404_NOT_FOUND,
                detail = f"User with id {user_id} not found"
            )
        try:
            self.db.delete(user_to_delete)
            self.db.commit()
        except Exception as e:
            self.db.rollback()
            raise HTTPException(
                status_code = status.HTTP_409_CONFLICT,
                detail = f"Failed to delete user: {e}"
            )

        return True

    def get_user_by_email(self, email: EmailStr) -> Optional[User]:
        """
        Method to get user by email
        :param email: EmailStr
        :return: user | None
        """
        user = self.db.query(User).filter(User.email == email).first()
        if not user:
            return None

        return user
