from django.urls import path
from django.http import HttpResponse
from django.views.decorators.cache import cache_page


@cache_page(60 * 60 * 24)
def robots_txt(request):  # type: ignore
    lines = [
        "User-agent: *",
        "Allow: /",
        "Disallow: /admin/",
        "Disallow: /i18n/",
        "",
        f"Sitemap: {request.build_absolute_uri('/sitemap.xml')}",
    ]
    return HttpResponse("\n".join(lines), content_type="text/plain")


urlpatterns = [
    path("", robots_txt),
]
