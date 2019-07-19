# -*- coding: utf-8 -*-
from django.conf import settings
from django.core.exceptions import ObjectDoesNotExist

from security_headers.models import FramingAllowedFrom


def extra_security_headers_middleware(get_response):
    """
    Sets security headers specified in SETTINGS on all responses.
    """

    def middleware(req):
        resp = get_response(req)

        try:
            allowed_domain = FramingAllowedFrom.objects.get(domain=req.get_host())
            resp["X-Frame-Options"] = "allow-from {}".format(allowed_domain)
        except ObjectDoesNotExist:
            resp["X-Frame-Options"] = "deny"

        if hasattr(settings, "REFERRER_POLICY"):
            resp["Referrer-Policy"] = settings.REFERRER_POLICY
        else:
            resp["Referrer-Policy"] = "same-origin"

        if hasattr(settings, "FEATURE_POLICY"):
            resp["Feature-Policy"] = "; ".join(settings.FEATURE_POLICY)
        else:
            resp["Feature-Policy"] = "; ".join(
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
            )

        return resp

    return middleware
