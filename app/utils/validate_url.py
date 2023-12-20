from urllib.parse import urlparse

from pydantic import validate_call


@validate_call(validate_return=True)
def is_valid_url(url):
    """is_valid_url _summary_

    Args:
        url (_type_): _description_

    Returns:
        _type_: _description_
    """
    try:
        parsed_url = urlparse(url)
    except ValueError:
        return False
    if not parsed_url.scheme:
        return False
    if not parsed_url.netloc:
        return False
    return True
