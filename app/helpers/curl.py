import requests


def get_curl(base_url: str, params: dict):
    return requests.get(base_url, params=params, headers={"content-type": "application/json"})
