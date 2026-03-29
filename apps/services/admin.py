from django.contrib import admin
from .models import Service


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ("name_uk", "slug", "price_range_display", "order", "is_active", "is_featured")
    list_editable = ("order", "is_active", "is_featured")
    list_display_links = ("name_uk",)
    list_filter = ("is_active", "is_featured")
    search_fields = ("name_uk", "name_ru", "slug")
    prepopulated_fields: dict = {}
    fieldsets = (
        ("Ідентифікатор", {
            "fields": ("slug",),
        }),
        ("Назва та опис (укр)", {
            "fields": ("name_uk", "short_desc_uk", "full_desc_uk", "image_alt_uk"),
        }),
        ("Назва та опис (рос)", {
            "fields": ("name_ru", "short_desc_ru", "full_desc_ru", "image_alt_ru"),
            "classes": ("collapse",),
        }),
        ("Медіа", {
            "fields": ("icon_svg", "image"),
        }),
        ("Ціна", {
            "fields": ("price_from", "price_to", "price_note_uk", "price_note_ru"),
        }),
        ("Налаштування", {
            "fields": ("order", "is_active", "is_featured"),
        }),
    )
