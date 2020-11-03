from sqlalchemy import Column, ForeignKey

from app.db.base import Base


class CountryCurrency(Base):
    __tablename__ = 'country_currency'

    country_id = Column('country_id', ForeignKey('country.id'), primary_key=True)
    currency_id = Column('currency_id', ForeignKey('currency.id'), primary_key=True)
