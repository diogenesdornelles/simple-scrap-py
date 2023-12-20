from typing import Protocol
from crawlers.models import CrawlResult


class TaskProtocol(Protocol):
    """Protocol defining the interface for a generic task.

    TaskProtocol defines the methods and properties expected in a task class. It serves as a protocol
    specifying the structure that task-related classes should adhere to.

    Attributes:
        name (str): The name property representing the task name.
        results (CrawlResult): The results property representing the crawl results.
    """

    @property
    def name(self) -> str:
        """Property: Represents the name of the task."""
        raise NotImplementedError

    @property
    def results(self) -> CrawlResult:
        """Property: Represents the crawl results."""
        raise NotImplementedError

    async def crawl(self) -> None:
        """Method: Perform the crawling process."""
        raise NotImplementedError

    async def posprocess_data(self) -> None:
        """Method: Perform post-processing on the crawled data."""
        raise NotImplementedError
