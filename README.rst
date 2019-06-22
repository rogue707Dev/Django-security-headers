================
Security Headers
================

Security Headers is a simple Django app, inspired by Scott Helme's _securityheaders.com: https://securityheaders.com, which adds configurable security headers to all Django responses.  It works in parallel with the excellent Django-CSP package maintained by Mozilla and aims to provide a basic framework for achieving an A+ grade.

Detailed documentation is available in the "docs" directory.


Quick start
-----------

1. Add the middleware: code:: python

    MIDDLEWARES = [
      "django.middleware.security.SecurityMiddleware",
      "csp.middleware.CSPMiddleware",
      "security_headers.middleware.extra_security_headers_middleware",
       ...
    ]


2. (Optional) If you wish to allow framing from certain domains, add the app to INSTALLED_APPS which will expose a simple admin interface for specifying safe domains: code:: python

    INSTALLED_APPS = [
      ...
      "security_headers",
      ...
    ]


3. (Optional) Add all default security header settings by importing to your local `settings.py`: code:: python

    from security_headers.defaults import *  # noqa


4. (Optional) During development using localhost server, it is recommended to overwrite some default settings (which requires SSL) at the very end of your `settings.py` file: code:: python

    CSRF_COOKIE_SECURE = not DEBUG
    SECURE_SSL_REDIRECT = not DEBUG
    SESSION_COOKIE_SECURE = not DEBUG


Development
-----------

1. To run localserver: code::python

    python security_headers.py runserver


2. To run tests: code:: python

    pytest
