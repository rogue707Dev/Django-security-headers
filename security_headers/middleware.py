# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf import settings


def extra_security_headers_middleware(get_response):
    """
    Sets all wanted security headers common to all responses.
    """

    def middleware(req):
        resp = get_response(req)

        if hasattr(settings, "FRAMING_ALLOWED_FROM"):
            resp["X-Frame-Options"] = "allow-from {}".format(
                " ".join(settings.FRAMING_ALLOWED_FROM)
            )
        else:
            resp["X-Frame-Options"] = "deny"

        if hasattr(settings, "REFERRER_POLICY"):
            resp["Referrer-Policy"] = settings.REFERRER_POLICY
        else:
            resp["Referrer-Policy"] = "same-origin"

        return resp

    return middleware
