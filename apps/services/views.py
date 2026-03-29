from django.shortcuts import render, get_object_or_404
from django.http import HttpRequest, HttpResponse
from .models import Service


def service_list(request: HttpRequest) -> HttpResponse:
    services = Service.objects.filter(is_active=True).order_by("order")
    return render(request, "services/service_list.html", {
        "services": services,
        "page_key": "services",
    })


def service_detail(request: HttpRequest, slug: str) -> HttpResponse:
    service = get_object_or_404(Service, slug=slug, is_active=True)
    related = Service.objects.filter(is_active=True).exclude(pk=service.pk).order_by("order")[:3]
    return render(request, "services/service_detail.html", {
        "service": service,
        "related": related,
        "page_key": f"service_{slug}",
    })
