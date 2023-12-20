from enum import Enum


class Subtype(Enum):
    """Enumeration representing different data subtypes in type list that can be retrieved.

    This enum lists the various data types that can be obtained, including string, float e int.

    Args:
        Enum (type): A Python enumeration for defining a set of named constants.

    Attributes:
        STRING: Represents the 'string' data type.
        FLOAT: Represents the 'float' data type.
        INT: Represents the 'int' data type.

    """
    STRING = "string"
    FLOAT = "float"
    INT = "int"
