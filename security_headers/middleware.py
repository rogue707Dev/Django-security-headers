# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf import settings


def extra_security_headers_middleware(get_response):
    """
    Sets all wanted security headers common to all responses.
    """

    def middleware(req):
        resp = get_response(req)

        iframe_allowed_from = settings.get("FRAMING_ALLOWED_FROM", [])
        if iframe_allowed_from:
            resp["X-Frame-Options"] = "allow-from {}".format(
                " ".join(iframe_allowed_from)
            )

        resp["Referrer-Policy"] = settings.get(
            "REFERRER_POLICY", "same-origin"
        )

        return resp

    return middleware
