"""
This module contains the Pydantic models for the User model.
"""
from typing import Optional
from pydantic import BaseModel, EmailStr , ConfigDict


class UserCreate(BaseModel):
    username: str
    email: EmailStr
    password: str
    address: Optional[str] = None


class UserResponse(BaseModel):
    id: int
    username: str
    email: EmailStr
    address: Optional[str] = None

    model_config = ConfigDict(from_attributes=True)


class UserUpdate(BaseModel):
    username: Optional[str] = None
    email: Optional[EmailStr] = None
    address: Optional[str] = None
    password: Optional[str] = None
