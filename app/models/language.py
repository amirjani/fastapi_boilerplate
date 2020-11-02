from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from app.db.base_class import Base
from app.models.country_language import CountryLanguage


class Language(Base):
    __tablename__ = "language"

    id = Column(Integer, primary_key=True, index=True)

    code = Column(String, nullable=False)
    name = Column(String, nullable=False)
    native_name = Column(String, nullable=False)

    created_at = Column(String, nullable=False)
    deleted_at = Column(String, nullable=True)

    country = relationship("Country", secondary=CountryLanguage.__tablename__, back_populates="language")
