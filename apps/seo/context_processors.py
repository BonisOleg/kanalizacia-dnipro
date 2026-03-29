from django.http import HttpRequest
from .models import SEOPage


def seo_meta(request: HttpRequest) -> dict:
    """Inject current page SEO metadata based on page_key view variable."""
    return {"seo_pages": {p.page_key: p for p in SEOPage.objects.all()}}
