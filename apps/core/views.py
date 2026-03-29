from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from .models import HeroSection, WhyUsItem, HowWeWorkStep, FAQ, Review, AboutSection
from apps.services.models import Service


def home(request: HttpRequest) -> HttpResponse:
    hero = HeroSection.get_solo()
    why_us = WhyUsItem.objects.filter(is_active=True)
    steps = HowWeWorkStep.objects.filter(is_active=True)
    faqs = FAQ.objects.filter(is_active=True)
    reviews = Review.objects.filter(is_active=True)
    services = Service.objects.filter(is_active=True).order_by("order")[:6]

    return render(request, "core/home.html", {
        "hero": hero,
        "why_us": why_us,
        "steps": steps,
        "faqs": faqs,
        "reviews": reviews,
        "services": services,
        "page_key": "home",
    })


def about(request: HttpRequest) -> HttpResponse:
    about_section = AboutSection.get_solo()
    return render(request, "core/about.html", {
        "about": about_section,
        "page_key": "about",
    })


def prices(request: HttpRequest) -> HttpResponse:
    services = Service.objects.filter(is_active=True).order_by("order")
    return render(request, "core/prices.html", {
        "services": services,
        "page_key": "prices",
    })
