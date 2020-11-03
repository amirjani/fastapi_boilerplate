import requests
from sqlalchemy.orm import Session

from app import crud, schemas
from app.core.config import settings
from app.db import base  # noqa: F401
from app.helpers import curl
from app.models import Country


def init_db(db: Session) -> None:
    rest_country_url = 'https://restcountries.eu/rest/v2/all'
    countries = requests.get(rest_country_url, headers={"content-type": "application/json"}).json()

    for country in countries:
        country_code = get_country_code(country)
        country_exists = get_existed_country(db, country_code)
        if not country_exists:
            seed_country(db, country, country_code)

        for language in country.get('languages'):
            code = get_language_code(language)
            language_exists = crud.language.get_by_code(db, code=code)
            if not language_exists:
                seed_language(db, language, code)

        for language in country.get('languages'):
            code = get_language_code(language)
            country_code = get_country_code(country)
            country_exists = get_existed_country(db, country_code)

            if country_exists:
                country_language_seed(db, code, country_exists)


def get_existed_country(db: Session, code: int):
    return crud.country.get_by_code(db, code=code)


def get_language_code(language: dict):
    return language.get('iso639_1') if language.get('iso639_1') else language.get('iso639_2')


def get_country_code(country: dict):
    return country.get('alpha2Code') if country.get('alpha2Code') else country.get('alpha3Code')


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


def country_language_seed(db: Session, code: str, country_exists: Country):
    language_to_attach = crud.language.get_by_code(db, code=code).id
    country_language_exists = crud.country_language.get_one(db, country_id=country_exists.id, language_id=language_to_attach)
    if not country_language_exists:
        country_language_in = schemas.CountryLanguageCreate(
            country_id=country_exists.id,
            language_id=language_to_attach
        )
        crud.country_language.create(db, obj_in=country_language_in)
