"""
 Manage exceptions Globally in the application
"""
from __future__ import annotations


class ItemNotFoundError(Exception):
    """Exception raised when an item is not found in the database."""
    def __init__(self, item_type: str, identifier: str | int):
        self.item_type = item_type
        self.identifier = identifier
        super().__init__(f"{item_type} with identifier {identifier} not found")

class UserAlreadyExistsError(Exception):
    """Exception raised when an item is not found in the database."""
    def __init__(self, field: str, value: str | int):
        self.field = field
        self.value = value
        super().__init__(f"User with {field} '{value}' already exists")

class RepositoryError(Exception):
    """Exception raised when an item is not found in the database."""
    def __init__(self, error: str):
        self.error = error
        super().__init__(f"Repository error: {error}")