from django.db import migrations


def set_phone_2(apps, schema_editor):
    SiteSettings = apps.get_model("core", "SiteSettings")
    SiteSettings.objects.filter(phone_2="").update(phone_2="+38 (098) 395-03-56")


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0001_initial"),
    ]

    operations = [
        migrations.RunPython(set_phone_2, migrations.RunPython.noop),
    ]
