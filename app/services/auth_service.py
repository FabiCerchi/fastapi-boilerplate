"""
    This module is responsible for handling the business logic of the authentication service.
"""
from app.repositories.auth_repository import AuthRepository
from app.schemas.auth import Login


class AuthService:
    """
    AuthService class to handle authentication service
    """

    def __init__(self, repo: AuthRepository):
        """
        Constructor for AuthService class
        :param repo:
        """
        self.repo = repo

    def auth_user(self, login: Login) -> dict[str, str]:
        """
        Function to authenticate user
        :param login: Login
        :return: dict[str, str]:
        """
        return self.repo.auth_user(login)
