from enum import Enum


class CSSSelectorPseudoElement(Enum):
    """CSSSelectorPseudoElement Enum class that contains CSS pseudo elements

    Args:
        Enum (_type_):
    """
    BEFORE = "::before"
    AFTER = "::after"
    FIRST_LINE = "::first-line"
    FIRST_LETTER = "::first-letter"
    SELECTION = "::selection"
    MARKER = "::marker"
    EMPTY_STR = ""
