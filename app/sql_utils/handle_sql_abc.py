from abc import ABC, abstractmethod
from crawlers.models import CrawlResult


class HandleSQLABC(ABC):
    """Abstract class for handling SQL queries and data persistence.

    This class defines an abstract interface for handling SQL queries and persisting data
    into a database.

    Args:
        ABC (type): A Python metaclass for defining abstract base classes.

    Raises:
        NotImplementedError: If any abstract method is not implemented in the subclass.

    Attributes:
        data (CrawlResult): The refined data result to be persisted.
        table_name (str): The name of the table in the database to save the data.

    """

    @abstractmethod
    def __init__(self, data: CrawlResult, table_name: str):
        """Initialize the HandleSQLABC class.

        Args:
            data (CrawlResult): The refined data result to be persisted.
            table_name (str): The name of the table in the database to save the data.

        Raises:
            NotImplementedError: If the method is not implemented in the subclass.
        """
        raise NotImplementedError

    @abstractmethod
    def persisting(self) -> None:
        """Persist the data into the database.

        This method should be implemented in a subclass to define how the data will be
        saved into the database.

        Raises:
            NotImplementedError: If the method is not implemented in the subclass.
        """
        raise NotImplementedError
