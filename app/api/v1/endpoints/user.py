"""
User endpoints
"""
from typing import Optional

from fastapi import APIRouter, Depends, status
from pydantic import EmailStr

from app.schemas.token import TokenData
from app.schemas.user import UserCreate, UserResponse, UserUpdate
from app.services.user_service import UserService
from app.api.dependencies import get_user_service
from app.api.dependencies import get_current_user

user_router = APIRouter(prefix='/users', tags=['Users'])


@user_router.post(
    "/",
    status_code=status.HTTP_201_CREATED,
    response_model=UserResponse,
    response_description="User created successfully"
)
async def create_user(
        user: UserCreate,
        user_service: UserService = Depends(get_user_service),
):
    """
    Create a new user
        :param user: UserCreate
        :param user_service: UserService
        :param current_user: TokenData
        :return: UserResponse
    """
    new_user = user_service.create_user(user)
    return new_user

@user_router.get(
    "/",
    status_code=status.HTTP_200_OK,
    response_model=list[UserResponse],
    response_description="List of users"
)
async def get_users(
        user_service: UserService = Depends(get_user_service),
        current_user: TokenData = Depends(get_current_user),
):
    """
    Get a list of users
        :param user_service: UserService
        :param current_user: TokenData
        :return: list[UserResponse]
    """
    users = user_service.get_users()
    return users

@user_router.get(
    "/{user_id}",
    status_code=status.HTTP_200_OK,
    response_model=UserResponse,
    response_description="User retrieved successfully"
)
async def get_user_by_id(
        user_id: int,
        user_service: UserService = Depends(get_user_service),
        current_user: TokenData = Depends(get_current_user),
):
    """
    Get a user by id
        :param user_id: int
        :param user_service: UserService
        :param current_user: TokenData
        :return: UserResponse
    """
    user = user_service.get_user_by_id(user_id)
    return user

@user_router.delete(
    "/{user_id}",
    status_code=status.HTTP_204_NO_CONTENT,
    response_description="User deleted successfully"
)
async def delete_user(
        user_id: int,
        user_service: UserService = Depends(get_user_service),
        current_user: TokenData = Depends(get_current_user),
):
    """
    Delete a user
        :param user_id: int
        :param user_service: UserService
        :param current_user:
        :return: bool
    """
    return user_service.delete_user(user_id)

@user_router.put(
    "/{user_id}",
    status_code=status.HTTP_200_OK,
    response_model=UserResponse,
    response_description="User updated successfully"
)
async def update_user(
        user_id: int,
        user: UserUpdate,
        user_service: UserService = Depends(get_user_service),
        current_user: TokenData = Depends(get_current_user),
):
    """
    Update a user
        :param user_id: int
        :param user: UserUpdate
        :param user_service: UserService
        :param current_user: TokenData
        :return: UserResponse
    """
    updated_user = user_service.update_user(user_id, user)
    return updated_user

@user_router.get(
    "/email/{email}",
    status_code=status.HTTP_200_OK,
    response_model=Optional[UserResponse],
    response_description="User retrieved successfully"
)
async def get_user_by_email(
        email: EmailStr,
        user_service: UserService = Depends(get_user_service),
        current_user: TokenData = Depends(get_current_user),
):
    """
    Get a user by email
        :param email: EmailStr
        :param user_service: UserService
        :param current_user: TokenData
        :return: UserResponse
    """
    user = user_service.get_user_by_email(email)
    return user