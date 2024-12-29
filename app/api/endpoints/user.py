from fastapi import APIRouter, Depends, status

from app.models.schemas.user import UserCreate, UserResponse
from app.services.user_service import UserService
from app.services.dependencies import get_user_service

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
        :return: UserResponse
    """
    new_user = user_service.create_user(user)
    return new_user
