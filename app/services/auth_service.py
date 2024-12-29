from app.repositories.auth_repository import AuthRepository
from app.schemas.auth import Login


class AuthService:

    def __init__(self, repo: AuthRepository):
        self.repo = repo

    def auth_user(self, login: Login) -> dict[str, str]:
        """
        Function to authenticate user
        :param login:
        :param dict[str, str]:
        """
        return self.repo.auth_user(login)
