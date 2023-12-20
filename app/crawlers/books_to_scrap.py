from .abc_spider import ABCSpider


class BooksToScrap(ABCSpider):
    """BooksToScrap _summary_

    Args:
        ABCSpider (_type_): _description_
    """

    async def posprocess_data(self) -> None:
        pass
