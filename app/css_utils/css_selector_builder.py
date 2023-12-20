from .css_attr_validator import CSSAttrValidator
from .css_pseudo_selector_validator import CSSPseudoSelectorValidator
from .css_selector_combinator import CSSSelectorCombinator
from .css_selector_pseudo_element import CSSSelectorPseudoElement
from .css_selector_pseudo_selector import CSSSelectorPseudoSelector
from .empty_str import EmptyStr
from .html_element_attribute import (
    HTMLElementAttribute,
    HTMLElementClassAttribute,
    HTMLElementIdAttribute,
)
from .html_input_type import HTMLInputType
from .html_tag_element import HTMLTagElement


class CSSSelectorBuilder:
    """CSSSelectorBuilder: A class to construct CSS Selectors for performing queries."""

    def __init__(self) -> None:
        """Initialize a CSSSelectorBuilder object.

        Properties:
            selector = ""  # Private attribute for storing the constructed CSS Selector
            html_tag = HTMLTagElement  # Attribute for HTML tag elements
            html_attribute = HTMLElementAttribute  # Attribute for HTML element attributes
            css_combinator = CSSSelectorCombinator  # Attribute for CSS combinators
            css_pseudo_element = CSSSelectorPseudoElement  # Attribute for CSS pseudo-elements
            css_pseudo_selector = CSSSelectorPseudoSelector  # Attribute for CSS pseudo-selectors
            css_id = HTMLElementIdAttribute  # Attribute for HTML element IDs
            css_class = HTMLElementClassAttribute  # Attribute for HTML element classes
            html_input_type = HTMLInputType  # Attribute for HTML input types

        Summary:
            Initializes a CSSSelectorBuilder object with attributes for constructing CSS Selectors.
        """
        self.__selector = ""
        self.html_tag = HTMLTagElement
        self.html_attribute = HTMLElementAttribute
        self.css_combinator = CSSSelectorCombinator
        self.css_pseudo_element = CSSSelectorPseudoElement
        self.css_pseudo_selector = CSSSelectorPseudoSelector
        self.css_id = HTMLElementIdAttribute
        self.css_class = HTMLElementClassAttribute
        self.html_input_type = HTMLInputType

    @property
    def selector(self) -> str:
        """selector: return a property selector

        Returns:
            str: a property selector string
        """
        return self.__selector

    def add_tag(self, tag: HTMLTagElement) -> "CSSSelectorBuilder":
        """tag: add html tag to CSSSelectorBuilder

        Args:
            tag (HTMLTagElement): HTMLTagElement Enum

        Returns:
            CSSSelectorBuilder: CSSSelectorBuilder instance
        """
        self.__selector += f"{tag.value}"
        return self

    def add_attr(
        self,
        *,
        value: str | EmptyStr = "",
        tag: HTMLTagElement | EmptyStr = "",
        attr: HTMLElementAttribute | EmptyStr = "",
        combinator: CSSSelectorCombinator | EmptyStr = "",
        pseudo_element: CSSSelectorPseudoElement | EmptyStr = "",
        custom: str | EmptyStr = "",
    ) -> "CSSSelectorBuilder":
        """add_attr: add html attribute to CSSSelectorBuilder

        Args:
            value (str | EmptyStr, optional): expression value. Defaults to "".
            tag (HTMLTagElement | EmptyStr, optional): HTMLTagElement Enum. Defaults to "".
            attr (HTMLElementAttribute | EmptyStr, optional): HTMLElementAttribute Enum. Defaults to "".
            combinator (CSSSelectorCombinator | EmptyStr, optional): CSSSelectorCombinator Enum. Defaults to "".
            pseudo_element (CSSSelectorPseudoElement | EmptyStr, optional): CSSSelectorPseudoElement Enum.
            Defaults to "".
            custom (str | EmptyStr, optional): A custom attribute html. Defaults to "".

        Returns:
            CSSSelectorBuilder: CSSSelectorBuilder instance
        """
        CSSAttrValidator(
            data=value, tag=tag, attr=attr, combinator=combinator, pseudo_element=pseudo_element, custom=custom
        )
        if isinstance(tag, HTMLTagElement):
            self.__selector += f"{tag.value}"
        if isinstance(attr, HTMLElementAttribute):
            if attr.value == HTMLElementAttribute.DATA.value:
                self.__selector += f"[{attr.value}{custom}"
            else:
                self.__selector += f"[{attr.value}"
        if isinstance(combinator, CSSSelectorCombinator):
            self.__selector += f"{combinator.value}"
        self.__selector += f"='{value}']"
        if isinstance(pseudo_element, CSSSelectorPseudoElement):
            self.__selector += f"{pseudo_element.value}"
        return self

    def add_combinator(self, combinator: CSSSelectorCombinator) -> "CSSSelectorBuilder":
        """combinator: add css combinator to CSSSelectorBuilder

        Args:
            combinator (CSSSelectorCombinator): CSSSelectorCombinator Enum

        Returns:
            CSSSelectorBuilder: CSSSelectorBuilder instance
        """
        self.__selector += f"{combinator.value}"
        return self

    def add_pseudo_element(self, pseudo_element: CSSSelectorPseudoElement) -> "CSSSelectorBuilder":
        """pseudo_element: add css pseudo element to CSSSelectorBuilder

        Args:
            pseudo_element (CSSSelectorPseudoElement): CSSSelectorPseudoElement Enum

        Returns:
            CSSSelectorBuilder: CSSSelectorBuilder instance
        """
        self.__selector += f"{pseudo_element.value}"
        return self

    def add_pseudo_selector(
        self, *, pseudo_selector: CSSSelectorPseudoSelector, expression: str = ""
    ) -> "CSSSelectorBuilder":
        """add_pseudo_selector: add css pseudo selector to CSSSelectorBuilder

        Args:
            pseudo_selector (CSSSelectorPseudoSelector): CSSSelectorPseudoSelector Enum
            expression (str, optional): expression. Defaults to "".

        Returns:
            CSSSelectorBuilder: CSSSelectorBuilder instance
        """
        CSSPseudoSelectorValidator(expression=expression, pseudo_selector=pseudo_selector)
        if len(expression) > 0:
            expression = f"({expression})"
        self.__selector += f"{pseudo_selector.value}{expression}"
        return self

    def add_id(self, value: str) -> "CSSSelectorBuilder":
        """add_id: add html id attr to CSSSelectorBuilder

        Args:
            value (str): expression value

        Returns:
            CSSSelectorBuilder: CSSSelectorBuilder instance
        """
        self.__selector += f"{HTMLElementIdAttribute.ID.value}{value}"
        return self

    def add_class(self, value: str) -> "CSSSelectorBuilder":
        """add_class: add html class attr to CSSSelectorBuilder

        Args:
            value (str): expression value

        Returns:
            CSSSelectorBuilder: CSSSelectorBuilder instance
        """
        self.__selector += f"{HTMLElementClassAttribute.CLASS.value}{value}"
        return self

    def to_str(self) -> str:
        """to_str: return selector string representation

        Returns:
            str: selector string representation
        """
        return self.__selector.strip()


if __name__ == "__main__":
    selector: CSSSelectorBuilder = CSSSelectorBuilder()
    selector.add_attr(value="title", tag=HTMLTagElement.DIV, attr=HTMLElementAttribute.HREF)
