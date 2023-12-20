from bs4 import BeautifulSoup
from constants import HEADERS, PARSER
from httpx import AsyncClient, HTTPError
from task_utils.task import Task
from utils import logger


class DownloaderMiddleware:
    """Middleware class for downloading content from URLs and extracting BeautifulSoup objects.

    This class provides methods to asynchronously download content from URLs and parse HTML content
    to create BeautifulSoup objects for further processing.

    Attributes:
        __base_url (str): The base URL used for constructing absolute URLs.
        __url (str): The URL to download content from.
        __timeout (int): The timeout value for HTTP requests in seconds.
        __soup (BeautifulSoup): BeautifulSoup object representing parsed HTML content.

    """

    def __init__(self, task: Task):
        """Initialize DownloaderMiddleware instance.

        Args:
            task (Task): The task object containing URL information.

        """
        self.__base_url: str = task.base_url
        self.__url: str = task.url
        self.__timeout: int = 5
        self.__soup: BeautifulSoup

    @property
    def soup(self) -> BeautifulSoup:
        """BeautifulSoup: The parsed HTML content as a BeautifulSoup object."""
        return self.__soup

    @property
    def url(self) -> str:
        """str: The URL being downloaded."""
        return self.__url

    @url.setter
    def url(self, value: str) -> None:
        """Set the URL to download.

        Args:
            value (str): The new URL value.
        """
        self.__url = value

    @property
    def base_url(self) -> str:
        """str: The base URL used for constructing absolute URLs."""
        return self.__base_url

    @base_url.setter
    def base_url(self, value: str) -> None:
        """Set the base URL for constructing absolute URLs.

        Args:
            value (str): The new base URL value.
        """
        self.base__url = value

    async def __get_response(self) -> None:
        """Internal method to perform asynchronous HTTP GET request."""
        try:
            async with AsyncClient(
                headers=HEADERS, timeout=self.__timeout, base_url=self.__base_url if self.__base_url else ""
            ) as client:
                self.__response = await client.get(self.__url)
        except HTTPError as err:
            print(f"Error HTTP: {err}")
            logger.exception("Error HTTP")
        except Exception as err:
            print(f"Unexpected Error: {err}")
            logger.exception("Error HTTP")

    async def get_soup(self) -> None:
        """Fetch content from the URL and parse it into a BeautifulSoup object."""
        await self.__get_response()
        if self.__response and self.__response.status_code == 200:
            self.__soup = BeautifulSoup(self.__response.text, PARSER)
            logger.debug("Crawling at %s%s", self.__base_url, self.__url)
        else:
            logger.exception("Invalid HTTPS status code")
            raise Exception("Failed to get soup: Invalid response status code")
