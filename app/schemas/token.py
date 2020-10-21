from typing import Optional

from pydantic.main import BaseModel

from app.schemas.core import CoreModel


class Token(CoreModel):
    access_token: str
    token_type: str


class TokenPayload(CoreModel):
    sub: Optional[int] = None
