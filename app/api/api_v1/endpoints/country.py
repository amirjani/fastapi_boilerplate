from datetime import datetime
from typing import Any

import requests
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app import crud, schemas
from app.api import deps
from app.middleware.acl import access_control_layer

router = APIRouter()


@router.get("/country")
def read_all(
    db: Session = Depends(deps.get_db),
    skip: int = 0,
    limit: int = 10
) -> Any:
    rest_country_url = 'https://restcountries.eu/rest/v2/all'
    countries = requests.get(rest_country_url, headers={"content-type": "application/json"}).json()
    return countries
    # for country in countries:
        # ret
        # for language in country.get('languages'):
        #     return language
    return crud.country.get_multi(db, skip=skip, limit=limit)


@router.post("country", dependencies=[Depends(access_control_layer)])
def create(
        *,
        db: Session = Depends(deps.get_db),
        item_in: schemas.CountryCreate,

) -> Any:
    # item_in['created_at'] = datetime.now()

    # item_in.created_at = datetime.now()
    # return item_in
    country = crud.country.create(db=db, obj_in=item_in)
    return country
