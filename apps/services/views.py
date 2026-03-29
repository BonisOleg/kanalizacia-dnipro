from django.shortcuts import render
from django.http import HttpRequest, HttpResponse, Http404
from apps.core.hardcoded_data import get_active_services, get_service_by_slug


def service_list(request: HttpRequest) -> HttpResponse:
    return render(request, "services/service_list.html", {
        "services": get_active_services(),
        "page_key": "services",
    })


def service_detail(request: HttpRequest, slug: str) -> HttpResponse:
    service = get_service_by_slug(slug)
    if service is None or not service.is_active:
        raise Http404
    related = [s for s in get_active_services() if s.slug != slug][:3]
    return render(request, "services/service_detail.html", {
        "service": service,
        "related": related,
        "page_key": f"service_{slug}",
    })
