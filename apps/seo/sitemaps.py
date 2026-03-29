from django.contrib.sitemaps import Sitemap
from django.urls import reverse
from apps.services.models import Service


class StaticViewSitemap(Sitemap):
    priority = 0.8
    changefreq = "weekly"
    i18n = True
    languages = ["uk", "ru"]

    def items(self) -> list[str]:
        return ["home", "service_list", "about", "prices", "contact"]

    def location(self, item: str) -> str:
        return reverse(item)


class ServiceSitemap(Sitemap):
    priority = 0.7
    changefreq = "monthly"
    i18n = True
    languages = ["uk", "ru"]

    def items(self):  # type: ignore
        return Service.objects.filter(is_active=True)

    def location(self, obj: Service) -> str:
        return obj.get_absolute_url()
