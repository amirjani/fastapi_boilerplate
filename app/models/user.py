from typing import TYPE_CHECKING

from sqlalchemy import Boolean, Column, Integer, String
from sqlalchemy.orm import relationship, backref

from app.db.base_class import Base
from app.models.user_role import UserRole
import enum


class UserType(enum.Enum):
    natural_entity = 'Natural Entity'
    legal_entity = 'Legal Entity'


class UserGender(enum.Enum):
    Male = 'Male'
    Female = 'Female'
    Other = 'Other'


class User(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True, index=True)
    full_name = Column(String, index=True)
    email = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    is_active = Column(Boolean(), default=True)
    is_superuser = Column(Boolean(), default=False)

    role = relationship("Role", secondary=UserRole.__tablename__, back_populates="user")
