from constants import BOOKS_TO_SCRAP_BASE_URL, BOOKS_TO_SCRAP_URL
from css_utils import CSSSelectorBuilder, CSSSelectorCombinator, HTMLTagElement
from task_utils import DataGetter, DataType, HTMLAttributeTypes, LinkGetter, Task

from .models import ColumnsBooksToScrap

selector1 = (
    CSSSelectorBuilder()
    .add_class("row")
    .add_combinator(CSSSelectorCombinator.DESCENDANT)
    .add_class("product_pod")
    .add_combinator(CSSSelectorCombinator.DESCENDANT)
    .add_tag(HTMLTagElement.H3)
    .add_combinator(CSSSelectorCombinator.DESCENDANT)
    .add_tag(HTMLTagElement.A)
)

selector2 = (
    CSSSelectorBuilder()
    .add_class("row")
    .add_combinator(CSSSelectorCombinator.DESCENDANT)
    .add_class("product_pod")
    .add_combinator(CSSSelectorCombinator.DESCENDANT)
    .add_class("price_color")
)

data_getters = [
    DataGetter(
        name=ColumnsBooksToScrap.LINK, selector=selector1, attr=HTMLAttributeTypes.HREF, type=DataType.STRING
    ),
    DataGetter(
        name=ColumnsBooksToScrap.PRICE,
        selector=selector2,
        attr=HTMLAttributeTypes.TEXT_CONTENT,
        type=DataType.FLOAT,
    ),
    DataGetter(
        name=ColumnsBooksToScrap.TITLE, selector=selector1, attr=HTMLAttributeTypes.TITLE, type=DataType.STRING
    ),
]

selector3 = (
    CSSSelectorBuilder()
    .add_tag(HTMLTagElement.UL)
    .add_class("pager")
    .add_combinator(CSSSelectorCombinator.DESCENDANT)
    .add_tag(HTMLTagElement.LI)
    .add_class("next")
    .add_combinator(CSSSelectorCombinator.DESCENDANT)
    .add_tag(HTMLTagElement.A)
)


link_getters = LinkGetter(selector=selector3, type="href", get_previous=False)

books_to_scrap_tasks = Task(
    name="books_to_scrap",
    base_url=BOOKS_TO_SCRAP_BASE_URL,
    url=BOOKS_TO_SCRAP_URL,
    data_getters=data_getters,
    link_getter=link_getters,
    pages=1,
)
