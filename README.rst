================
Security Headers
================

Security Headers is a simple Django app to add configurable security headers to django responses.

Detailed documentation is in the "docs" directory.

Quick start
-----------

1. Add the middlewares::

   MIDDLEWARES = [
       ...
       "django.middleware.security.SecurityMiddleware",
       "csp.middleware.CSPMiddleware",
       "security_headers.middleware.extra_security_middleware"
   ]

2. (optional) Add the default settings by adding to your `settings.py`::

   from security_headers.settings import *
