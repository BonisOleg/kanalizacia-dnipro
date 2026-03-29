from django.db import models
from django.utils.translation import gettext_lazy as _
from solo.models import SingletonModel
from cloudinary.models import CloudinaryField


class SiteSettings(SingletonModel):
    """Global site settings managed via admin."""

    company_name = models.CharField(_("Назва компанії"), max_length=200, default="Прочищення Каналізації")
    logo = CloudinaryField(_("Логотип"), folder="site/", blank=True, null=True)
    logo_alt_uk = models.CharField(_("Alt логотипу (укр)"), max_length=200, default="Прочищення каналізації Дніпро")
    logo_alt_ru = models.CharField(_("Alt логотипу (рос)"), max_length=200, default="Прочистка канализации Днепр")

    phone_1 = models.CharField(_("Телефон 1"), max_length=30, default="+38 (000) 000-00-00")
    phone_2 = models.CharField(_("Телефон 2"), max_length=30, blank=True)
    phone_1_viber = models.BooleanField(_("Viber (тел. 1)"), default=True)
    phone_1_telegram = models.BooleanField(_("Telegram (тел. 1)"), default=True)
    phone_2_viber = models.BooleanField(_("Viber (тел. 2)"), default=False)

    email = models.EmailField(_("Email"), blank=True)
    address_uk = models.CharField(_("Адреса (укр)"), max_length=300, default="м. Дніпро та Дніпропетровська область")
    address_ru = models.CharField(_("Адреса (рос)"), max_length=300, default="г. Днепр и Днепропетровская область")
    working_hours_uk = models.CharField(_("Години роботи (укр)"), max_length=100, default="Без вихідних: 06:00–23:00")
    working_hours_ru = models.CharField(_("Часы работы (рос)"), max_length=100, default="Без выходных: 06:00–23:00")

    footer_text_uk = models.TextField(_("Текст футера (укр)"), blank=True)
    footer_text_ru = models.TextField(_("Текст футера (рос)"), blank=True)

    years_experience = models.PositiveIntegerField(_("Років досвіду"), default=5)
    clients_count = models.CharField(_("Клієнтів (текст)"), max_length=20, default="1000+")
    satisfaction_rate = models.CharField(_("Задоволеність (%)"), max_length=10, default="98%")

    class Meta:
        verbose_name = _("Налаштування сайту")

    def __str__(self) -> str:
        return "Налаштування сайту"


class HeroSection(SingletonModel):
    """Main hero section on homepage."""

    heading_uk = models.CharField(_("Заголовок (укр)"), max_length=300, default="Прочищення каналізації у Дніпрі")
    heading_ru = models.CharField(_("Заголовок (рос)"), max_length=300, default="Прочистка канализации в Днепре")
    subheading_uk = models.TextField(
        _("Підзаголовок (укр)"),
        default="Професійне прочищення будь-якої складності. Без вихідних, з гарантією результату.",
    )
    subheading_ru = models.TextField(
        _("Подзаголовок (рос)"),
        default="Профессиональная прочистка любой сложности. Без выходных, с гарантией результата.",
    )
    cta_primary_uk = models.CharField(_("Кнопка CTA (укр)"), max_length=100, default="Розрахувати вартість")
    cta_primary_ru = models.CharField(_("Кнопка CTA (рос)"), max_length=100, default="Рассчитать стоимость")
    cta_secondary_uk = models.CharField(_("Кнопка 2 (укр)"), max_length=100, default="Наші послуги")
    cta_secondary_ru = models.CharField(_("Кнопка 2 (рос)"), max_length=100, default="Наши услуги")
    background_image = CloudinaryField(_("Фонове зображення"), folder="hero/", blank=True, null=True)

    class Meta:
        verbose_name = _("Секція Hero")

    def __str__(self) -> str:
        return "Секція Hero"


