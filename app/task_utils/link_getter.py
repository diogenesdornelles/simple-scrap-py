from typing import Literal, Optional
from css_utils import CSSSelectorBuilder, HTMLTagElement
from pydantic import BaseModel, Field


class LinkGetter(BaseModel):
    """Model representing a getter for extracting links from HTML content.

    This model defines attributes necessary for retrieving links, such as the CSS selector,
    the type of link to extract (e.g., 'href'), and an optional flag to get the previous link.

    Args:
        BaseModel (type): Base Pydantic model for defining attributes.

    Attributes:
        selector (CSSSelectorBuilder): CSS selector for locating HTML elements containing links.
        type (Literal["href"]): Type of link to extract (default value is "href").
        get_previous (Optional[bool]): Flag indicating whether to retrieve the previous link (default is False).

    """

    selector: CSSSelectorBuilder = Field(..., kw_only=True)
    type: Literal["href"] = Field(default="href", kw_only=True)
    get_previous: Optional[bool] = Field(default=False, kw_only=True)

    class Config:
        arbitrary_types_allowed = True

    def to_dict(self) -> dict[str, Literal["href"] | str | bool | None]:
        """Converts LinkGetter object to a dictionary representation.

        Returns:
            dict: A dictionary containing selector, type, and get_previous attributes.
        """
        return {"selector": self.selector.to_str(), "type": self.type, "pre": self.get_previous}


if __name__ == "__main__":
    # Example usage of LinkGetter class
    a = LinkGetter(
        selector=CSSSelectorBuilder().add_tag(HTMLTagElement.UL),
        type="href",
    )
    print(a.to_dict())
