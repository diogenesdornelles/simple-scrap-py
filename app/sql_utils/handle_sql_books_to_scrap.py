from crawlers.models import CrawlResult
from sqlalchemy.orm import Session
from tasks.models import ColumnsBooksToScrap

from .connect import engine, start_connection
from .handle_sql_abc import HandleSQLABC
from .tables_factory import BooksToScrapTableFactory


class HandleSQLBooksToScrap(HandleSQLABC):
    """HandleSQLBooksToScrap _summary_

    Args:
        HandleSQLABC (_type_): Abstract class to handle SQL
    """
    def __init__(self, data: CrawlResult, table_name: str):
        """__init__ _summary_

        Args:
            data (CrawlResult): the refined data
            table_name (str): table name
        """
        self.__data = data
        start_connection()
        self.__table = BooksToScrapTableFactory.create_table(table_name)

    def persisting(self) -> None:
        """persisting: method for persiste data in mysql database
        """
        items = []
        with Session(bind=engine) as session:
            for link, price, title in zip(
                self.__data[ColumnsBooksToScrap.LINK.value],
                self.__data[ColumnsBooksToScrap.PRICE.value],
                self.__data[ColumnsBooksToScrap.TITLE.value],
            ):
                item = self.__table(link=link, price=price, title=title)
                items.append(item)
            session.add_all(items)
            session.commit()
            session.close()