class AboutSection(SingletonModel):
    """About us section content."""

    heading_uk = models.CharField(_("Заголовок (укр)"), max_length=300, default="Про нас")
    heading_ru = models.CharField(_("Заголовок (рос)"), max_length=300, default="О нас")
    text_uk = models.TextField(
        _("Текст (укр)"),
        default=(
            "Ми — команда досвідчених фахівців з прочищення каналізації у Дніпрі. "
            "Працюємо з 2019 року, виконали понад 1000 успішних виїздів. "
            "Використовуємо найсучасніше обладнання: електромеханічний апарат ROTHENBERGER R 750, "
            "гідродинамічні машини та ілосос з власним Ecoflo."
        ),
    )
    text_ru = models.TextField(
        _("Текст (рос)"),
        default=(
            "Мы — команда опытных специалистов по прочистке канализации в Днепре. "
            "Работаем с 2019 года, выполнили более 1000 успешных выездов. "
            "Используем современное оборудование: электромеханический аппарат ROTHENBERGER R 750, "
            "гидродинамические машины и илосос с собственным Ecoflo."
        ),
    )
    image = CloudinaryField(_("Фото команди"), folder="about/", blank=True, null=True)
    image_alt_uk = models.CharField(_("Alt фото (укр)"), max_length=200, blank=True)
    image_alt_ru = models.CharField(_("Alt фото (рос)"), max_length=200, blank=True)

    class Meta:
        verbose_name = _("Секція «Про нас»")

    def __str__(self) -> str:
        return "Секція «Про нас»"


class WhyUsItem(models.Model):
    """Single benefit/advantage item."""

    icon_svg = models.TextField(_("SVG-іконка"), blank=True, help_text=_("Вставте SVG-код іконки"))
    title_uk = models.CharField(_("Заголовок (укр)"), max_length=200)
    title_ru = models.CharField(_("Заголовок (рос)"), max_length=200)
    description_uk = models.TextField(_("Опис (укр)"), blank=True)
    description_ru = models.TextField(_("Опис (рос)"), blank=True)
    order = models.PositiveIntegerField(_("Порядок"), default=0)
    is_active = models.BooleanField(_("Активний"), default=True)

    class Meta:
        verbose_name = _("Перевага")
        verbose_name_plural = _("Переваги")
        ordering = ["order"]

    def __str__(self) -> str:
        return self.title_uk


class HowWeWorkStep(models.Model):
    """Step in «How we work» section."""

    number = models.PositiveIntegerField(_("Номер кроку"))
    title_uk = models.CharField(_("Заголовок (укр)"), max_length=200)
    title_ru = models.CharField(_("Заголовок (рос)"), max_length=200)
    description_uk = models.TextField(_("Опис (укр)"))
    description_ru = models.TextField(_("Опис (рос)"))
    order = models.PositiveIntegerField(_("Порядок"), default=0)
    is_active = models.BooleanField(_("Активний"), default=True)

    class Meta:
        verbose_name = _("Крок «Як ми працюємо»")
        verbose_name_plural = _("Кроки «Як ми працюємо»")
        ordering = ["order", "number"]

    def __str__(self) -> str:
        return f"{self.number}. {self.title_uk}"


class FAQ(models.Model):
    """Frequently asked question."""

    question_uk = models.CharField(_("Питання (укр)"), max_length=500)
    question_ru = models.CharField(_("Питання (рос)"), max_length=500)
    answer_uk = models.TextField(_("Відповідь (укр)"))
    answer_ru = models.TextField(_("Відповідь (рос)"))
    order = models.PositiveIntegerField(_("Порядок"), default=0)
    is_active = models.BooleanField(_("Активний"), default=True)

    class Meta:
        verbose_name = _("FAQ")
        verbose_name_plural = _("FAQ")
        ordering = ["order"]

    def __str__(self) -> str:
        return self.question_uk


class Review(models.Model):
    """Customer review."""

    author_name = models.CharField(_("Ім'я клієнта"), max_length=100)
    text_uk = models.TextField(_("Відгук (укр)"))
    text_ru = models.TextField(_("Відгук (рос)"))
    rating = models.PositiveSmallIntegerField(
        _("Оцінка"),
        default=5,
        choices=[(i, str(i)) for i in range(1, 6)],
    )
    photo = CloudinaryField(_("Фото клієнта"), folder="reviews/", blank=True, null=True)
    service_uk = models.CharField(_("Послуга (укр)"), max_length=200, blank=True)
    service_ru = models.CharField(_("Послуга (рос)"), max_length=200, blank=True)
    created_at = models.DateField(_("Дата"))
    order = models.PositiveIntegerField(_("Порядок"), default=0)
    is_active = models.BooleanField(_("Активний"), default=True)

    class Meta:
        verbose_name = _("Відгук")
        verbose_name_plural = _("Відгуки")
        ordering = ["order", "-created_at"]

    def __str__(self) -> str:
        return f"{self.author_name} ({self.created_at})"
