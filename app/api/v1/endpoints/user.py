from fastapi import APIRouter, Depends, status

from app.schemas.token import TokenData
from app.schemas.user import UserCreate, UserResponse
from app.services.user_service import UserService
from app.services.dependencies import get_user_service
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
        :param user:
        :param user_service:
        :param current_user:
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
        :param user_service:
        :param current_user:
        :return: list[UserResponse]
    """
    users = user_service.get_users()
    return users