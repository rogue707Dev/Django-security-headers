import os
import sys

from django.conf import settings
from django.conf.urls import url
from django.contrib import admin
from django.core.wsgi import get_wsgi_application
from django.http import HttpResponse


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

settings.configure(
    SECRET_KEY="security-headers",
    DEBUG=True,
    ROOT_URLCONF=__name__,
    INSTALLED_APPS=[
        "security_headers",
        "django.contrib.admin",
        "django.contrib.auth",
        "django.contrib.contenttypes",
        "django.contrib.sessions",
        "django.contrib.messages",
        "django.contrib.staticfiles",
    ],
    MIDDLEWARE=[
        "django.middleware.security.SecurityMiddleware",
        "django.contrib.sessions.middleware.SessionMiddleware",
        "django.middleware.common.CommonMiddleware",
        "django.middleware.csrf.CsrfViewMiddleware",
        "django.contrib.auth.middleware.AuthenticationMiddleware",
        "django.contrib.messages.middleware.MessageMiddleware",
    ],
    TEMPLATES=[
        {
            "BACKEND": "django.template.backends.django.DjangoTemplates",
            "DIRS": [os.path.join(BASE_DIR, "templates")],
            "APP_DIRS": True,
            "OPTIONS": {
                "context_processors": [
                    "django.template.context_processors.debug",
                    "django.template.context_processors.request",
                    "django.contrib.auth.context_processors.auth",
                ]
            },
        }
    ],
    DATABASES={
        "default": {
            "ENGINE": "django.db.backends.sqlite3",
            "NAME": os.path.join(BASE_DIR, "db.sqlite3"),
        }
    },
    STATIC_URL="/static/",
)

application = get_wsgi_application()


def ping(request):
    return HttpResponse("Pong")


urlpatterns = (url(r"^$", ping), url(r"^admin/", admin.site.urls))

if __name__ == "__main__":
    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
