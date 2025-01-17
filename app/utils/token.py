"""
Token utility
"""
from datetime import datetime, timedelta, timezone
from jose import jwt, JWTError

from app.core.config import settings
from app.schemas.token import TokenData

ACCESS_TOKEN_EXPIRE_MINUTES = 30

class Token:
    """
    Token utility class
    """
    @staticmethod
    def generate_token(data: dict) -> str:
        """
        Generate a new token
        :param data: {dict} data to encode
        :return: str: token
        """
        to_encode = data.copy()
        expire = datetime.now(timezone.utc) + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
        to_encode.update({"exp": expire})
        encoded_jwt = jwt.encode(to_encode, settings.SECRET_KEY, algorithm=settings.ALGORITHM)

        return encoded_jwt

    @staticmethod
    def verify_token(token: str, credentials_exception) -> TokenData:
        """
        Verify token
        :param token: {str} token to verify
        :param credentials_exception: {Exception} exception to raise
        :return: dict: token data
        """
        try:
            payload = jwt.decode(token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM])
            username = payload.get("sub")
            user_id = payload.get("id")
            is_superuser = payload.get("is_superuser")
            active = payload.get("active")
            if username is None:
                raise credentials_exception
            token_data = TokenData(username=username, id=user_id, is_superuser=is_superuser, active=active)
        except JWTError:
            raise credentials_exception
        return token_data
