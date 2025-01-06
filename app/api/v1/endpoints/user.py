"""
User endpoints
"""
from multiprocessing.managers import Value
from typing import Optional

from fastapi import APIRouter, Depends, status, HTTPException
from pydantic import EmailStr
from sqlalchemy.orm import Query

from app.core.exceptions import *
from app.schemas.pagination import PaginationParams
from app.schemas.token import TokenData
from app.schemas.user import UserCreate, UserResponse, UserUpdate, UserPaginatedResponse
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
    try:
        new_user = user_service.create_user(user)
    except UserAlreadyExistsError as e:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail=str(e)
        )
    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(e)
        )
    except RepositoryError as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=str(e)
        )

    return new_user

@user_router.get(
    "/",
    status_code=status.HTTP_200_OK,
    response_model=UserPaginatedResponse,
    response_description="List of users"
)
async def get_users(
        pagination: PaginationParams = Depends(),
        user_service: UserService = Depends(get_user_service),
        current_user: TokenData = Depends(get_current_user),
):
    """
    Get a list of users
        :param pagination:
        :param user_service: UserService
        :param current_user: TokenData
        :return: list[UserResponse]
    """
    limit = pagination.limit
    offset = pagination.offset
    try:
        users, count = user_service.get_users(limit, offset)
        metadata = {
            "total_count": count,
            "limit": limit,
            "offset": offset,
            "current_page": (offset // limit) + 1,
            "total_pages": (count // limit) + (1 if count % limit > 0 else 0),
        }
    except RepositoryError as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=str(e)
        )

    users_response = UserPaginatedResponse(metadata=metadata, data=users)

    return users_response

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
    try:
        user = user_service.get_user_by_id(user_id)
    except ItemNotFoundError as e:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=str(e)
        )
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

    # Check si el user que se quiere eliminar es el mismo que el que está logueado
    if current_user.id != user_id:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="You can only delete your own user"
        )

    try:
        response = user_service.delete_user(user_id)
    except RepositoryError as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=str(e)
        )

    return response

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

    # Check si el user que se quiere actualizar es el mismo que el que está logueado
    if current_user.id != user_id:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="You can only update your own user"
        )

    try:
        updated_user = user_service.update_user(user_id, user)
    except ItemNotFoundError as e:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=str(e)
        )
    except UserAlreadyExistsError as e:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail=str(e)
        )
    except RepositoryError as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=str(e)
        )

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

    try:
        user = user_service.get_user_by_email(email)
    except ItemNotFoundError as e:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=str(e)
        )
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail=str(e)
        )

    return user