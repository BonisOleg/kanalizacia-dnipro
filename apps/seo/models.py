from django.db import models
from django.utils.translation import gettext_lazy as _
from cloudinary.models import CloudinaryField


class SEOPage(models.Model):
    """SEO metadata for each page, editable in admin."""

    PAGE_KEYS = [
        ("home", "Головна"),
        ("about", "Про нас"),
        ("services", "Послуги"),
        ("prices", "Ціни"),
        ("contact", "Контакти"),
    ]

    page_key = models.SlugField(_("Ключ сторінки"), unique=True, choices=PAGE_KEYS)
    meta_title_uk = models.CharField(_("Meta title (укр)"), max_length=70)
    meta_title_ru = models.CharField(_("Meta title (рос)"), max_length=70)
    meta_desc_uk = models.CharField(_("Meta description (укр)"), max_length=160)
    meta_desc_ru = models.CharField(_("Meta description (рос)"), max_length=160)
    og_image = CloudinaryField(_("OG-зображення"), folder="seo/og/", blank=True, null=True)
    schema_json = models.TextField(
        _("JSON-LD схема"),
        blank=True,
        help_text=_("Додаткова структурована розмітка (JSON-LD) для цієї сторінки"),
    )

    class Meta:
        verbose_name = _("SEO сторінки")
        verbose_name_plural = _("SEO сторінок")

    def __str__(self) -> str:
        label = dict(self.PAGE_KEYS).get(self.page_key, self.page_key)
        return f"SEO: {label}"
