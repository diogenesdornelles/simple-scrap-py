from crawlers.models import CrawlResult
from sqlalchemy.orm import Session
from tasks.models import ColumnsOlx

from .connect import engine, start_connection
from .handle_sql_abc import HandleSQLABC
from .tables_factory import OlxTableFactory


class HandleSQLOlx(HandleSQLABC):
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
        self.__table = OlxTableFactory.create_table(table_name)

    def persisting(self) -> None:
        """persisting: method for persiste data in database"""
        items = []
        with Session(bind=engine) as session:
            for price, _name, description in zip(
                self.__data[ColumnsOlx.PRICE.value],
                self.__data[ColumnsOlx.NAME.value],
                self.__data[ColumnsOlx.DESCRIPTION.value],
            ):
                item = self.__table(price=price, name=_name, description=description)
                items.append(item)
            session.add_all(items)
            session.commit()
            session.close()
