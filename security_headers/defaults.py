# -*- coding: utf-8 -*-

# SecurityMiddleware settings
CSRF_COOKIE_SECURE = True  # set to False for localhost development
SECURE_BROWSER_XSS_FILTER = True
SECURE_CONTENT_TYPE_NOSNIFF = True
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True
SECURE_HSTS_SECONDS = 183 * 24 * 60 * 60  # 6-month default
SECURE_SSL_REDIRECT = True  # set to False for localhost development
SESSION_COOKIE_SECURE = True  # set to False for localhost development

# Sample Django-CSP settings
CSP_DEFAULT_SRC = ["'self'"]
CSP_FONT_SRC = ["'self'", "fonts.googleapis.com", "fonts.gstatic.com"]
CSP_FRAME_SRC = ["*"]
CSP_IMG_SRC = ["*", "data:"]
CSP_MEDIA_SRC = ["*", "data:"]
CSP_SCRIPT_SRC = ["'self'", "ajax.googleapis.com", "cdn.polyfill.io"]
CSP_STYLE_SRC = ["'self'", "fonts.googleapis.com"]
CSP_INCLUDE_NONCE_IN = ["script-src", "style-src"]
CSP_REPORT_PERCENTAGE = 0.1

# Default extra SecurityMiddleware settings
REFERRER_POLICY = "same-origin"
