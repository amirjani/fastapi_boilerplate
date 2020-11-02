from datetime import datetime
from typing import Optional

from app.schemas.core import CoreModel


class LanguageBase(CoreModel):
    code: Optional[str] = None
    name: Optional[str] = None
    native_name: Optional[str] = None
    created_at: Optional[datetime]
    deleted_at: Optional[datetime]


class LanguageCreate(LanguageBase):
    code: str
    name: str
    native_name: str
    created_at = datetime.now()


class LanguageUpdate(LanguageBase):
    pass


class LanguageInDBBase(LanguageBase):
    id: Optional[int] = None

    class config:
        orm_mode = True


class Language(LanguageInDBBase):
    pass
