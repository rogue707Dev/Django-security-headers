================
Security Headers
================

Security Headers is a simple Django app (originally inspired by Scott Helme's `securityheaders.com <https://securityheaders.com>`_) that adds configurable security headers to all Django responses.  It works in parallel with the excellent `Django-CSP <https://github.com/mozilla/django-csp>`_ package and is self-tested using the `Http Observatory <https://github.com/mozilla/http-observatory>`_ both maintained by Mozilla.  The goal of this package is to provide a basic framework for achieving an A+ grade.

Detailed documentation is available in the "docs" directory.


Quick start
-----------

1. Add the middleware: highlight::

    MIDDLEWARES = [
      "django.middleware.security.SecurityMiddleware",
      "csp.middleware.CSPMiddleware",
      "security_headers.middleware.extra_security_headers_middleware",
       ...
    ]


2. (Optional) If you wish to allow framing from certain domains, add the app to INSTALLED_APPS which will expose a simple admin interface for specifying safe domains:  highlight::

    INSTALLED_APPS = [
      ...
      "security_headers",
      ...
    ]


3. (Optional) Add all default security header settings by importing to your local `settings.py`:  highlight::

    from security_headers.defaults import *  # noqa


4. (Optional) During development using http localhost server, at the very end of your `settings.py` file you will need to overwrite some default settings which require SSL.  Reducing SECURE_HSTS_SECONDS time is also a good idea: highlight::

    CSRF_COOKIE_SECURE = not DEBUG
    SECURE_SSL_REDIRECT = not DEBUG
    SESSION_COOKIE_SECURE = not DEBUG
    SECURE_HSTS_SECONDS = 3600


Development
-----------

1. Install dev requirements:  highlight::

    pip install -r requirements/dev-requirements.txt
    
    
2. Install pre-commit hooks:  highlight::

    pre-commit install
    

3. To run localserver:  highlight::

    python security_headers.py runserver


4. To run tests or to get http-observatory scan report, start a secure localhost (at 127.0.0.1:8000) to enable https:  highlight::

    python security_headers.py runsslserver


5. Run test suite as a separate process:  highlight::

    pytest
