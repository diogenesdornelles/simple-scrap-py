""" modulo that contains Olx scrapper
"""
from .abc_spider import ABCSpider


class Olx(ABCSpider):
    """Olx _summary_

    Args:
        ABCSpider (_type_): _description_
    """

    async def posprocess_data(self) -> None:
        pass
