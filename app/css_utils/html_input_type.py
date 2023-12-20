from enum import Enum


class HTMLInputType(Enum):
    """HTMLInputType: Enum class that contains HTML input types

    Args:
        Enum (_type_):
    """

    TEXT = "text"
    PASSWORD = "password"
    CHECKBOX = "checkbox"
    RADIO = "radio"
    SUBMIT = "submit"
    RESET = "reset"
    BUTTON = "button"
    FILE = "file"
    IMAGE = "image"
    HIDDEN = "hidden"
    RANGE = "range"
    COLOR = "color"
    DATE = "date"
    DATETIME_LOCAL = "datetime-local"
    DATETIME = "datetime"
    MONTH = "month"
    WEEK = "week"
    TIME = "time"
    URL = "url"
    EMAIL = "email"
    TEL = "tel"
    NUMBER = "number"
    SEARCH = "search"
    METER = "meter"
    PROGRESS = "progress"
    OUTPUT = "output"
    DATALIST = "datalist"
    SELECT = "select"
    OPTION = "option"
    SOURCE = "source"
    TRACK = "track"
    EMPTY_STR = ""
