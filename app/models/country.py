from sqlalchemy import Boolean, Column, Integer, String, JSON
from app.db.base_class import Base


class Country(Base):
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    code = Column(String, index=True)
    calling_code = Column(Integer, unique=True, index=True, nullable=False)
    region = Column(String, nullable=False)
    translation = Column(JSON, nullable=False)
    flag = Column(String, nullable=False)
    created_at = Column(String, nullable=False)
    deleted_at = Column(String, nullable=True)
