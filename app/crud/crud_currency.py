from sqlalchemy.orm import Session

from app.crud.base import CRUDBase
from app.models import Currency
from app.schemas import CurrencyCreate, CurrencyUpdate


class CRUDCurrency(CRUDBase[Currency, CurrencyCreate, CurrencyUpdate]):

    def get_by_code(self, db: Session, *, code: str):
        return db.query(Currency).filter(Currency.code == code).first()


currency = CRUDCurrency(Currency)
