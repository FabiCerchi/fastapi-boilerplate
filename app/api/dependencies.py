from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer

from app.utils.oauth import OAuth
from app.utils.token import Token

# Instancia global para extraer tokens
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/login")

# Instancia de OAuth
oauth_service = OAuth(Token())

def get_current_user(token: str = Depends(oauth2_scheme)):
    """
    Función que inyecta la dependencia para los endpoints.
    """
    try:
        return oauth_service.get_current_user(token)
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail=str(e),
            headers={"WWW-Authenticate": "Bearer"},
        )