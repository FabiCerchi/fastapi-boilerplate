"""
 Manage exceptions Globally in the application
"""

class ItemIdNotFoundError(BaseException):
    """Exception raised when an item is not found in the database."""
    def __init__(self, item_type: str, item_id: int):
        self.item_type = item_type
        self.item_id = item_id
        super().__init__(f"{item_type} with ID {item_id} not found")

class ItemEmailNotFoundError(BaseException):
    """Exception raised when an item is not found in the database."""
    def __init__(self, item_type: str, item_email: str):
        self.item_type = item_type
        self.item_email = item_email
        super().__init__(f"{item_type} with email {item_email} not found")
