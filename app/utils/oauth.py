"""
Oauth module
"""

class OAuth:
    def __init__(self, token):
        self.token = token

    def get_current_user(self, token: str) -> dict:
        """
        Get current user
        :param token: str
        :return: dict
        """
        credentials_exception = Exception("Could not validate credentials")
        return self.token.verify_token(token, credentials_exception)
