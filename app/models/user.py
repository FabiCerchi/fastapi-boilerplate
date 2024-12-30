from datetime import datetime
from sqlalchemy import Column, Integer, String, DateTime

from app.db.database import Base


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    email = Column(String(50), unique=True, nullable=False, index=True)
    username = Column(String(24), unique=True, nullable=False, index=True)
    password = Column(String(64), nullable=False)
    address = Column(String, nullable=True)
    created_at = Column(DateTime, default=datetime.now())
    updated_at = Column(DateTime, default=datetime.now(), onupdate=datetime.now())
