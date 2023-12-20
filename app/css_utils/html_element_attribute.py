from enum import Enum


class HTMLElementAttribute(Enum):
    """HTMLElementAttribute Enum class that contains HTML element attributes combinators

    Args:
        Enum (_type_): _description_
    """
    ID = "id"
    CLASS = "class"
    TITLE = "title"
    HREF = "href"
    SRC = "src"
    ALT = "alt"
    LANG = "lang"
    DATA = "data-"
    TYPE = "type"
    VALUE = "value"
    NAME = "name"
    REL = "rel"
    CHARSET = "charset"
    FOR = "for"
    PLACEHOLDER = "placeholder"
    READONLY = "readonly"
    DISABLED = "disabled"
    CONTENT = "content"
    EMPTY_STR = ""


class HTMLElementClassAttribute(Enum):
    CLASS = "."
    EMPTY_STR = ""


class HTMLElementIdAttribute(Enum):
    ID = "#"
    EMPTY_STR = ""
