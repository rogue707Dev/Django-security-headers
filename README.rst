================
Security Headers
================

Security Headers is a simple Django app to add configurable security headers to django responses.

Detailed documentation is in the "docs" directory.

Quick start
-----------

1. Add "security_headers" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = [
        ...
        'security_headers',
    ]

2. Add the security_headers middleware.

3. Update settings.py for configurable options.
