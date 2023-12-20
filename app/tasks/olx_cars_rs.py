from constants import OLX_CARS_RS_BASE_URL, OLX_CARS_RS_URL
from css_utils import (
    CSSSelectorBuilder,
    CSSSelectorCombinator,
    HTMLElementAttribute,
    HTMLTagElement,
)
from task_utils import DataGetter, HTMLAttributeTypes, LinkGetter, Task
from task_utils.data_getter import DataType

from .models import ColumnsOlx

selector1 = (
    CSSSelectorBuilder()
    .add_tag(HTMLTagElement.DIV)
    .add_id("content")
    .add_combinator(CSSSelectorCombinator.DESCENDANT)
    .add_tag(HTMLTagElement.DIV)
    .add_class("ad__sc-h3us20-4")
    .add_combinator(CSSSelectorCombinator.DESCENDANT)
    .add_tag(HTMLTagElement.H1)
    .add_class("ad__sc-45jt43-0")
)

selector2 = (
    CSSSelectorBuilder()
    .add_tag(HTMLTagElement.DIV)
    .add_id("content")
    .add_combinator(CSSSelectorCombinator.DESCENDANT)
    .add_tag(HTMLTagElement.DIV)
    .add_class("ad__sc-h3us20-4")
    .add_combinator(CSSSelectorCombinator.DESCENDANT)
    .add_tag(HTMLTagElement.H2)
    .add_class("ad__sc-1leoitd-0")
)

selector3 = (
    CSSSelectorBuilder()
    .add_tag(HTMLTagElement.DIV)
    .add_id("content")
    .add_combinator(CSSSelectorCombinator.DESCENDANT)
    .add_tag(HTMLTagElement.DIV)
    .add_class("ad__sc-h3us20-4")
    .add_combinator(CSSSelectorCombinator.DESCENDANT)
    .add_tag(HTMLTagElement.SPAN)
    .add_class("ad__sc-1sj3nln-1")
)

data_getters = [
    DataGetter(selector=selector1, name=ColumnsOlx.NAME,
               attr=HTMLAttributeTypes.TEXT_CONTENT, type=DataType.STRING),
    DataGetter(selector=selector2, name=ColumnsOlx.PRICE,
               attr=HTMLAttributeTypes.TEXT_CONTENT, type=DataType.FLOAT),
    DataGetter(
        selector=selector3, name=ColumnsOlx.DESCRIPTION, attr=HTMLAttributeTypes.TEXT_CONTENT, type=DataType.STRING
    ),
]

selector4 = (
    CSSSelectorBuilder()
    .add_tag(HTMLTagElement.DIV)
    .add_id("__next")
    .add_combinator(CSSSelectorCombinator.DESCENDANT)
    .add_tag(HTMLTagElement.MAIN)
    .add_id("main")
    .add_combinator(CSSSelectorCombinator.DESCENDANT)
    .add_tag(HTMLTagElement.DIV)
    .add_class("sc-7f8e2e8f-0")
    .add_combinator(CSSSelectorCombinator.DESCENDANT)
    .add_tag(HTMLTagElement.UL)
    .add_attr(attr=HTMLElementAttribute.DATA, custom="testid", value="card-list")
    .add_combinator(CSSSelectorCombinator.DESCENDANT)
    .add_tag(HTMLTagElement.SECTION)
    .add_combinator(CSSSelectorCombinator.CHILD)
    .add_tag(HTMLTagElement.A)
)

link_getters = LinkGetter(selector=selector4, type="href", get_previous=True)

olx_cars_rs_task = Task(
    name="olx_cars_rs",
    base_url=OLX_CARS_RS_BASE_URL,
    url=OLX_CARS_RS_URL,
    data_getters=data_getters,
    link_getter=link_getters,
    pages=8,
)

if __name__ == "__main__":
    print(olx_cars_rs_task)
