from sqlalchemy.orm import Session

from app.crud.base import CRUDBase
from app.schemas.country import CountryCreate, CountryUpdate
from app.models.country import Country


class CRUDCountry(CRUDBase[Country, CountryCreate, CountryUpdate]):


    def get_by_code(self, db: Session, *, code: str):
        return db.query(Country).filter(Country.code == code).first()


country = CRUDCountry(Country)
