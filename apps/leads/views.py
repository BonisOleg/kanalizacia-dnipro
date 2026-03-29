from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from django.views.decorators.http import require_POST
from django.core.mail import mail_admins
from django.conf import settings
from .forms import (
    QuizStep1Form, QuizStep2Form, QuizStep3Form, QuizStep4Form,
    ContactForm,
)


def contact(request: HttpRequest) -> HttpResponse:
    form = ContactForm()
    return render(request, "leads/contact.html", {
        "form": form,
        "page_key": "contact",
    })


@require_POST
def contact_submit(request: HttpRequest) -> HttpResponse:
    form = ContactForm(request.POST)
    if form.is_valid():
        _notify_admin_contact(form.cleaned_data)
        return render(request, "leads/partials/contact_success.html")
    return render(request, "leads/partials/contact_form.html", {"form": form}, status=422)


def quiz_start(request: HttpRequest) -> HttpResponse:
    form = QuizStep1Form()
    return render(request, "leads/partials/quiz_step_1.html", {"form": form, "step": 1})


@require_POST
def quiz_step(request: HttpRequest, step: int) -> HttpResponse:
    session_key = "quiz_data"
    quiz_data: dict = request.session.get(session_key, {})

    if step == 1:
        form = QuizStep1Form(request.POST)
        if form.is_valid():
            if form.cleaned_data.get("honeypot"):
                return HttpResponse(status=204)
            quiz_data["location"] = form.cleaned_data["location"]
            request.session[session_key] = quiz_data
            return render(request, "leads/partials/quiz_step_2.html", {"form": QuizStep2Form(), "step": 2})
        return render(request, "leads/partials/quiz_step_1.html", {"form": form, "step": 1}, status=422)

    if step == 2:
        form = QuizStep2Form(request.POST)
        if form.is_valid():
            quiz_data["duration"] = form.cleaned_data["duration"]
            request.session[session_key] = quiz_data
            return render(request, "leads/partials/quiz_step_3.html", {"form": QuizStep3Form(), "step": 3})
        return render(request, "leads/partials/quiz_step_2.html", {"form": form, "step": 2}, status=422)

    if step == 3:
        form = QuizStep3Form(request.POST)
        if form.is_valid():
            quiz_data["smell"] = form.cleaned_data["smell"]
            request.session[session_key] = quiz_data
            return render(request, "leads/partials/quiz_step_4.html", {"form": QuizStep4Form(), "step": 4})
        return render(request, "leads/partials/quiz_step_3.html", {"form": form, "step": 3}, status=422)

    if step == 4:
        form = QuizStep4Form(request.POST)
        if form.is_valid():
            quiz_data["messenger"] = form.cleaned_data["messenger"]
            quiz_data["phone"] = form.cleaned_data["phone"]
            _notify_admin_lead(quiz_data)
            request.session.pop(session_key, None)
            return render(request, "leads/partials/quiz_success.html")
        return render(request, "leads/partials/quiz_step_4.html", {"form": form, "step": 4}, status=422)

    return HttpResponse(status=400)


def _notify_admin_lead(data: dict) -> None:
    if not getattr(settings, "ADMIN_EMAIL", ""):
        return
    try:
        mail_admins(
            subject="Нова заявка з квізу",
            message=(
                f"Телефон: {data.get('phone')}\n"
                f"Месенджер: {data.get('messenger')}\n"
                f"Місце: {data.get('location')}\n"
                f"Давність: {data.get('duration')}\n"
                f"Запах: {data.get('smell')}"
            ),
        )
    except Exception:
        pass


def _notify_admin_contact(data: dict) -> None:
    if not getattr(settings, "ADMIN_EMAIL", ""):
        return
    try:
        mail_admins(
            subject="Нове повідомлення з форми контактів",
            message=(
                f"Ім'я: {data.get('name')}\n"
                f"Телефон: {data.get('phone')}\n"
                f"Повідомлення: {data.get('message', '')}"
            ),
        )
    except Exception:
        pass
