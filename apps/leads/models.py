from django.db import models
from django.utils.translation import gettext_lazy as _


class LeadRequest(models.Model):
    """Lead captured via the step-by-step quiz form."""

    class Location(models.TextChoices):
        BATHROOM = "bathroom", _("Ванна або душ")
        KITCHEN = "kitchen", _("Кухня")
        WHOLE_HOUSE = "whole_house", _("Весь будинок / квартира")
        OUTDOOR = "outdoor", _("На вулиці / зовнішня труба")

    class Duration(models.TextChoices):
        TODAY = "today", _("Сьогодні")
        FEW_DAYS = "few_days", _("Кілька днів тому")
        LONG = "long", _("Кілька тижнів або більше")

    class SmellLevel(models.TextChoices):
        STRONG = "strong", _("Так, дуже сильний")
        SOMETIMES = "sometimes", _("Іноді")
        WHEN_USING = "when_using", _("Тільки під час використання")
        NO = "no", _("Немає")

    class Messenger(models.TextChoices):
        TELEGRAM = "telegram", "Telegram"
        VIBER = "viber", "Viber"
        WHATSAPP = "whatsapp", "WhatsApp"
        CALL = "call", _("Дзвінок")

    location = models.CharField(_("Місце засмічення"), max_length=20, choices=Location.choices, blank=True)
    duration = models.CharField(_("Як давно"), max_length=20, choices=Duration.choices, blank=True)
    smell = models.CharField(_("Запах"), max_length=20, choices=SmellLevel.choices, blank=True)
    messenger = models.CharField(_("Месенджер"), max_length=20, choices=Messenger.choices, blank=True)
    phone = models.CharField(_("Телефон"), max_length=30)
    honeypot = models.CharField(_("Не заповнювати"), max_length=100, blank=True)
    created_at = models.DateTimeField(_("Дата заявки"), auto_now_add=True)
    is_processed = models.BooleanField(_("Опрацьовано"), default=False)
    ip_address = models.GenericIPAddressField(_("IP-адреса"), blank=True, null=True)

    class Meta:
        verbose_name = _("Заявка (квіз)")
        verbose_name_plural = _("Заявки (квіз)")
        ordering = ["-created_at"]

    def __str__(self) -> str:
        return f"Заявка від {self.phone} — {self.created_at:%d.%m.%Y %H:%M}"


class ContactMessage(models.Model):
    """Simple contact form submission."""

    name = models.CharField(_("Ім'я"), max_length=100)
    phone = models.CharField(_("Телефон"), max_length=30)
    message = models.TextField(_("Повідомлення"), blank=True)
    honeypot = models.CharField(_("Не заповнювати"), max_length=100, blank=True)
    created_at = models.DateTimeField(_("Дата"), auto_now_add=True)
    is_read = models.BooleanField(_("Прочитано"), default=False)
    ip_address = models.GenericIPAddressField(_("IP-адреса"), blank=True, null=True)

    class Meta:
        verbose_name = _("Повідомлення (контакт)")
        verbose_name_plural = _("Повідомлення (контакт)")
        ordering = ["-created_at"]

    def __str__(self) -> str:
        return f"{self.name} — {self.phone} ({self.created_at:%d.%m.%Y})"
