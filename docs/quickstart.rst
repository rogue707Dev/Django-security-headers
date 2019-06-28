Quick start
===========


Default configuration
---------------------

To apply default security headers to all responses:


1. Install from ``pip`` ::

    pip install django-security-headers


2. Add the ``csp`` and ``security_headers`` middleware ::

    MIDDLEWARES = [
      "django.middleware.security.SecurityMiddleware",
      "csp.middleware.CSPMiddleware",
      "security_headers.middleware.extra_security_headers",
      "django_cookies_samesite.middleware.CookiesSameSite",
       ...
    ]

3. Add the default ``csp`` and ``security_headers`` settings by importing the defaults to your local ``settings.py``  ::

    from security_headers.defaults import *


Optional configuration
----------------------

To permit framing from whitelisted domains, add ``security_headers`` to your ``INSTALLED_APPS``.  ::

    INSTALLED_APPS = [
      ...
      "security_headers",
      ...
    ]

This will expose a simple admin interface for specifying safe domains.  To access template tags provided by ``django-csp``, install ``csp`` as well  ::

    INSTALLED_APPS = [
      ...
      "security_headers",
      "csp",
      ...
    ]



Development settings
--------------------

During development using http localhost server, you will need to overwrite some default settings that require SSL.  At the very end of your ``settings.py`` file, include ::

    CSRF_COOKIE_SECURE = not DEBUG
    SECURE_SSL_REDIRECT = not DEBUG
    SESSION_COOKIE_SECURE = not DEBUG
    SECURE_HSTS_SECONDS = 3600

Reducing ``SECURE_HSTS_SECONDS`` time is also a good idea during development.
