Quick start
===========


Default configuration
---------------------

To apply default security headers to all responses:


1. Installation

    a. From ``pip`` ::

        pip install django-security-headers


    b. To access the ``scan`` function from ``httpobs``, add the following to your project's dev requirements ::

        -e git+https://github.com/jsumnerPhD/http-observatory#egg=httpobs


2. Add the ``csp``, ``security_headers``, and ``samesite`` middlewares ::

    MIDDLEWARES = [
      "django.middleware.security.SecurityMiddleware",
      "csp.middleware.CSPMiddleware",
      "security_headers.middleware.extra_security_headers",
      "django_cookies_samesite.middleware.CookiesSameSite",
       ...
    ]

3. Add the default ``csp`` and ``security_headers`` settings by importing the defaults to your local ``settings.py``  ::

    from security_headers.defaults import *

4. (Optional) If you included step 1b, you can add a scan link to ``urls.py``.  Accessing this link will run a scan against ``https://127.0.0.1:8000/<path>`` where the path is determined from reversing ``url_name``.  Note that the sslserver must be running in parallel to the request.  ::

    from security_headers.views import scan_url

    if settings.DEBUG:
        urlpatterns += [
            url(
                r"^security/(?P<url_name>[\w-]+)/",
                scan_url,
                name="scan",
            ),
        ]

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

To use the sslserver ::

    INSTALLED_APPS = [
      ...
      "security_headers",
      "csp",
      "sslserver",
      ...
    ]



Development settings
--------------------

During development using http localhost server, you will need to overwrite some default settings when not using the ssl server.  At the very end of your ``settings.py`` file, include ::

    if "runsslserver" in sys.argv:
        SSL_CONTEXT = True
    else:
        SSL_CONTEXT = False

    CSRF_COOKIE_SECURE = SSL_CONTEXT
    SECURE_SSL_REDIRECT = SSL_CONTEXT
    SESSION_COOKIE_SECURE = SSL_CONTEXT

    SECURE_HSTS_SECONDS = 3600

Reducing ``SECURE_HSTS_SECONDS`` time is also a good idea during development.
