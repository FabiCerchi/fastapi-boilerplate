"""
This file contains the hashing utility functions.
"""
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


class Hasher:
    """
    Hasher class to handle hashing utility functions
    """

    @staticmethod
    def get_password_hash(password: str) -> str:
        """
        Function to get password hash
        :param password: str
        :return: str hashed password
        """
        return pwd_context.hash(password)

    @staticmethod
    def verify_password(plain_password, hashed_password) -> bool:
        """
        Function to verify password
        :param plain_password: str
        :param hashed_password: str hashed password
        :return: bool
        """
        return pwd_context.verify(plain_password, hashed_password)
