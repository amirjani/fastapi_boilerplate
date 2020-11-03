from typing import Optional
from datetime import datetime

from app.schemas.core import CoreModel


class CountryBase(CoreModel):
    name: Optional[str] = None
    code: Optional[str] = None
    calling_code: Optional[str] = None
    region: Optional[str] = None
    translation: Optional[dict] = None
    flag: Optional[str] = None
    created_at: Optional[datetime]
    deleted_at: Optional[datetime]


class CountryCreate(CountryBase):
    name: str
    code: str
    calling_code: str
    region: str
    translation: Optional[dict]
    flag: str
    created_at = datetime.now()


class CountryUpdate(CountryBase):
    pass


class CountryInDBBase(CountryBase):
    id: Optional[int] = None

    class Config:
        orm_mode = True


class Country(CountryInDBBase):
    pass
