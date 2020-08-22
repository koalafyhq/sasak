import re
import hmac
import hashlib

from hmac import HMAC
from typing import Pattern
from flask import current_app

ALLOWED_EXTENSIONS = {"png", "jpg", "jpeg", "gif"}

DEFAULT_HEADERS = {
    "X-Frame-Options": "deny",
    "X-XSS-Protection": "1; mode=block",
    "X-Content-Type-Options": "nosniff",
    "Content-Security-Policy": "default-src 'none'; img-src data:; style-src 'unsafe-inline'",
    "Strict-Transport-Security": "max-age=31536000; includeSubDomains",
}

def valid_url(url: str) -> bool:
    # valid value is http(s)://(ip|domain.tld):(port)
    url_re: Pattern[str] = re.compile(
        r'^(?:http)s?://'
        r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|'
        r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})'
        r'(?::\d+)?'
        r'(?:/?|[/?]\S+)$', re.IGNORECASE)

    return re.match(url_re, url) is not None

def get_signature(url: str) -> str:
    secret: str = current_app.config["SECRET_KEY"]

    key: bytes = bytes(secret, "utf-8")
    msg: bytes = bytes(url, "utf-8")

    signature: HMAC = hmac.new(key, msg, hashlib.sha1)

    return signature.hexdigest()
