from typing import TYPE_CHECKING

from sqlalchemy import Boolean, Column, Integer, String, Date, Enum
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

    first_name = Column(String, index=True, nullable=False)
    last_name = Column(String, index=True, nullable=False)
    user_type = Column(Enum, index=True, nullable=False)
    gender = Column(Enum, index=True, nullable=False)
    country_id = Column(Integer, index=True, nullable=False)
    language_id = Column(Integer, index=True, nullable=False)
    birth_date = Column(Date, index=True, nullable=False)
    phone = Column(String, index=True, nullable=False)
    password = Column(String, index=True, nullable=False)
    email = Column(String, index=True, nullable=False)

    created_at = Column(String, nullable=False)
    deleted_at = Column(String, nullable=True)

    role = relationship("Role", secondary=UserRole.__tablename__, back_populates="user")
