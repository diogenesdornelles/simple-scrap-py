from constants import IMDB_BASE_URL, IMDB_URL
from css_utils import (
    CSSSelectorBuilder,
    CSSSelectorCombinator,
    HTMLTagElement,
)
from task_utils import DataGetter, HTMLAttributeTypes, Task
from task_utils.data_getter import DataType, Subtype
from task_utils.link_getter import LinkGetter

from .models import ColumnsIMDB

html_tag, css_combinator, css_pseudo_selector = (
    CSSSelectorBuilder().html_tag,
    CSSSelectorBuilder().css_combinator,
    CSSSelectorBuilder().css_pseudo_selector,
)


movie_selector = CSSSelectorBuilder()
movie_selector.add_tag(html_tag.DIV)
movie_selector.add_class("sc-e226b0e3-3")
movie_selector.add_combinator(css_combinator.DESCENDANT)
movie_selector.add_tag(html_tag.H1)
movie_selector.add_class("sc-82970163-0")
movie_selector.add_combinator(css_combinator.DESCENDANT)
movie_selector.add_tag(html_tag.SPAN)
movie_selector.add_class("hero__primary-text")

year_selector = CSSSelectorBuilder()
year_selector.add_tag(html_tag.DIV)
year_selector.add_class("sc-e226b0e3-3")
year_selector.add_combinator(css_combinator.DESCENDANT)
year_selector.add_tag(html_tag.UL)
year_selector.add_class("ipc-inline-list")
year_selector.add_combinator(css_combinator.DESCENDANT)
year_selector.add_tag(html_tag.LI)
year_selector.add_class("ipc-inline-list__item")
year_selector.add_pseudo_selector(pseudo_selector=css_pseudo_selector.FIRST_CHILD)
year_selector.add_combinator(css_combinator.DESCENDANT)
year_selector.add_tag(html_tag.A)

director_selector = CSSSelectorBuilder()
director_selector.add_tag(html_tag.SECTION)
director_selector.add_class("sc-69e49b85-4")
director_selector.add_combinator(css_combinator.DESCENDANT)
director_selector.add_tag(html_tag.UL)
director_selector.add_class("ipc-metadata-list")
director_selector.add_combinator(css_combinator.DESCENDANT)
director_selector.add_tag(html_tag.LI)
director_selector.add_class("ipc-metadata-list__item")
director_selector.add_pseudo_selector(pseudo_selector=css_pseudo_selector.FIRST_CHILD)
director_selector.add_combinator(css_combinator.DESCENDANT)
director_selector.add_tag(html_tag.A)

rating_selector = CSSSelectorBuilder()
rating_selector.add_tag(html_tag.DIV)
rating_selector.add_class("sc-e226b0e3-3")
rating_selector.add_combinator(css_combinator.DESCENDANT)
rating_selector.add_tag(html_tag.DIV)
rating_selector.add_class("sc-acdbf0f3-0")
rating_selector.add_combinator(css_combinator.DESCENDANT)
rating_selector.add_tag(html_tag.SPAN)
rating_selector.add_class("sc-bde20123-1")


artists_selector = CSSSelectorBuilder()
artists_selector.add_tag(html_tag.DIV)
artists_selector.add_class("sc-69e49b85-3")
artists_selector.add_combinator(css_combinator.DESCENDANT)
artists_selector.add_pseudo_selector(pseudo_selector=css_pseudo_selector.LAST_CHILD)
artists_selector.add_combinator(css_combinator.CHILD)
artists_selector.add_tag(html_tag.DIV)
artists_selector.add_combinator(css_combinator.CHILD)
artists_selector.add_tag(html_tag.UL)
artists_selector.add_combinator(css_combinator.CHILD)
artists_selector.add_tag(html_tag.LI)
artists_selector.add_combinator(css_combinator.DESCENDANT)
artists_selector.add_tag(html_tag.A)


sinopsis_selector = CSSSelectorBuilder()
sinopsis_selector.add_tag(html_tag.SECTION)
sinopsis_selector.add_class("sc-69e49b85-4")
sinopsis_selector.add_combinator(css_combinator.DESCENDANT)
sinopsis_selector.add_tag(html_tag.P)
sinopsis_selector.add_class("sc-466bb6c-3")
sinopsis_selector.add_combinator(css_combinator.DESCENDANT)
sinopsis_selector.add_tag(html_tag.SPAN)
sinopsis_selector.add_class("sc-466bb6c-1")


data_getters = [
    DataGetter(
        selector=movie_selector, name=ColumnsIMDB.MOVIE, attr=HTMLAttributeTypes.TEXT_CONTENT, type=DataType.STRING
    ),
    DataGetter(selector=year_selector, name=ColumnsIMDB.YEAR, attr=HTMLAttributeTypes.TEXT_CONTENT, type=DataType.INT),
    DataGetter(
        selector=director_selector,
        name=ColumnsIMDB.DIRECTOR,
        attr=HTMLAttributeTypes.TEXT_CONTENT,
        type=DataType.LIST,
        subtype=Subtype.STRING,
    ),
    DataGetter(
        selector=rating_selector, name=ColumnsIMDB.RATING, attr=HTMLAttributeTypes.TEXT_CONTENT, type=DataType.FLOAT
    ),
    DataGetter(
        selector=artists_selector,
        name=ColumnsIMDB.ARTISTS,
        attr=HTMLAttributeTypes.TEXT_CONTENT,
        type=DataType.LIST,
        subtype=Subtype.STRING,
    ),
    DataGetter(
        selector=sinopsis_selector,
        name=ColumnsIMDB.SINOPSIS,
        attr=HTMLAttributeTypes.TEXT_CONTENT,
        type=DataType.STRING,
    ),
]

selector_url = (
    CSSSelectorBuilder()
    .add_tag(HTMLTagElement.DIV)
    .add_class("sc-479faa3c-0")
    .add_combinator(CSSSelectorCombinator.DESCENDANT)
    .add_tag(HTMLTagElement.A)
    .add_class("ipc-title-link-wrapper")
)

link_getters = LinkGetter(selector=selector_url, type="href", get_previous=True)

imdb_tasks = Task(
    name="imdb", base_url=IMDB_BASE_URL, url=IMDB_URL, data_getters=data_getters, link_getter=link_getters, pages=2
)

if __name__ == "__main__":
    print(imdb_tasks)
