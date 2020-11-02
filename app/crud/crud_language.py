from sqlalchemy.orm import Session

from app.crud.base import CRUDBase
from app.schemas.language import LanguageCreate, LanguageUpdate
from app.models.language import Language


class CRUDLanguage(CRUDBase[Language, LanguageCreate, LanguageUpdate]):

    def get_by_code(self, db: Session, *, code: str):
        return db.query(Language).filter(Language.code == code).first()


language = CRUDLanguage(Language)
