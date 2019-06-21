================
Security Headers
================

Security Headers is a simple Django app to add configurable security headers to django responses.

Detailed documentation is in the "docs" directory.

Quick start
-----------

1. Add the middleware: code:: python

    MIDDLEWARES = [
       "django.middleware.security.SecurityMiddleware",
       "csp.middleware.CSPMiddleware",
       "security_headers.middleware.extra_security_middleware",
       ...
    ]


2. (Optional) Add the app so that domains from which FRAMING_ALLOWED_FROM should be true can be set in the admin: code:: python

    INSTALLED_APPS = [
     ...
     "security_headers",
     ...
    ]


3. (Optional) Add the default settings by adding to your local `settings.py`: code:: python

    from security_headers.settings import *


4. (Optional) To run localserver: code::python

    python settings.py runserver


5. (Optional) Set up a local sqlite3 db for testing.  Run the following from the python shell and then create a superuser: code::python

    import sqlite3
    sqlite3.connect("db.sqlite3")


6. (optional) For development using a localhost server, it's also recommended to add to your `settings.py` code:: python

   CSRF_COOKIE_SECURE = not DEBUG
   SECURE_SSL_REDIRECT = not DEBUG
   SESSION_COOKIE_SECURE = not DEBUG
