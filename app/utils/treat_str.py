def treat_str(value: str) -> str:
    """treat_str _summary_

    Args:
        value (str): _description_

    Returns:
        str: _description_
    """
    if not value:
        return ''
    value = value.strip()
    return value
