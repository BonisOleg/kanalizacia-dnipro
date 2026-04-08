from django.db import migrations


def force_phone_2(apps, schema_editor):
    SiteSettings = apps.get_model("core", "SiteSettings")
    SiteSettings.objects.all().update(phone_2="+38 (098) 395-03-56")


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0002_set_phone_2"),
    ]

    operations = [
        migrations.RunPython(force_phone_2, migrations.RunPython.noop),
    ]
