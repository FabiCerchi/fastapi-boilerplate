"""
This module contains the settings for the application
"""
import os
from pathlib import Path
from dotenv import load_dotenv

env_path = Path('.') / '.env.test'
print(f'Loading environment variables from: {env_path}')
load_dotenv(dotenv_path=env_path)

class Settings:
    """
    Settings for the application
    """
    DB = os.getenv('DB')
    DB_USER: str = os.getenv('DB_USER')
    DB_PASSWORD: str = os.getenv('DB_PASSWORD')
    DB_NAME: str = os.getenv('DB_NAME')
    DB_HOST: str = os.getenv('DB_HOST')
    DB_PORT: int = os.getenv('DB_PORT')
    SQLALCHEMY_DATABASE_URI: str = (
        f'{DB}://{DB_USER}:{DB_PASSWORD}@'
        f'{DB_HOST}:{DB_PORT}/{DB_NAME}'
    )
    SQLALCHEMY_TRACK_MODIFICATIONS: bool = False
    SECRET_KEY: str = os.getenv('SECRET_KEY')
    ALGORITHM: str = os.getenv('ALGORITHM')
    def __str__(self):
        return (
            f'DB: {self.DB}\n'
            f'DB_USER: {self.DB_USER}\n'
            f'DB_PASSWORD: {self.DB_PASSWORD}\n'
            f'DB_NAME: {self.DB_NAME}\n'
            f'DB_HOST: {self.DB_HOST}\n'
            f'DB_PORT: {self.DB_PORT}\n'
            f'SQLALCHEMY_DATABASE_URI: {self.SQLALCHEMY_DATABASE_URI}\n'
            f'SQLALCHEMY_TRACK_MODIFICATIONS: {self.SQLALCHEMY_TRACK_MODIFICATIONS}\n'
        )

settings = Settings()