Quick start
===========

.. danger::
    The default security settings set by this package are aggressive, especially concerning HSTS.  Do not deploy in a production environment with default settings unless you are certain your server configuration is compatible.


Default configuration
---------------------

To apply default security headers to all responses:


1. Installation

    a. From ``pip`` ::

        pip install django-security-headers


    b. To access the ``scan`` function from ``httpobs``, add the following to your project's dev requirements ::

        -e git+https://github.com/jsumnerPhD/http-observatory#egg=httpobs


2. Add the ``csp``, ``security_headers`` middlewares.  For Django 1.11, also add the ``samesite`` middleware  ::

    MIDDLEWARES = [
      "django.middleware.security.SecurityMiddleware",
      "csp.middleware.CSPMiddleware",
      "security_headers.middleware.extra_security_headers_middleware",
      "django_cookies_samesite.middleware.CookiesSameSite", # Not needed for Django 2.2
       ...
    ]


3. Add ``security_headers`` to your ``INSTALLED_APPS``.  ::

    INSTALLED_APPS = [
      ...
      "security_headers",
      ...
    ]

This will expose a simple admin interface for specifying safe domains.


Optional configuration
----------------------

If you included step 1b, you can add a scan link to ``urls.py``.  Accessing this link will run a scan against ``https://127.0.0.1:8000/<path>`` where the path is determined from reversing ``url_name``.  Note that the sslserver must be running in parallel to the request.  ::

    from security_headers.views import scan_url

    if settings.DEBUG:
        urlpatterns += i18n_patterns(
            url(r"^security/(?P<url_name>[\w-]+)/", scan_url, name="scan")
        )

For newer Django syntax ::

    urlpatterns += [path("security/<slug:url_name>/", scan_url, name="scan")]


To access template tags provided by ``django-csp``, add ``csp`` to ``INSTALLED_APPS``  ::

    INSTALLED_APPS = [
      ...
      "security_headers",
      "csp",
      ...
    ]

To use the sslserver (provided by `django-sslserver <https://github.com/teddziuba/django-sslserver>`_ through ``./manage.py runsslserver``) ::

    INSTALLED_APPS = [
      ...
      "security_headers",
      "csp",
      "sslserver",
      ...
    ]



Development settings
--------------------

During development, you will need to overwrite some default settings if not using the ssl server.  At the very end of your ``settings.py`` file, include (this is conveniently done through an imported ``local_settings.py``)::

    if "runsslserver" in sys.argv:
        SSL_CONTEXT = True
        SECURE_HSTS_SECONDS = 3600
    else:
        SSL_CONTEXT = False
        SECURE_HSTS_SECONDS = 0
        CSRF_COOKIE_NAME = 'csrftoken'

    CSRF_COOKIE_SECURE = SSL_CONTEXT
    SECURE_SSL_REDIRECT = SSL_CONTEXT
    SESSION_COOKIE_SECURE = SSL_CONTEXT

Reducing ``SECURE_HSTS_SECONDS`` time is also a good idea during development.
