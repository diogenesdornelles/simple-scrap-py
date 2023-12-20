from typing import Optional

from css_utils import CSSSelectorBuilder
from pydantic import BaseModel, Field, root_validator

from .column import Column
from .data_type import DataType
from .html_attribute_types import HTMLAttributeTypes
from .subtype import Subtype


class DataGetter(BaseModel):
    """Model representing a data getter for extracting information from HTML content.

    DataGetter defines attributes necessary for retrieving data such as name, selector, HTML attributes,
    data types, subtype, and preprocessing requirements.

    Args:
        BaseModel (DataType_): Base Pydantic model for defining attributes.

    Attributes:
        name (Column): The name of the data to retrieve.
        selector (CSSSelectorBuilder): CSS selector for locating HTML elements.
        attr (HTMLAttributeTypes): HTML attribute types to extract data.
        type (DataType): Type of data to retrieve.
        subtype (Optional[Subtype]): Subtype of data (if applicable).
        preprocess (Optional[bool]): Flag indicating whether preprocessing is required (default is True).
    """

    name: Column = Field(..., kw_only=True, title="name data to get")
    selector: CSSSelectorBuilder = Field(..., kw_only=True)
    attr: HTMLAttributeTypes = Field(..., kw_only=True)
    type: DataType = Field(..., kw_only=True)
    subtype: Optional[Subtype] = Field(default=None, kw_only=True)
    preprocess: Optional[bool] = Field(default=True, kw_only=True)

    @root_validator(skip_on_failure=True, allow_reuse=True)
    @classmethod
    def validateDataType(cls, values):
        type, subtype = values.get("type"), values.get("subtype")
        if type.value == "list":
            if subtype.value:
                if subtype.value not in [DataType.FLOAT.value, DataType.INT.value, DataType.STRING.value]:
                    raise ValueError(
                        f"{subtype.value} must be {DataType.FLOAT.value} | {
                            DataType.INT.value} | {DataType.STRING.value}"
                    )
            else:
                raise ValueError("subtype must be given in type List")
        return values

    class Config:
        arbitrary_types_allowed = True


# The code below is executed only when this file is run as a script
if __name__ == "__main__":
    print(HTMLAttributeTypes)
