import re


def convert_to_float(value: str) -> float:
    """convert_to_float _summary_

    Args:
        value (str): _description_

    Returns:
        float: _description_
    """

    try:
        return float(value.replace(",", "."))
    except Exception:
        f_value: str = re.findall(r"[0-9.,]+", value)[0]
        arr_value: list[str] = f_value.rsplit(",", 1)
        if len(arr_value) > 1:
            return float(arr_value[0].replace(".", "").replace(",", "") + "." + arr_value[1])
        arr_value: list[str] = f_value.rsplit(".", 1)
        if len(arr_value) > 1:
            if len(arr_value[1]) == 3:
                return float(arr_value[0].replace(".", "").replace(",", "") + arr_value[1])
            return float(arr_value[0].replace(".", "").replace(",", "") + "." + arr_value[1])
        if len(arr_value) == 0:
            return 0
        return float(f_value)


if __name__ == "__main__":
    print(convert_to_float("9,3"))
