from django.http import HttpRequest

from .models import SiteSettings


def site_settings(request: HttpRequest) -> dict:
    return {"site_settings": SiteSettings.get_solo()}
