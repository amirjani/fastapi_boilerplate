from sqlalchemy.orm import Session

from app.crud.base import CRUDBase
from app.models.country_currency import CountryCurrency
from app.schemas import CountryCurrencyCreate, CountryCurrencyUpdate


class CRUDCountryCurrency(CRUDBase[CountryCurrency, CountryCurrencyCreate, CountryCurrencyUpdate]):
    def get_one(self, db: Session, *, country_id: int, currency_id: int):
        return db.query(CountryCurrency).\
            filter(CountryCurrency.country_id == country_id).\
            filter(CountryCurrency.currency_id == currency_id).\
            first()


country_currency = CRUDCountryCurrency(CountryCurrency)
