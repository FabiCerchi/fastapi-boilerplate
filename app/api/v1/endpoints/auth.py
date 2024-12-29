from fastapi import APIRouter, Depends, status
from fastapi.security import OAuth2PasswordRequestForm

from app.services.auth_service import AuthService
from app.services.dependencies import get_auth_service
from app.schemas.token import TokenResponse

auth_router = APIRouter(prefix='/auth', tags=['Auth'])

@auth_router.post('/login',
                  status_code=status.HTTP_200_OK,
                  response_model=TokenResponse)
async def get_login(login: OAuth2PasswordRequestForm = Depends(), auth_service: AuthService = Depends(get_auth_service)):
    """
    Get a token
    :param login:
    :param auth_service:
    :return: dict: token
    """

    jwt = auth_service.auth_user(login)
    return jwt