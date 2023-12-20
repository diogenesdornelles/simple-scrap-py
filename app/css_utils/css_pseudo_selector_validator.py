from math import e
from typing import Any, Dict

from pydantic import BaseModel, root_validator

from .css_selector_pseudo_selector import CSSSelectorPseudoSelector
from .empty_str import EmptyStr

HAS_PARAM: list[str] = [
    CSSSelectorPseudoSelector.NTH_CHILD.value,
    CSSSelectorPseudoSelector.NOT.value,
    CSSSelectorPseudoSelector.FIRST_OF_TYPE.value,
    CSSSelectorPseudoSelector.LANG.value,
    CSSSelectorPseudoSelector.HAS.value,
    CSSSelectorPseudoSelector.NTH_LAST_OF_TYPE.value,
    CSSSelectorPseudoSelector.DIR.value,
    CSSSelectorPseudoSelector.IS.value,
    CSSSelectorPseudoSelector.NTH_LAST_CHILD.value,
    CSSSelectorPseudoSelector.NTH_OF_TYPE.value,
    CSSSelectorPseudoSelector.WHERE.value,
]


class CSSPseudoSelectorValidator(BaseModel):
    """Represents a Pydantic model for validating CSS pseudo selectors.

    Args:
        BaseModel (type): Pydantic's BaseModel for data validation and serialization.

    Raises:
        ValueError: Raised when the provided expression is invalid.
        ValueError: Raised when the provided pseudo_selector is invalid.

    Returns:
        Union[str, EmptyStr]: A string representing the CSS pseudo selector expression,
        or an empty string if not provided.
    """
    expression: str | EmptyStr = ""
    pseudo_selector: CSSSelectorPseudoSelector | EmptyStr = ""

    @root_validator(skip_on_failure=True, allow_reuse=True)
    def validate_fields(cls, values: Dict[str, str]) -> Dict[str, str] | Any:
        """validate_fields: validate fields from CSSPseudoSelector

        Args:
            values (Dict[str, str]): properties

        Raises:
            ValueError: An expression that must be given
            ValueError: An expression that can't be given

        Returns:
            Dict[str, str] | Any: validated properties
        """
        expression, pseudo_selector = values.get("expression"), values.get("pseudo_selector")
        if isinstance(pseudo_selector, CSSSelectorPseudoSelector) and expression:
            if len(expression) > 0:
                if pseudo_selector.value in HAS_PARAM:
                    return values
                raise ValueError(f"An expression must be given to {pseudo_selector.value}")
            if pseudo_selector.value not in HAS_PARAM:
                return values
            raise ValueError(f"An expression can't be given to {pseudo_selector.value}")
        return values

    class Config:
        arbitrary_types_allowed = True


if __name__ == "__main__":
    v = CSSPseudoSelectorValidator(
        expression="ola",
        pseudo_selector="",
    )
