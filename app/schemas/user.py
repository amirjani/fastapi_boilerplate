from typing import Optional

from pydantic import EmailStr
from datetime import datetime

from app.schemas.core import CoreModel
from app.models.user import UserType, UserGender


class UserBase(CoreModel):
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    user_type: Optional[UserType] = None
    gender: Optional[UserGender] = None
    country_id: Optional[int] = None
    language_id: Optional[int] = None
    birth_date: Optional[datetime] = None
    phone: Optional[str] = None
    password: Optional[str] = None
    email: Optional[EmailStr] = None
    created_at: Optional[datetime]
    deleted_at: Optional[datetime]


class UserCreate(UserBase):
    first_name: str
    last_name: str
    user_type: UserType
    gender: UserGender
    country_id: int
    language_id: int
    birth_date: datetime
    phone: str
    password: str
    email: EmailStr
    created_at = datetime.now()


class UserUpdate(UserBase):
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    user_type: Optional[UserType] = None
    gender: Optional[UserGender] = None
    country_id: Optional[int] = None
    language_id: Optional[int] = None
    birth_date: Optional[datetime] = None
    phone: Optional[str] = None
    password: Optional[str] = None
    email: Optional[EmailStr] = None


class UserInDBBase(UserBase):
    id: Optional[int] = None

    class Config:
        orm_mode = True


class User(UserInDBBase):
    pass


class UserInDB(UserInDBBase):
    password: str
