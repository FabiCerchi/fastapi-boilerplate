# OAuth class proteje las rutas de la aplicación

class OAuth:
    def __init__(self, token):
        self.token = token

    def get_current_user(self, token: str) -> dict:
        """
        Valida el token y devuelve los datos del usuario.
        """
        credentials_exception = Exception("Could not validate credentials")
        return self.token.verify_token(token, credentials_exception)
