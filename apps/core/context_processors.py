from django.http import HttpRequest

from .hardcoded_data import SITE_SETTINGS


def site_settings(request: HttpRequest) -> dict:
    return {"site_settings": SITE_SETTINGS}
