import requests
from sqlalchemy.orm import Session

from app import crud, schemas
from app.core.config import settings
from app.db import base  # noqa: F401
from app.helpers import curl


def init_db(db: Session) -> None:
    # user = crud.user.get_by_email(db, email=settings.FIRST_SUPERUSER)
    # if not user:
    #     user_in = schemas.UserCreate(
    #         email=settings.FIRST_SUPERUSER,
    #         password=settings.FIRST_SUPERUSER_PASSWORD,
    #         is_superuser=True,
    #     )
    #     user = crud.user.create(db, obj_in=user_in)  # noqa: F841

    rest_country_url = 'https://restcountries.eu/rest/v2/all'
    countries = requests.get(rest_country_url, headers={"content-type": "application/json"}).json()

    for country in countries:
        country_in = schemas.CountryCreate(
            name=country.get('name'),
            code=country.get('alpha2Code') if country.get('alpha2Code') else country.get('alpha3Code'),
            calling_code=country.get('callingCodes')[0],
            region=country.get('region'),
            translation=country.get('translations'),
            flag=country.get('flag')
        )
        crud.country.create(db, obj_in=country_in)

