from pydantic import BaseModel, Field
from jwt import encode, decode
from uuid import uuid4, UUID
from datetime import datetime

ALGORITHM = "HS256"


class TokenPayload(BaseModel):
    sub: str
    exp: datetime
    iat: datetime = Field(default_factory=datetime.utcnow)
    nbf: datetime = Field(default_factory=datetime.utcnow)


class BaseToken(BaseModel):
    refresh_token: UUID = Field(default_factory=uuid4, alias="_id")
    create_at: datetime


class Token(BaseToken):
    jwt_token: str = Field(...)


def generate_token(secret: str, payload: TokenPayload) -> Token:
    token = encode(payload=payload.model_dump(), key=secret, algorithm=ALGORITHM)
    return Token(jwt_token=token, create_at=payload.iat)


def decode_token(secret: str, token: Token, verify: bool = True) -> TokenPayload:
    options = {"verify_signature": verify}
    return TokenPayload.model_validate(decode(jwt=token.jwt_token, key=secret, algorithms=ALGORITHM, options=options))
