Default settings
================


Django settings
---------------

CSRF_COOKIE_NAME_
~~~~~~~~~~~~~~~~~

.. _CSRF_COOKIE_NAME: https://docs.djangoproject.com/en/2.2/ref/settings/#csrf-cookie-name

Default: ``__Host-csrftoken``

.. tip::
    See the Mozilla Http Observatory recommendations regarding `cookies <https://infosec.mozilla.org/guidelines/web_security#directives-2>`_.


CSRF_COOKIE_SAMESITE_
~~~~~~~~~~~~~~~~~~~~~

.. _CSRF_COOKIE_SAMESITE: https://docs.djangoproject.com/en/2.2/ref/settings/#csrf-cookie-samesite

Default:  ``Lax``

.. note::
    This setting is available in Django 2.2 or through the ``django-cookie-samesite`` package in Django 1.11.


CSRF_COOKIE_SECURE_
~~~~~~~~~~~~~~~~~~~

.. _CSRF_COOKIE_SECURE: https://docs.djangoproject.com/en/2.2/ref/settings/#csrf-cookie-secure/

Default: ``True``

.. note::
    Requires an HTTPS connection.


SECURE_BROWSER_XSS_FILTER_
~~~~~~~~~~~~~~~~~~~~~~~~~~

.. _SECURE_BROWSER_XSS_FILTER: https://docs.djangoproject.com/en/2.2/ref/settings/#secure-browser-xss-filter

Default: ``True``


SECURE_CONTENT_TYPE_NOSNIFF_
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. _SECURE_CONTENT_TYPE_NOSNIFF: https://docs.djangoproject.com/en/2.2/ref/settings/#secure-content-type-nosniff

Default: ``True``


SECURE_HSTS_INCLUDE_SUBDOMAINS_
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. _SECURE_HSTS_INCLUDE_SUBDOMAINS: https://docs.djangoproject.com/en/2.2/ref/settings/#secure-hsts-include-subdomains

Default: ``True``

.. warning::
    Activating HSTS may irreversibly break your site (for ``SECURE_HSTS_SECONDS``) if improperly configured.  Review `Django's advice <https://docs.djangoproject.com/en/2.2/ref/middleware/#http-strict-transport-security>`_ regarding HSTS first!


SECURE_HSTS_PRELOAD_
~~~~~~~~~~~~~~~~~~~~

.. _SECURE_HSTS_PRELOAD: https://docs.djangoproject.com/en/2.2/ref/settings/#secure-hsts-preload

Default: ``True``

.. warning::
    Activating HSTS may irreversibly break your site (for ``SECURE_HSTS_SECONDS``) if improperly configured.  Review `Django's advice <https://docs.djangoproject.com/en/2.2/ref/middleware/#http-strict-transport-security>`_ regarding HSTS first!


SECURE_HSTS_SECONDS_
~~~~~~~~~~~~~~~~~~~~

.. _SECURE_HSTS_SECONDS: https://docs.djangoproject.com/en/2.2/ref/settings/#secure-hsts-seconds

Default:  183 * 24 * 60 * 60

.. warning::
    Activating HSTS may irreversibly break your site (for ``SECURE_HSTS_SECONDS``) if improperly configured.  Review `Django's advice <https://docs.djangoproject.com/en/2.2/ref/middleware/#http-strict-transport-security>`_ regarding HSTS first!


SESSION_COOKIE_HTTPONLY_
~~~~~~~~~~~~~~~~~~~~~~~~

.. _SESSION_COOKIE_HTTPONLY: https://docs.djangoproject.com/en/2.2/ref/settings/#session-cookie-httponly

Default:  ``True``

.. hint::
    This is already true by default in Django 1.11 and 2.2.


SESSION_COOKIE_SAMESITE_
~~~~~~~~~~~~~~~~~~~~~~~~

.. _SESSION_COOKIE_SAMESITE: https://docs.djangoproject.com/en/2.2/ref/settings/#session-cookie-samesite

Default:  ``Lax``

.. note::
    This setting is available in Django 2.2 or through ``django-cookie-samesite`` package in Django 1.11.


SESSION_COOKIE_SECURE_
~~~~~~~~~~~~~~~~~~~~~~

.. _SESSION_COOKIE_SECURE: https://docs.djangoproject.com/en/2.2/ref/settings/#session-cookie-secure

Default:  ``True``

.. note::
    Requires an HTTPS connection.

Django-CSP settings
-------------------

See the `django-csp docs <https://django-csp.readthedocs.io/en/latest/>`_ for full details.

CSP_DEFAULT_SRC
~~~~~~~~~~~~~~~

Default: ``["'self'"]``


CSP_FONT_SRC
~~~~~~~~~~~~

Default: ``["'self'"]``


CSP_FRAME_SRC
~~~~~~~~~~~~~

Default: ``["*"]``

CSP_IMG_SRC
~~~~~~~~~~~

Default:  ``["*", "data:"]``


CSP_MEDIA_SRC
~~~~~~~~~~~~~

Default: ``["*", "data:"]``


CSP_SCRIPT_SRC
~~~~~~~~~~~~~~

Default: ``["'self'"]``


CSP_STYLE_SRC
~~~~~~~~~~~~~

Default: ``["'self'"]``


CSP_INCLUDE_NONCE_IN
~~~~~~~~~~~~~~~~~~~~

Default: ``["script-src", "style-src"]``

CSP_UPGRADE_INSECURE_REQUESTS
~~~~~~~~~~~~~~~~~~~~

Default: ``True``

CSP_BLOCK_ALL_MIXED_CONTENT
~~~~~~~~~~~~~~~~~~~~

Default: ``True``

CSP_REPORT_PERCENTAGE
~~~~~~~~~~~~~~~~~~~~~

Default: ``0.1``


Middleware settings
-------------------

REFERRER_POLICY
~~~~~~~~~~~~~~~

Default:  ``same-origin``

.. tip::
    See the Mozilla Http Observatory recommendations regarding the `referrer-policy <https://infosec.mozilla.org/guidelines/web_security#referrer-policy>`_ as well as Scott Helme's `discussion <https://scotthelme.co.uk/a-new-security-header-referrer-policy/>`_.

FEATURE_POLICY
~~~~~~~~~~~~~~

Default: ::

    [
        "autoplay 'none'",
        "camera 'none'",
        "display-capture 'none'",
        "document-domain 'none'",
        "encrypted-media 'none'",
        "fullscreen *",
        "geolocation 'none'",
        "microphone 'none'",
        "midi 'none'",
        "payment 'none'",
        "vr *",
    ]

.. tip::
    See Scott Helme's discussion on the new `feature policy header <https://scotthelme.co.uk/a-new-security-header-feature-policy/>`_.
