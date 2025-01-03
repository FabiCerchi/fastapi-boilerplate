"""
    This module contains the service class for user related operations
"""
from typing import Optional

from pydantic import EmailStr

from app.core.exceptions import ItemNotFoundError, UserAlreadyExistsError
from app.schemas.user import UserCreate, UserResponse, UserUpdate
from app.repositories.user_respository import IUserRepository
from app.utils.hashing import Hasher


class UserService:
    """
        Service class for user related operations
    """
    def __init__(self, user_repository: IUserRepository):
        """
        Constructor for UserService class
        :param user_repository: IUserRepository
        """
        self.user_repository = user_repository

    def create_user(self, user: UserCreate) -> UserResponse:
        """
        Method to create a new user
        :param user: UserCreate
        :return: UserResponse
        """

        existing_user = self.get_user_by_username_or_email(user.username, user.email)
        if existing_user:
            if existing_user.email == user.email:
                raise UserAlreadyExistsError('email', user.email)
            elif existing_user.username == user.username:
                raise UserAlreadyExistsError('username', user.username)

        user.password = Hasher.get_password_hash(user.password)
        created_user = self.user_repository.add(user)
        return UserResponse.model_validate(created_user)

    def get_users(self) -> list[UserResponse]:
        """
        Method to get all users
        :return: list[UserResponse]
        """
        # Check if exist users
        users = self.user_repository.get_all()
        return users

    def get_user_by_id(self, user_id: int) -> UserResponse:
        """
        Method to get user by id
        :param user_id: int
        :return: UserResponse
        """
        user = self.user_repository.get(user_id)
        if user is None:
            raise ItemNotFoundError('user', user_id)

        return user

    def delete_user(self, user_id: int) -> bool:
        """
        Method to delete a user
        :param user_id: int
        :return: bool
        """
        # Check if user exists
        return self.user_repository.delete(user_id)

    def update_user(self, user_id: int, user: UserUpdate) -> UserResponse:
        """
        Method to update a user
        :param user_id: int
        :param user: UserUpdate
        :return: UserResponse
        """
        exist  = self.user_repository.get(user_id)
        if not exist:
            raise ItemNotFoundError('user', user_id)

        try:
            updated_user = self.user_repository.update(user_id, user)
        except Exception as e:
            raise Exception(f"Failed to update user: {e}")

        return updated_user

    def get_user_by_email(self, email: EmailStr) -> Optional[UserResponse]:
        """
        Method to get user by email
        :param email: EmailStr
        :return: UserResponse
        """
        user = self.user_repository.get_user_by_email(email)
        if not user:
            raise ItemNotFoundError('user', email)
        return user

    def get_user_by_username_or_email(self, username: str, email: str) -> Optional[UserResponse]:
        """
        Method to get user by username or email
        :param username: str
        :param email: str
        :return: UserResponse
        """
        user = self.user_repository.get_user_by_username_or_email(username, email)

        return user
