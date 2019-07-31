# -*- coding: utf-8 -*-

# SecurityMiddleware settings
CSRF_COOKIE_HTTPONLY = True
CSRF_COOKIE_NAME = "__Host-csrftoken"
CSRF_COOKIE_SECURE = True
SECURE_BROWSER_XSS_FILTER = True
SECURE_CONTENT_TYPE_NOSNIFF = True
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True
SECURE_HSTS_SECONDS = 183 * 24 * 60 * 60  # 6-month default
SECURE_SSL_REDIRECT = True
SESSION_COOKIE_HTTPONLY = True
SESSION_COOKIE_SECURE = True

# Django 1.11 patches for Django 2.1 functionality
CSRF_COOKIE_SAMESITE = "Lax"
SESSION_COOKIE_SAMESITE = "Lax"

# Sample Django-CSP settings
CSP_DEFAULT_SRC = ["'self'"]
CSP_FONT_SRC = ["'self'"]
CSP_FRAME_SRC = ["*"]
CSP_IMG_SRC = ["*", "data:"]
CSP_MEDIA_SRC = ["*", "data:"]
CSP_SCRIPT_SRC = ["'self'"]
CSP_STYLE_SRC = ["'self'"]
CSP_INCLUDE_NONCE_IN = ["script-src", "style-src"]
CSP_UPGRADE_INSECURE_REQUESTS = True
CSP_BLOCK_ALL_MIXED_CONTENT = True
CSP_REPORT_PERCENTAGE = 0.1

# Default extra security header settings
REFERRER_POLICY = "same-origin"
FEATURE_POLICY = [
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
