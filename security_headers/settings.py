# -*- coding: utf-8 -*-
import django
import os
from packaging import version
import sys


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SECRET_KEY = "security-headers"

DEBUG = True

ALLOWED_HOSTS = ["*"]

ROOT_URLCONF = "security_headers.urls"

INSTALLED_APPS = [
    "security_headers",
    "sslserver",  # For development and local testing only
    "csp",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
]

if version.parse(django.get_version()) < version.parse("2.1"):
    MIDDLEWARE = [
        "django.middleware.security.SecurityMiddleware",
        "csp.middleware.CSPMiddleware",
        "security_headers.middleware.extra_security_headers_middleware",
        "django_cookies_samesite.middleware.CookiesSameSite",
        "django.contrib.sessions.middleware.SessionMiddleware",
        "django.middleware.common.CommonMiddleware",
        "django.middleware.csrf.CsrfViewMiddleware",
        "django.contrib.auth.middleware.AuthenticationMiddleware",
        "django.contrib.messages.middleware.MessageMiddleware",
    ]
else:
    MIDDLEWARE = [
        "django.middleware.security.SecurityMiddleware",
        "csp.middleware.CSPMiddleware",
        "security_headers.middleware.extra_security_headers_middleware",
        "django.contrib.sessions.middleware.SessionMiddleware",
        "django.middleware.common.CommonMiddleware",
        "django.middleware.csrf.CsrfViewMiddleware",
        "django.contrib.auth.middleware.AuthenticationMiddleware",
        "django.contrib.messages.middleware.MessageMiddleware",
    ]

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [os.path.join(BASE_DIR, "templates")],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ]
        },
    }
]

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": os.path.join(BASE_DIR, "db.sqlite3"),
    }
}

STATIC_URL = "/static/"

try:
    from .defaults import *  # noqa
except ImportError:
    import warnings

    warnings.warn("File defaults.py not found.")  # noqa

if "runsslserver" in sys.argv:
    SSL_CONTEXT = True
else:
    SSL_CONTEXT = False

CSRF_COOKIE_SECURE = SSL_CONTEXT
SECURE_SSL_REDIRECT = SSL_CONTEXT
SESSION_COOKIE_SECURE = SSL_CONTEXT

HEADLESS_TESTING = True
