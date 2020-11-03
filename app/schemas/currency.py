from datetime import datetime
from typing import Optional

from app.schemas.core import CoreModel


class CurrencyBase(CoreModel):
    code: Optional[str] = None
    name: Optional[str] = None
    symbol: Optional[str] = None
    created_at: Optional[datetime]
    deleted_at: Optional[datetime]


class CurrencyCreate(CurrencyBase):
    code: Optional[str]
    name: str
    symbol: Optional[str]
    created_at = datetime.now()


class CurrencyUpdate(CurrencyBase):
    pass


class CurrencyInDBBase(CurrencyBase):
    id: Optional[int] = None

    class Config:
        orm_mode = True


class Currency(CurrencyInDBBase):
    pass
