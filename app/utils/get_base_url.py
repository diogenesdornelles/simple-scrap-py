from difflib import ndiff

from pydantic import validate_call


@validate_call(validate_return=True)
def get_base_url(link_a: str, link_b: str) -> str | None:
    """get_base_url _summary_

    Args:
        link_a (str): _description_
        link_b (str): _description_

    Returns:
        str: _description_
    """
    differences = list(ndiff(link_a, link_b))
    common_part = ''.join([diff[2:] for diff in differences if diff.startswith(' ')])
    if common_part.find('http://') == 0 or common_part.find('https://') == 0:
        return common_part
    else:
        return None
