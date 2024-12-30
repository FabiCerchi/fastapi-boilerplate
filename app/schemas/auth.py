"""
This file contains the schema for the login endpoint.
"""
from pydantic import BaseModel

class Login(BaseModel):
    username: str
    password: str
