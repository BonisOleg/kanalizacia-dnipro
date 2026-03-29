from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls.i18n import i18n_patterns
from django.urls import path, include
from django.views.generic import TemplateView
from django.contrib.sitemaps.views import sitemap
from apps.seo.sitemaps import StaticViewSitemap, ServiceSitemap

admin.site.site_header = settings.ADMIN_SITE_HEADER
admin.site.site_title = settings.ADMIN_SITE_TITLE
admin.site.index_title = settings.ADMIN_INDEX_TITLE

sitemaps = {
    "static": StaticViewSitemap,
    "services": ServiceSitemap,
}

urlpatterns = [
    path("admin/", admin.site.urls),
    path("i18n/", include("django.conf.urls.i18n")),
    path("sitemap.xml", sitemap, {"sitemaps": sitemaps}, name="django.contrib.sitemaps.views.sitemap"),
    path("robots.txt", include("apps.seo.urls_robots")),
    path("healthz/", TemplateView.as_view(template_name="healthz.html", content_type="text/plain"), name="healthz"),
]

urlpatterns += i18n_patterns(
    path("", include("apps.core.urls")),
    path("services/", include("apps.services.urls")),
    path("leads/", include("apps.leads.urls")),
    prefix_default_language=False,
)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
