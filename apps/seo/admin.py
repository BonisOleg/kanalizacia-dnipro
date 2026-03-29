from django.contrib import admin
from .models import SEOPage


@admin.register(SEOPage)
class SEOPageAdmin(admin.ModelAdmin):
    list_display = ("page_key", "meta_title_uk", "meta_title_ru")
    list_display_links = ("page_key", "meta_title_uk")
    fieldsets = (
        ("Сторінка", {
            "fields": ("page_key",),
        }),
        ("Meta (укр)", {
            "fields": ("meta_title_uk", "meta_desc_uk"),
        }),
        ("Meta (рос)", {
            "fields": ("meta_title_ru", "meta_desc_ru"),
            "classes": ("collapse",),
        }),
        ("Open Graph", {
            "fields": ("og_image",),
        }),
        ("Структурована розмітка", {
            "fields": ("schema_json",),
            "classes": ("collapse",),
        }),
    )
