"""
Database module to handle database connection and session
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

from app.core.config import settings


class Database:
    """
    Database class to handle database connection and session
    """

    def __init__(self):
        self.engine = create_engine(settings.SQLALCHEMY_DATABASE_URI)
        self.session_local = sessionmaker(autocommit=False, autoflush=False, bind=self.engine)
        self.base = declarative_base()


    def get_db(self):
        """
        Get database session
        :return: db session
        """
        db = self.session_local()
        try:
            yield db
        finally:
            db.close()


db = Database()
Base = db.base
get_db = db.get_db
