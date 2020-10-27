from sqlalchemy import Boolean, Column, Integer, String
from sqlalchemy.orm import relationship

from app.db.base_class import Base
from app.models.user_role import UserRole


class Role(Base):
    __tablename__ = 'role'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    is_primary = Column(Boolean)

    items = relationship("User", secondary=UserRole, back_populates="role")
