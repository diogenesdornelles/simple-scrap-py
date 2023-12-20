from abc import ABC, abstractmethod
from typing import Dict, List

from bs4 import ResultSet, Tag
from css_utils.css_selector_builder import CSSSelectorBuilder
from extract import Extract
from task_utils import DataGetter, DataType, LinkGetter, Task
from task_utils.column import Column
from task_utils.html_attribute_types import HTMLAttributeTypes
from utils import get_base_url, logger

from .downloader_middleware import DownloaderMiddleware
from .models import CrawlRawResult, CrawlResult
from .pipelines import Pipelines


class ABCSpider(ABC):
    """Abstract base class defining the structure for creating spiders to crawl data.

    ABCSpider serves as an abstract base class (ABC) providing a structure for creating spider classes
    used for web crawling tasks.

    Attributes:
        _name (str): The name of the spider.
        _data_getters (List[DataGetter]): List of data getters used to extract specific data from the web page.
        _link_getter (LinkGetter | None): Getter for extracting links (default is None).
        _raw_results (CrawlRawResult): Dictionary containing raw crawl results.
        _results (CrawlResult): Dictionary containing refined crawl results.
        __pages (int): Number of pages to crawl (default is 1).
        __links (List[str]): List of URLs to be crawled.
        _pipelines (Pipelines): Pipelines object for data preprocessing.
        __downloader_middleware (DownloaderMiddleware): Middleware for handling downloads.
    """

    def __init__(self, task: Task):
        """Initialize ABCSpider with the provided TaskProtocol object."""
        self._name: str = task.name
        self._data_getters: List[DataGetter] = task.data_getters
        self._link_getter: LinkGetter | None = task.link_getter
        self._raw_results: CrawlRawResult = {}
        self._results: CrawlResult = {}
        self.__pages: int = task.pages if task.pages else 1
        self.__links: List[str] = []
        self._pipelines: Pipelines = Pipelines(self._raw_results, task)
        self.__downloader_middleware: DownloaderMiddleware = DownloaderMiddleware(task)

    @property
    def name(self) -> str:
        """name: Property to retrieve the name of the spider.

        Returns:
            str: name of the spider
        """
        return self._name

    @property
    def results(self) -> CrawlResult:
        """results: Property to retrieve the refined crawl results.

        Returns:
            CrawlResult: the refined result
        """
        return self._results

    async def _extract_data(
        self, selector: CSSSelectorBuilder, attr: HTMLAttributeTypes, name: Column | str, data_type: DataType
    ) -> CrawlRawResult | Dict[str, List]:
        """
        Extracts data from HTML based on the provided selector and attributes.

        Args:
            selector (CSSSelectorBuilder): CSS selector to identify HTML elements.
            attr (HTMLAttributeTypes): HTML attribute type.
            name (Union[Column, str]): Column name or string.
            data_type (DataType): Type of data to extract.

        Returns:
            Union[CrawlRawResult, Dict[str, List]]: Extracted data as a dictionary or CrawlRawResult.
        """
        tags: ResultSet[Tag] = self.__downloader_middleware.soup.select(selector.to_str())
        if len(tags) > 0:
            result = Extract.data(tags, attr.value)
            logger.debug(
                "Name: %s. Extracted data:\n %s. Length: %s",
                name.value if isinstance(name, Column) else name,
                result,
                len(result),
            )
            if data_type.value == "list":
                return {f"{name.value if isinstance(name, Column) else name}": [result]}

            else:
                return {f"{name.value if isinstance(name, Column) else name}": result}
        else:
            logger.warning("No data found: %s", name.value if isinstance(name, Column) else name)
            return {f"{name.value if isinstance(name, Column) else name}": []}

    async def _get_data(self) -> None:
        """Obtains data from the web page."""
        for getter in self._data_getters:
            result = await self._extract_data(getter.selector, getter.attr, getter.name, getter.type)
            if getter.name.value not in self._raw_results:
                self._raw_results.update(result)
            else:
                self._raw_results[getter.name.value] = self._raw_results[getter.name.value] + result[getter.name.value]

    async def _get_links(self) -> None:
        """Obtains links from the web page."""
        if isinstance(self._link_getter, LinkGetter):
            result = await self._extract_data(
                self._link_getter.selector, HTMLAttributeTypes.HREF, "url", DataType.STRING
            )
            self.__links = result["url"]
        else:
            raise TypeError(f"{self._link_getter} must be a Type <LinkGetter>")

    async def _run_previous(self):
        """Runs tasks based on previous links."""
        await self._run_link_getter()
        if len(self.__links) > 1:
            new_base_url = get_base_url(self.__links[0], self.__links[1])
            if new_base_url:
                self.__downloader_middleware.base_url = new_base_url
            for link in self.__links:
                self.__downloader_middleware.url = link
                if self.__pages > 0:
                    await self._run_data_getter()
                    self.__pages -= 1
                else:
                    break
        elif len(self.__links) == 1:
            if self.__links[0].find(self.__downloader_middleware.base_url) == 0:
                self.__downloader_middleware.base_url = ""
            self.__downloader_middleware.url = self.__links[0]
            await self._run_data_getter()
        else:
            self._raw_results = {f"{self._name}": []}

    async def _run_after(self):
        """Runs tasks after obtaining links."""
        self.__pages -= 1
        await self._run_data_getter()
        while self.__pages > 0:
            await self._get_links()
            if len(self.__links) > 0:
                if self.__links[0].find(self.__downloader_middleware.base_url) == 0:
                    self.__downloader_middleware.base_url = ""
                self.__downloader_middleware.url = self.__links[0]
                await self._run_data_getter()
            self.__pages -= 1

    async def _run_data_getter(self):
        """Runs data getter to obtain data."""
        await self.__downloader_middleware.get_soup()
        await self._get_data()

    async def _run_link_getter(self):
        """Runs link getter to obtain links."""
        await self.__downloader_middleware.get_soup()
        await self._get_links()

    async def crawl(self) -> None:
        """Starts the crawling process."""
        if isinstance(self._link_getter, LinkGetter):
            if self._link_getter.get_previous:
                await self._run_previous()
            else:
                await self._run_after()
        else:
            await self._run_data_getter()
        self._pipelines.__data = self._raw_results
        await self._pipelines.preprocess_data()
        self._results = self._pipelines._results

    @abstractmethod
    async def posprocess_data(self) -> None:
        """preprocess_data: Performs post-processing of the crawled data.

        Raises:
            NotImplementedError: NotImplementedError
        """
        raise NotImplementedError
