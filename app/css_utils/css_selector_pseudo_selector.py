from enum import Enum


class CSSSelectorPseudoSelector(Enum):
    """CSSSelectorPseudoSelector: Enum class that contains CSS pseudo selectors

    Args:
        Enum (_type_): _description_
    """
    HOVER = ":hover"
    ACTIVE = ":active"
    FOCUS = ":focus"
    FIRST_CHILD = ":first-child"
    LAST_CHILD = ":last-child"
    NTH_CHILD = ":nth-child"
    NOT = ":not"
    NTH_OF_TYPE = ":nth-of-type"
    FIRST_OF_TYPE = ":first-of-type"
    LAST_OF_TYPE = ":last-of-type"
    EMPTY = ":empty"
    ROOT = ":root"
    CHECKED = ":checked"
    DISABLED = ":disabled"
    ENABLED = ":enabled"
    TARGET = ":target"
    VISITED = ":visited"
    LANG = ":lang"
    HAS = ":has"
    LINK = ":link"
    IN_RANGE = ":in-range"
    INVALID = ":invalid"
    VALID = ":valid"
    REQUIRED = ":required"
    READ_WRITE = ":read-write"
    READ_ONLY = ":read-only"
    OUT_OF_RANGE = ":out-of-range"
    OPTIONAL = ":optional"
    ONLY_CHILD = ":only-child"
    ONLY_OF_TYPE = ":only-of-type"
    NTH_LAST_CHILD = ":nth-last-child"
    NTH_LAST_OF_TYPE = ":nth-last-of-type"
    AUTO_FILL = ":autofill"
    ANY_LINK = ":any-link"
    BUFFERING = ":buffering"
    CURRENT = ":current"
    DEFAULT = ":default"
    DEFINED = ":defined"
    DIR = ":dir"
    FIRST = ":first"
    FOCUS_VISIBLE = ":focus-visible"
    FOCUS_WITHIN = ":focus-within"
    FULL_SCREEN = ":fullscreen"
    HOST = ":host"
    HOST_CONTEXT = ":host-context"
    INDETERMINATE = ":indeterminate"
    IS = ":is"
    LEFT = ":left"
    LOCAL_LINK = ":local-link"
    MODAL = ":modal"
    MUTED = ":muted"
    PAUSED = ":paused"
    PICTURE_IN_PICTURE = ":picture-in-picture"
    PLACEHOLDER_SHOWN = ":placeholder-shown"
    PLAYING = ":playing"
    RIGHT = ":right"
    SCOPE = ":scope"
    SEEKING = ":seeking"
    STALLED = ":stalled"
    USER_INVALID = ":user-invalid"
    USER_VALID = ":user-valid"
    VOLUME_LOCKED = ":volume-locked"
    WHERE = ":where"
    EMPTY_STR = ""
