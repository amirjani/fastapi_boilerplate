from sqlalchemy import Boolean, Column, Integer, String, JSON
from sqlalchemy.orm import relationship

from app.db.base_class import Base
from app.models.country_language import CountryLanguage


class Country(Base):
    __tablename__ = "country"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    code = Column(String, index=True)
    calling_code = Column(String, unique=True, index=True, nullable=False)
    region = Column(String, nullable=False)
    translation = Column(JSON, nullable=False)
    flag = Column(String, nullable=False)
    created_at = Column(String, nullable=False)
    deleted_at = Column(String, nullable=True)

    language = relationship("Language", secondary=CountryLanguage.__tablename__, back_populates="country")
