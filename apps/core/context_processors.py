from django.http import HttpRequest
from .models import SiteSettings


def site_settings(request: HttpRequest) -> dict:
    """Inject SiteSettings singleton into every template context."""
    return {"site_settings": SiteSettings.get_solo()}
