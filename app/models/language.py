from sqlalchemy import Column, Integer, String

from app.db.base_class import Base


class Language(Base):
    __tablename__ = "language"

    id = Column(Integer, primary_key=True, index=True)

    code = Column(String, nullable=False)
    name = Column(String, nullable=False)
    native_name = Column(String, nullable=False)

    created_at = Column(String, nullable=False)
    deleted_at = Column(String, nullable=True)
