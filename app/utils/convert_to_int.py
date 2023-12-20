import re
from math import trunc


def convert_to_int(value: str) -> float:
    """convert_to_int _summary_

    Args:
        value (str): _description_

    Returns:
        float: _description_
    """
    if re.match(r'^-?\d+[\.,]?\d*$', value):
        value = re.sub(r'[^\d\.,]', '', value)
        value = value.replace(',', '.')
        return int(trunc(float(value)))
    else:
        return 0
