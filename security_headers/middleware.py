# -*- coding: utf-8 -*-
from django.conf import settings
from django.core.exceptions import ImproperlyConfigured, ObjectDoesNotExist

from security_headers.models import FramingAllowedFrom


def extra_security_headers_middleware(get_response):
    """
    Sets security headers specified in SETTINGS on all responses.
    """

    def middleware(req):
        resp = get_response(req)

        domain = req.get_host()

        try:
            allowed_domains = settings.FRAMING_ALLOWED_FROM
            if not isinstance(allowed_domains, list):
                raise ImproperlyConfigured(
                    """
                    If specified in settings.py, FRAMING_ALLOWED_FROM must be a
                    list of allowed domains.

                    As a security measure, any list specified in settings.py
                    overrides any database entries to provide sys admins with a
                    veto over user settings.
                    """
                )

            if "*" in allowed_domains or domain in allowed_domains:
                resp["X-Frame-Options"] = "allow-from {}".format(domain)
            else:
                resp["X-Frame-Options"] = "deny"

        except AttributeError:
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
