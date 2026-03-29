from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from .hardcoded_data import HERO, WHY_US, STEPS, FAQS, REVIEWS, ABOUT, get_active_services


def home(request: HttpRequest) -> HttpResponse:
    return render(request, "core/home.html", {
        "hero": HERO,
        "why_us": WHY_US,
        "steps": STEPS,
        "faqs": FAQS,
        "reviews": REVIEWS,
        "services": get_active_services()[:6],
        "page_key": "home",
    })


def about(request: HttpRequest) -> HttpResponse:
    return render(request, "core/about.html", {
        "about": ABOUT,
        "page_key": "about",
    })


def prices(request: HttpRequest) -> HttpResponse:
    return render(request, "core/prices.html", {
        "services": get_active_services(),
        "page_key": "prices",
    })
