from django.http import HttpRequest
from apps.core.hardcoded_data import SEO_PAGES


def seo_meta(request: HttpRequest) -> dict:
    return {"seo_pages": SEO_PAGES}
