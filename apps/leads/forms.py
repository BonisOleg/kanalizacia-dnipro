from django import forms
from django.utils.translation import gettext_lazy as _
from .models import LeadRequest, ContactMessage


class QuizStep1Form(forms.Form):
    location = forms.ChoiceField(
        choices=LeadRequest.Location.choices,
        label=_("Де знаходиться засмічення?"),
        widget=forms.RadioSelect,
    )
    honeypot = forms.CharField(required=False, widget=forms.HiddenInput)


class QuizStep2Form(forms.Form):
    duration = forms.ChoiceField(
        choices=LeadRequest.Duration.choices,
        label=_("Як давно ви помітили проблему?"),
        widget=forms.RadioSelect,
    )


class QuizStep3Form(forms.Form):
    smell = forms.ChoiceField(
        choices=LeadRequest.SmellLevel.choices,
        label=_("Чи є неприємний запах?"),
        widget=forms.RadioSelect,
    )


class QuizStep4Form(forms.Form):
    messenger = forms.ChoiceField(
        choices=LeadRequest.Messenger.choices,
        label=_("Яким месенджером зручніше?"),
        widget=forms.RadioSelect,
    )
    phone = forms.CharField(
        max_length=30,
        label=_("Ваш номер телефону"),
        widget=forms.TextInput(attrs={"placeholder": "+38 (0__) ___-__-__", "autocomplete": "tel"}),
    )

    def clean_phone(self) -> str:
        phone: str = self.cleaned_data["phone"].strip()
        if len(phone) < 10:
            raise forms.ValidationError(_("Введіть коректний номер телефону."))
        return phone


class ContactForm(forms.Form):
    name = forms.CharField(
        max_length=100,
        label=_("Ваше ім'я"),
        widget=forms.TextInput(attrs={"autocomplete": "name"}),
    )
    phone = forms.CharField(
        max_length=30,
        label=_("Телефон"),
        widget=forms.TextInput(attrs={"placeholder": "+38 (0__) ___-__-__", "autocomplete": "tel"}),
    )
    message = forms.CharField(
        required=False,
        label=_("Повідомлення"),
        widget=forms.Textarea(attrs={"rows": 4}),
    )
    honeypot = forms.CharField(required=False, widget=forms.HiddenInput)

    def clean_honeypot(self) -> str:
        value: str = self.cleaned_data.get("honeypot", "")
        if value:
            raise forms.ValidationError("Spam detected.")
        return value

    def clean_phone(self) -> str:
        phone: str = self.cleaned_data["phone"].strip()
        if len(phone) < 10:
            raise forms.ValidationError(_("Введіть коректний номер телефону."))
        return phone
