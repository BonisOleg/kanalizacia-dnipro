from django.contrib import admin
from .models import LeadRequest, ContactMessage


@admin.register(LeadRequest)
class LeadRequestAdmin(admin.ModelAdmin):
    list_display = ("phone", "location", "duration", "messenger", "created_at", "is_processed")
    list_editable = ("is_processed",)
    list_display_links = ("phone",)
    list_filter = ("is_processed", "location", "messenger")
    search_fields = ("phone",)
    readonly_fields = ("created_at", "ip_address")
    fieldsets = (
        ("Контакт", {
            "fields": ("phone", "messenger"),
        }),
        ("Деталі засмічення", {
            "fields": ("location", "duration", "smell"),
        }),
        ("Мета", {
            "fields": ("created_at", "ip_address", "is_processed"),
        }),
    )


@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ("name", "phone", "created_at", "is_read")
    list_editable = ("is_read",)
    list_display_links = ("name",)
    list_filter = ("is_read",)
    search_fields = ("name", "phone", "message")
    readonly_fields = ("created_at", "ip_address")
    fieldsets = (
        ("Відправник", {
            "fields": ("name", "phone"),
        }),
        ("Повідомлення", {
            "fields": ("message",),
        }),
        ("Мета", {
            "fields": ("created_at", "ip_address", "is_read"),
        }),
    )
