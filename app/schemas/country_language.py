from datetime import datetime
from typing import Optional

from app.schemas.core import CoreModel


class CountryLanguageBase(CoreModel):
    country_id: Optional[int] = None
    language_id: Optional[int] = None


class CountryLanguageCreate(CountryLanguageBase):
    country_id: int
    language_id: int


class CountryLanguageUpdate(CountryLanguageBase):
    pass


class CountryLanguageInDBBase(CountryLanguageBase):
    class config:
        orm_mode = True


class CountryLanguage(CountryLanguageInDBBase):
    pass
