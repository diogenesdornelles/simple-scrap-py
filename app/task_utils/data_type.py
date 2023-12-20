from enum import Enum


class DataType(Enum):
    """Enumeration representing different data types that can be retrieved.

    This enum lists the various data types that can be obtained, including string, float, int, and list.

    Args:
        Enum (type): A Python enumeration for defining a set of named constants.

    Attributes:
        STRING: Represents the 'string' data type.
        FLOAT: Represents the 'float' data type.
        INT: Represents the 'int' data type.
        LIST: Represents the 'list' data type.

    """
    STRING = "string"
    FLOAT = "float"
    INT = "int"
    LIST = "list"
