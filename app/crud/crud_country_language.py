from sqlalchemy.orm import Session

from app.crud.base import CRUDBase
from app.models.country_language import CountryLanguage
from app.schemas import CountryLanguageCreate, CountryLanguageUpdate


class CRUDCountryLanguage(CRUDBase[CountryLanguage, CountryLanguageCreate, CountryLanguageUpdate]):
    def get_one(self, db: Session, *, country_id: int, language_id: int):
        return db.query(CountryLanguage).\
            filter(CountryLanguage.country_id == country_id).\
            filter(CountryLanguage.language_id == language_id).\
            first()


country_language = CRUDCountryLanguage(CountryLanguage)
