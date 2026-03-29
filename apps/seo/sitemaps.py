from django.contrib.sitemaps import Sitemap
from django.urls import reverse
from apps.core.hardcoded_data import get_active_services, ServiceObj


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

    def items(self) -> list[ServiceObj]:
        return get_active_services()

    def location(self, obj: ServiceObj) -> str:
        return obj.get_absolute_url()
