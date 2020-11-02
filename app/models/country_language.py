from sqlalchemy import Column, ForeignKey

from app.db.base import Base


class CountryLanguage(Base):
    __tablename__ = 'country_language'

    country_id = Column('country_id', ForeignKey('country.id'), primary_key=True)
    language_id = Column('language_id', ForeignKey('language.id'), primary_key=True)
