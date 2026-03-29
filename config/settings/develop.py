from .base import *  # noqa: F401, F403

DEBUG = True

EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"

# Use local file storage in dev (no Cloudinary needed)
DEFAULT_FILE_STORAGE = "django.core.files.storage.FileSystemStorage"
