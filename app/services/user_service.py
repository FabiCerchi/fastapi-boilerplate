"""
    This module contains the service class for user related operations
"""
from typing import Optional

from pydantic import EmailStr

from app.schemas.user import UserCreate, UserResponse, UserUpdate
from app.repositories.user_respository import IUserRepository

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
        new_user = self.user_repository.add(user)
        return new_user

    def get_users(self) -> list[UserResponse]:
        """
        Method to get all users
        :return: list[UserResponse]
        """
        users = self.user_repository.get_all()
        return users

    def get_user_by_id(self, user_id: int) -> UserResponse:
        """
        Method to get user by id
        :param user_id: int
        :return: UserResponse
        """
        user = self.user_repository.get(user_id)
        return user

    def delete_user(self, user_id: int) -> bool:
        """
        Method to delete a user
        :param user_id: int
        :return: bool
        """
        return self.user_repository.delete(user_id)

    def update_user(self, user_id: int, user: dict) -> UserResponse:
        """
        Method to update a user
        :param user_id: int
        :param user: UserUpdate
        :return: UserResponse
        """
        updated_user = self.user_repository.update(user_id, user)
        return updated_user

    def get_user_by_email(self, email: EmailStr) -> Optional[UserResponse]:
        """
        Method to get user by email
        :param email: EmailStr
        :return: UserResponse
        """
        user = self.user_repository.get_user_by_email(email)
        return user
