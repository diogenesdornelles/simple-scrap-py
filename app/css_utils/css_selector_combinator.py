from enum import Enum


class CSSSelectorCombinator(Enum):
    """CSSSelectorCombinator: Enum class that contains CSS combinators

    Args:
        Enum Enum class
    """
    EMPTY_STR = ""
    UNIVERSAL = "*"
    START = "^"
    END = "$"
    SUBSEQUENT_SIBLING = "~"
    CHILD = ">"
    DESCENDANT = " "
    NEXT_SIBLING = "+"
    GROUPING = ","
