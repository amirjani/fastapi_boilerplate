from datetime import datetime
from typing import Optional

from app.schemas.core import CoreModel


class CountryCurrencyBase(CoreModel):
    country_id: Optional[int] = None
    currency_id: Optional[int] = None


class CountryCurrencyCreate(CountryCurrencyBase):
    country_id: int
    currency_id: int


class CountryCurrencyUpdate(CountryCurrencyBase):
    pass


class CountryCurrencyInDBBase(CountryCurrencyBase):
    class config:
        orm_mode = True


class CountryCurrency(CountryCurrencyInDBBase):
    pass
