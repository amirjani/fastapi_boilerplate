from app.crud.base import CRUDBase
from app.models.country_language import CountryLanguage
from app.schemas import CountryLanguageCreate, CountryLanguageUpdate


class CRUDCountryLanguage(CRUDBase[CountryLanguage, CountryLanguageCreate, CountryLanguageUpdate]):
    pass


country_language = CRUDCountryLanguage(CountryLanguage)
