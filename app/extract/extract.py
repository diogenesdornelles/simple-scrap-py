from typing import List

from bs4 import ResultSet, Tag
from task_utils import HTMLAttributeTypes


class Extract:
    """ Class for extracting data from an HTML

    Returns:
        _type_:
    """
    @staticmethod
    def data(tags: ResultSet[Tag], arg: str) -> List[str]:
        """data _summary_

        Args:
            tags (ResultSet[Tag]): BS4 tags to extract
            arg (str): type of data to extract

        Returns:
            List[str]: A list of strings
        """
        if arg == HTMLAttributeTypes.TEXT_CONTENT.value:
            return Extract.extract_text(tags)
        return [tag.get(arg) for tag in tags if isinstance(tag.get(arg), str)]  # type: ignore

    @staticmethod
    def extract_text(tags: ResultSet[Tag]) -> List[str]:
        """extract_text: extract text content

        Args:
            tags (ResultSet[Tag]): BS4 tags to extract

        Returns:
            List[str]: A list of strings
        """
        return [tag.text for tag in tags if isinstance(tag.text, str)]
