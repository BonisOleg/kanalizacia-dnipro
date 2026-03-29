from django.contrib import admin
from django.utils.html import format_html
from solo.admin import SingletonModelAdmin
from .models import (
    SiteSettings, HeroSection, AboutSection,
    WhyUsItem, HowWeWorkStep, FAQ, Review,
)


@admin.register(SiteSettings)
class SiteSettingsAdmin(SingletonModelAdmin):
    fieldsets = (
        ("Основне", {
            "fields": ("company_name", "logo", "logo_alt_uk", "logo_alt_ru"),
        }),
        ("Контакти", {
            "fields": (
                "phone_1", "phone_1_viber", "phone_1_telegram",
                "phone_2", "phone_2_viber",
                "email",
            ),
        }),
        ("Адреса та години роботи", {
            "fields": ("address_uk", "address_ru", "working_hours_uk", "working_hours_ru"),
        }),
        ("Статистика", {
            "fields": ("years_experience", "clients_count", "satisfaction_rate"),
        }),
        ("Футер", {
            "fields": ("footer_text_uk", "footer_text_ru"),
        }),
    )


@admin.register(HeroSection)
class HeroSectionAdmin(SingletonModelAdmin):
    fieldsets = (
        ("Тексти (укр)", {
            "fields": ("heading_uk", "subheading_uk", "cta_primary_uk", "cta_secondary_uk"),
        }),
        ("Тексти (рос)", {
            "fields": ("heading_ru", "subheading_ru", "cta_primary_ru", "cta_secondary_ru"),
            "classes": ("collapse",),
        }),
        ("Зображення", {
            "fields": ("background_image",),
        }),
    )


@admin.register(AboutSection)
class AboutSectionAdmin(SingletonModelAdmin):
    fieldsets = (
        ("Тексти (укр)", {
            "fields": ("heading_uk", "text_uk", "image_alt_uk"),
        }),
        ("Тексти (рос)", {
            "fields": ("heading_ru", "text_ru", "image_alt_ru"),
            "classes": ("collapse",),
        }),
        ("Зображення", {
            "fields": ("image",),
        }),
    )


@admin.register(WhyUsItem)
class WhyUsItemAdmin(admin.ModelAdmin):
    list_display = ("title_uk", "order", "is_active")
    list_editable = ("order", "is_active")
    list_display_links = ("title_uk",)
    fieldsets = (
        ("Зображення", {
            "fields": ("icon_svg",),
        }),
        ("Тексти (укр)", {
            "fields": ("title_uk", "description_uk"),
        }),
        ("Тексти (рос)", {
            "fields": ("title_ru", "description_ru"),
            "classes": ("collapse",),
        }),
        ("Налаштування", {
            "fields": ("order", "is_active"),
        }),
    )


@admin.register(HowWeWorkStep)
class HowWeWorkStepAdmin(admin.ModelAdmin):
    list_display = ("number", "title_uk", "order", "is_active")
    list_editable = ("order", "is_active")
    list_display_links = ("title_uk",)
    fieldsets = (
        ("Тексти (укр)", {
            "fields": ("number", "title_uk", "description_uk"),
        }),
        ("Тексти (рос)", {
            "fields": ("title_ru", "description_ru"),
            "classes": ("collapse",),
        }),
        ("Налаштування", {
            "fields": ("order", "is_active"),
        }),
    )


@admin.register(FAQ)
class FAQAdmin(admin.ModelAdmin):
    list_display = ("question_uk", "order", "is_active")
    list_editable = ("order", "is_active")
    list_display_links = ("question_uk",)
    search_fields = ("question_uk", "question_ru")
    fieldsets = (
        ("Питання та відповідь (укр)", {
            "fields": ("question_uk", "answer_uk"),
        }),
        ("Питання та відповідь (рос)", {
            "fields": ("question_ru", "answer_ru"),
            "classes": ("collapse",),
        }),
        ("Налаштування", {
            "fields": ("order", "is_active"),
        }),
    )


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ("author_name", "rating_stars", "service_uk", "created_at", "is_active")
    list_editable = ("is_active",)
    list_display_links = ("author_name",)
    list_filter = ("rating", "is_active")
    search_fields = ("author_name", "text_uk")
    fieldsets = (
        ("Клієнт", {
            "fields": ("author_name", "photo", "rating", "created_at"),
        }),
        ("Відгук (укр)", {
            "fields": ("text_uk", "service_uk"),
        }),
        ("Відгук (рос)", {
            "fields": ("text_ru", "service_ru"),
            "classes": ("collapse",),
        }),
        ("Налаштування", {
            "fields": ("order", "is_active"),
        }),
    )

    @admin.display(description="Оцінка")
    def rating_stars(self, obj: Review) -> str:
        return format_html("⭐" * obj.rating)
