""" modulo that contains IMDB scrapper
"""
from tasks.models import ColumnsIMDB

from .abc_spider import ABCSpider


class IMDB(ABCSpider):
    """Concrete class for spidering IMDB website

    Args:
        ABCSpider (_type_):
    Properties:
        task (Task): The Pydantic's task model to initialize the spider
    """

    async def posprocess_data(self) -> None:
        """preprocess_data _summary_"""
        if ColumnsIMDB.MOVIE.value in self._results:
            self._results[ColumnsIMDB.RANKING.value] = [
                index + 1 for index, _ in enumerate(self._results[ColumnsIMDB.MOVIE.value])
            ]
