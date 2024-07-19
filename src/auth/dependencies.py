from fastapi.security import HTTPBearer
from fastapi.security.http import HTTPAuthorizationCredentials


class TokenVerifier(HTTPBearer):
    pass  # implement init an call to process authentications
