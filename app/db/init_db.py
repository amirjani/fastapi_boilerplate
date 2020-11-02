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
        code = country.get('alpha2Code') if country.get('alpha2Code') else country.get('alpha3Code');
        country_exists = crud.country.get_by_code(db, code=code)
        if not country_exists:
            seed_country(db, country, code)

        for language in country.get('languages'):
            code = language.get('iso639_1') if language.get('iso639_1') else language.get('iso639_2')
            language_exists = crud.language.get_by_code(db, code=code)
            if not language_exists:
                seed_language(db, language, code)


def seed_country(db: Session, country: dict, code: str):
    country_in = schemas.CountryCreate(
        name=country.get('name'),
        code=code,
        calling_code=country.get('callingCodes')[0],
        region=country.get('region'),
        translation=country.get('translations'),
        flag=country.get('flag')
    )
    crud.country.create(db, obj_in=country_in)


def seed_language(db: Session, language: dict, code: str):
    language_in = schemas.LanguageCreate(
        code=code,
        name=language.get('name'),
        native_name=language.get('nativeName')
    )
    crud.language.create(db, obj_in=language_in)
