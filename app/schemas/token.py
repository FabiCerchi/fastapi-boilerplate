from pydantic import BaseModel

# TokenData schema
class TokenData(BaseModel):
    username: str = None
    id: int = None
    is_superuser: bool
    active: bool

class TokenResponse(BaseModel):
    access_token: str
    token_type: str
