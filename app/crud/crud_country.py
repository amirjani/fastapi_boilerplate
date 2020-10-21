from typing import Optional

from app.crud.base import CRUDBase
from sqlalchemy.orm import Session
from app.schemas.country import CountryCreate, CountryUpdate
from app.models.country import Country
from fastapi import APIRouter, Depends, HTTPException
from app.api import deps
from app import crud, models, schemas


class CRUDCountry(CRUDBase[Country, CountryCreate, CountryUpdate]):
    pass


country = CRUDCountry(Country)
