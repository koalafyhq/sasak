from .service import proxy_image
from .helpers import valid_url, get_signature, DEFAULT_HEADERS

from flask import Blueprint, make_response
from flask.wrappers import Response
from typing import Union, Tuple, cast
from requests import Response as requestsResponse

blueprint: Blueprint = Blueprint("sasak", __name__)

@blueprint.route("/<digest>/<url_hex>", methods=["GET"])
def get(digest: str, url_hex: str) -> Response:
    try:
        url: str = bytes.fromhex(url_hex).decode("utf-8")

        if not valid_url(url):
            return make_response("URL is not valid", 422)
    except:
        return make_response("Hex is not valid", 422)

    signature: str = get_signature(url)

    if (digest != signature):
        return make_response("Signature is not match", 403)

    proxy_response: Union[requestsResponse, Tuple[str, int, None]] = proxy_image(url)
    ok_response = all(proxy_response)

    if not ok_response:
        return make_response(proxy_response)

    res = cast(requestsResponse, proxy_response)
    response: Response = make_response(res.content)

    for k, v in DEFAULT_HEADERS.items():
        response.headers.set(k, v)

    response.headers.set("etag", signature)
    response.headers.set("content-type", res.headers["content-type"])

    return response
