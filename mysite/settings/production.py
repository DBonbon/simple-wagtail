from .base import *

DEBUG = True
SECRET_KEY = "django-insecure-yue(b!9h^a+d(ue57q2)pu+)bb(h3a0r-ta(q^q_!-sy=2r_oe"
ALLOWED_HOSTS = ["*"]

EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"
try:
    from .local import *
except ImportError:
    pass
