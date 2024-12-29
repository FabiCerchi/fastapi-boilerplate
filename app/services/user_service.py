from app.models.schemas.user import UserCreate, UserResponse
from app.repositories.user_respository import IUserRepository

class UserService:
    """
        Service class for user related operations
    """
    def __init__(self, user_repository: IUserRepository):
        """
        Constructor for UserService class
        :param user_repository:
        """
        self.user_repository = user_repository

    def create_user(self, user: UserCreate) -> UserResponse:
        """
        Method to create a new user
        :param user:
        :return: bool
        """
        new_user = self.user_repository.add(user)
        return new_user
