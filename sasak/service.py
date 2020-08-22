import requests

from typing import Tuple, Union
from flask import current_app
from requests import Response

from .helpers import ALLOWED_EXTENSIONS

def check_is_proxiable(url: str) -> bool:
    res: Response = requests.head(url, allow_redirects=True)

    content_type: str = res.headers.get("content-type") or ""
    content_length: str = res.headers.get("content-length") or ""

    try:
        extension: str = content_type.split("/")[1].lower()

        if extension not in ALLOWED_EXTENSIONS:
            return False
    except:
        return False

    if content_length:
        return int(content_length) < current_app.config["MAX_SIZE_IN_MB"] * 1024 * 1024

    return False

def proxy_image(url: str) -> Union[Response, Tuple[str, int, None]]:
    proxiable: bool = check_is_proxiable(url)

    if not proxiable:
        return "Content type is not supported or image size is too big", 422, None

    req: Response = requests.get(url)

    if req.status_code == 404:
        return "Image not found", 404, None

    if req.status_code != 200:
        return "Something went wrong", 500, None

    return req
