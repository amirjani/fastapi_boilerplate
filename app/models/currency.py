from sqlalchemy import Column, Integer, String

from app.db.base_class import Base


class Currency(Base):
    __tablename__ = 'currency'

    id = Column(Integer, primary_key=True, index=True)

    code = Column(String, nullable=True)
    name = Column(String, nullable=False)
    symbol = Column(String, nullable=True)

    created_at = Column(String, nullable=False)
    deleted_at = Column(String, nullable=True)
