from .base import *  # noqa: F401, F403

DEBUG = False

SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")
SECURE_SSL_REDIRECT = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True

CSRF_TRUSTED_ORIGINS = [
    o.strip() for o in os.environ.get("CSRF_TRUSTED_ORIGINS", "").split(",") if o.strip()  # type: ignore # noqa: F405
]

EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"

SESSION_ENGINE = "django.contrib.sessions.backends.signed_cookies"
