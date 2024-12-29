import os
from pathlib import Path
from dotenv import load_dotenv


env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)

class Settings:
    """
    Settings for the application
    """
    POSTGRES_USER: str = os.getenv('POSTGRES_USER')
    POSTGRES_PASSWORD: str = os.getenv('POSTGRES_PASSWORD')
    POSTGRES_DB: str = os.getenv('POSTGRES_DB')
    POSTGRES_HOST: str = os.getenv('POSTGRES_HOST')
    POSTGRES_PORT: int = os.getenv('POSTGRES_PORT')
    SQLALCHEMY_DATABASE_URI: str = (
        f'postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@'
        f'{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_DB}'
    )
    SQLALCHEMY_TRACK_MODIFICATIONS: bool = False

    def __str__(self):
        return (
            f'POSTGRES_USER: {self.POSTGRES_USER}\n'
            f'POSTGRES_PASSWORD: {self.POSTGRES_PASSWORD}\n'
            f'POSTGRES_DB: {self.POSTGRES_DB}\n'
            f'POSTGRES_HOST: {self.POSTGRES_HOST}\n'
            f'POSTGRES_PORT: {self.POSTGRES_PORT}\n'
            f'SQLALCHEMY_DATABASE_URI: {self.SQLALCHEMY_DATABASE_URI}\n'
            f'SQLALCHEMY_TRACK_MODIFICATIONS: {self.SQLALCHEMY_TRACK_MODIFICATIONS}\n'
        )

settings = Settings()
print(settings)
