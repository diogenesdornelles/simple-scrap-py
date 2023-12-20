from abc import ABC, abstractmethod

from crawlers.models import CrawlResult


class ISaveHandler(ABC):
    """ISaveHandler _summary_

    Args:
        ABC (_type_): _description_

    Raises:
        NotImplementedError: _description_
        NotImplementedError: _description_
        NotImplementedError: _description_
        NotImplementedError: _description_
    """

    @abstractmethod
    def __init__(self, name: str, data: CrawlResult, target_dir: str):
        """__init__ _summary_

        Args:
            name (str): _description_
            data (CrawlResult): _description_
            target_dir (str): _description_

        Raises:
            NotImplementedError: _description_
        """
        raise NotImplementedError

    @abstractmethod
    def to_df(self) -> None:
        """to_df _summary_

        Raises:
            NotImplementedError: _description_
        """
        raise NotImplementedError

    @abstractmethod
    def to_json(self) -> None:
        """to_json _summary_

        Raises:
            NotImplementedError: _description_
        """
        raise NotImplementedError

    @abstractmethod
    def to_mysql(self) -> None:
        """to_mysql _summary_

        Raises:
            NotImplementedError: _description_
        """
        raise NotImplementedError
