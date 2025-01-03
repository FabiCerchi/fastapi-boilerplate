"""
This module contains the Pydantic models for the User model.
"""
from typing import Optional
from pydantic import BaseModel, EmailStr, ConfigDict, Field, validator, field_validator


class UserCreate(BaseModel):
    username: str = Field(..., min_length=4, max_length=24)
    email: EmailStr
    password: str = Field(..., min_length=8, max_length=64)
    address: Optional[str] = None


class UserResponse(BaseModel):
    id: int
    username: str
    email: EmailStr
    address: Optional[str] = None

    model_config = ConfigDict(from_attributes=True)


class UserUpdate(BaseModel):
    username: Optional[str] = Field(None, min_length=3, max_length=24)
    password: Optional[str] = Field(None, min_length=8, max_length=64)
    email: Optional[EmailStr] = Field(None, max_length=50)
    address: Optional[str] = Field(None, max_length=255)

