from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from cloudinary.models import CloudinaryField


class Service(models.Model):
    """A service offered by the company."""

    slug = models.SlugField(_("Slug"), unique=True, max_length=100)
    name_uk = models.CharField(_("Назва (укр)"), max_length=200)
    name_ru = models.CharField(_("Назва (рос)"), max_length=200)
    short_desc_uk = models.TextField(_("Короткий опис (укр)"), max_length=300)
    short_desc_ru = models.TextField(_("Короткий опис (рос)"), max_length=300)
    full_desc_uk = models.TextField(_("Повний опис (укр)"))
    full_desc_ru = models.TextField(_("Повний опис (рос)"))
    icon_svg = models.TextField(_("SVG-іконка"), blank=True, help_text=_("Вставте SVG-код іконки"))
    image = CloudinaryField(_("Зображення"), folder="services/", blank=True, null=True)
    image_alt_uk = models.CharField(_("Alt зображення (укр)"), max_length=200, blank=True)
    image_alt_ru = models.CharField(_("Alt зображення (рос)"), max_length=200, blank=True)
    price_from = models.PositiveIntegerField(_("Ціна від (грн)"), blank=True, null=True)
    price_to = models.PositiveIntegerField(_("Ціна до (грн)"), blank=True, null=True)
    price_note_uk = models.CharField(_("Примітка до ціни (укр)"), max_length=200, blank=True)
    price_note_ru = models.CharField(_("Примітка до ціни (рос)"), max_length=200, blank=True)
    order = models.PositiveIntegerField(_("Порядок"), default=0)
    is_active = models.BooleanField(_("Активна"), default=True)
    is_featured = models.BooleanField(_("Виділена на головній"), default=False)

    class Meta:
        verbose_name = _("Послуга")
        verbose_name_plural = _("Послуги")
        ordering = ["order"]

    def __str__(self) -> str:
        return self.name_uk

    def get_absolute_url(self) -> str:
        return reverse("service_detail", kwargs={"slug": self.slug})

    def price_range_display(self) -> str:
        if self.price_from and self.price_to:
            return f"{self.price_from}–{self.price_to} грн"
        if self.price_from:
            return f"від {self.price_from} грн"
        return "Уточнювати"
