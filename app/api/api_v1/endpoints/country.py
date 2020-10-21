from datetime import datetime
from typing import Any

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app import crud, schemas
from app.api import deps

router = APIRouter()


@router.get("country")
def read_all(
        db: Session = Depends(deps.get_db),
        skip: int = 0,
        limit: int = 10
) -> Any:
    return crud.country.get_multi(db, skip=skip, limit=limit)


@router.post("country")
def create(
        *,
        db: Session = Depends(deps.get_db),
        item_in: schemas.CountryCreate
) -> Any:
    # item_in['created_at'] = datetime.now()

    # item_in.created_at = datetime.now()
    # return item_in
    country = crud.country.create(db=db, obj_in=item_in)
    return country
