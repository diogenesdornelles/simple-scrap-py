from typing import Any, Dict, Union

from pydantic import BaseModel, root_validator

from .css_selector_combinator import CSSSelectorCombinator
from .css_selector_pseudo_element import CSSSelectorPseudoElement
from .empty_str import EmptyStr
from .html_element_attribute import HTMLElementAttribute
from .html_input_type import HTMLInputType
from .html_tag_element import HTMLTagElement

TAllowedNameTagsFor = Dict[str, list[str]]

ALLOWED_NAME_TAGS_FOR: TAllowedNameTagsFor = {
    "name": [
        HTMLTagElement.A.value,
        HTMLTagElement.ABBR.value,
        HTMLTagElement.AREA.value,
        HTMLTagElement.AUDIO.value,
        HTMLTagElement.BUTTON.value,
        HTMLTagElement.CANVAS.value,
        HTMLTagElement.DATALIST.value,
        HTMLTagElement.DIALOG.value,
        HTMLTagElement.DIV.value,
        HTMLTagElement.DL.value,
        HTMLTagElement.DT.value,
        HTMLTagElement.EM.value,
        HTMLTagElement.FIELDSET.value,
        HTMLTagElement.FORM.value,
        HTMLTagElement.H1.value,
        HTMLTagElement.H2.value,
        HTMLTagElement.H3.value,
        HTMLTagElement.H4.value,
        HTMLTagElement.H5.value,
        HTMLTagElement.H6.value,
        HTMLTagElement.IFRAME.value,
        HTMLTagElement.IMG.value,
        HTMLTagElement.INPUT.value,
        HTMLTagElement.LABEL.value,
        HTMLTagElement.LEGEND.value,
        HTMLTagElement.LI.value,
        HTMLTagElement.LINK.value,
        HTMLTagElement.MAP.value,
        HTMLTagElement.MENU.value,
        HTMLTagElement.META.value,
        HTMLTagElement.METER.value,
        HTMLTagElement.NAV.value,
        HTMLTagElement.OBJECT.value,
        HTMLTagElement.OL.value,
        HTMLTagElement.OPTGROUP.value,
        HTMLTagElement.OPTION.value,
        HTMLTagElement.OUTPUT.value,
        HTMLTagElement.P.value,
        HTMLTagElement.PARAM.value,
        HTMLTagElement.PRE.value,
        HTMLTagElement.PROGRESS.value,
        HTMLTagElement.Q.value,
        HTMLTagElement.RUBY.value,
        HTMLTagElement.S.value,
        HTMLTagElement.SAMP.value,
        HTMLTagElement.SCRIPT.value,
        HTMLTagElement.SELECT.value,
        HTMLTagElement.SMALL.value,
        HTMLTagElement.SPAN.value,
        HTMLTagElement.STRONG.value,
        HTMLTagElement.STYLE.value,
        HTMLTagElement.SUB.value,
        HTMLTagElement.SUMMARY.value,
        HTMLTagElement.TABLE.value,
        HTMLTagElement.TBODY.value,
        HTMLTagElement.TD.value,
        HTMLTagElement.TEXTAREA.value,
        HTMLTagElement.TFOOT.value,
        HTMLTagElement.TH.value,
        HTMLTagElement.THEAD.value,
        HTMLTagElement.TIME.value,
        HTMLTagElement.TITLE.value,
        HTMLTagElement.TR.value,
        HTMLTagElement.U.value,
        HTMLTagElement.UL.value,
        HTMLTagElement.VAR.value,
        HTMLTagElement.VIDEO.value,
    ],
    "value": [
        HTMLTagElement.INPUT.value,
        HTMLTagElement.OPTION.value,
        HTMLTagElement.TEXTAREA.value,
        HTMLTagElement.BUTTON.value,
        HTMLTagElement.METER.value,
        HTMLTagElement.PROGRESS.value,
        HTMLTagElement.PARAM.value,
    ],
    "content": [
        HTMLTagElement.META.value,
        HTMLTagElement.STYLE.value,
        HTMLTagElement.LINK.value,
        HTMLTagElement.SCRIPT.value,
    ],
    "charset": [HTMLTagElement.META.value, HTMLTagElement.HTML.value],
    "alt": [
        HTMLTagElement.INPUT.value,
        HTMLTagElement.IMG.value,
        HTMLTagElement.AREA.value,
        HTMLTagElement.VIDEO.value,
        HTMLTagElement.OBJECT.value,
    ],
    "src": [
        HTMLTagElement.IMG.value,
        HTMLTagElement.AUDIO.value,
        HTMLTagElement.VIDEO.value,
        HTMLTagElement.PICTURE.value,
        HTMLTagElement.SOURCE.value,
    ],
    "href": [HTMLTagElement.A.value],
    "placeholder": [HTMLTagElement.INPUT.value, HTMLTagElement.TEXTAREA.value],
    "type": [
        HTMLTagElement.INPUT.value,
        HTMLTagElement.BUTTON.value,
        HTMLTagElement.TEXTAREA.value,
        HTMLTagElement.SELECT.value,
        HTMLTagElement.DATALIST.value,
        HTMLTagElement.OPTION.value,
        HTMLTagElement.METER.value,
        HTMLTagElement.PROGRESS.value,
        HTMLTagElement.OUTPUT.value,
        HTMLTagElement.SOURCE.value,
        HTMLTagElement.TRACK.value,
    ],
}


class CSSAttrValidator(BaseModel):
    """CSSAttrValidator Pydantic Validation to CSSAttr

    Args:
        BaseModel (_type_): Pydantic BaseModel
    """

    data: str | EmptyStr = ""
    tag: HTMLTagElement | EmptyStr = ""
    attr: HTMLElementAttribute | EmptyStr = ""
    combinator: CSSSelectorCombinator | EmptyStr = ""
    pseudo_element: CSSSelectorPseudoElement | EmptyStr = ""
    custom: str | EmptyStr = ""

    @root_validator(skip_on_failure=True, allow_reuse=True)
    def validate_tag_attr(cls, values: Dict[str, str]) -> Union[Dict[str, str], Any]:
        """validate_tag_attr method to validate attributes on HTML elements

        Args:
            values (Dict[str, str]): properties to validate

        Raises:
            ValueError: attribute given cant be used with some tag
            ValueError: attribute value not present in Enum HTMLInputType
            ValueError: attribute must have a custom property

        Returns:
            Union[Dict[str, str], Any]: properties validated
        """
        tag, attr, data, custom = values.get("tag"), values.get("attr"), values.get("data"), values.get("custom")
        if isinstance(tag, HTMLTagElement) and isinstance(attr, HTMLElementAttribute):
            if tag.value not in ALLOWED_NAME_TAGS_FOR[attr.value]:
                raise ValueError(f"{attr.value} attribute cant be used with tag {tag.value}")
        if isinstance(attr, HTMLElementAttribute):
            if attr.value == HTMLElementAttribute.TYPE.value:
                if data not in [HTMLInputType[value.name] for value in HTMLInputType]:
                    raise ValueError(f"{attr.value} value not present in {HTMLInputType.name} Enum class: given {data}")
            if attr.value == HTMLElementAttribute.DATA.value and isinstance(custom, str) and len(custom) < 1:
                raise ValueError(f"{attr.value} must have a custom property: {attr.value}<property>")
        return values

    class Config:
        arbitrary_types_allowed = True


if __name__ == "__main__":
    v = CSSAttrValidator(
        data="ola",
        tag=HTMLTagElement.INPUT,
        attr=HTMLElementAttribute.TYPE,
        combinator="",
        pseudo_element="",
    )
