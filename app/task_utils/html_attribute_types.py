from enum import Enum


class HTMLAttributeTypes(Enum):
    """Enumeration defining various HTML attribute types used for data extraction.

    This enum lists different types of HTML attributes commonly used for data extraction purposes,
    such as ID, class, title, href, src, alt, and more.

    Args:
        Enum (type): A Python enumeration for defining a set of named constants.

    Attributes:
        ID: Represents the 'id' attribute in HTML.
        CLASS: Represents the 'class' attribute in HTML.
        TITLE: Represents the 'title' attribute in HTML.
        HREF: Represents the 'href' attribute in HTML.
        SRC: Represents the 'src' attribute in HTML.
        ALT: Represents the 'alt' attribute in HTML.
        LANG: Represents the 'lang' attribute in HTML.
        DATA: Represents the 'data-' attribute in HTML.
        TYPE: Represents the 'type' attribute in HTML.
        VALUE: Represents the 'value' attribute in HTML.
        NAME: Represents the 'name' attribute in HTML.
        REL: Represents the 'rel' attribute in HTML.
        CHARSET: Represents the 'charset' attribute in HTML.
        FOR: Represents the 'for' attribute in HTML.
        PLACEHOLDER: Represents the 'placeholder' attribute in HTML.
        READONLY: Represents the 'readonly' attribute in HTML.
        DISABLED: Represents the 'disabled' attribute in HTML.
        CONTENT: Represents the 'content' attribute in HTML.
        TEXT_CONTENT: Represents the 'text_content' attribute in HTML.

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
    TEXT_CONTENT = "text_content"
