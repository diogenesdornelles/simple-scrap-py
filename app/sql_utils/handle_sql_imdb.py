from crawlers.models import CrawlResult
from sqlalchemy.orm import Session
from tasks.models import ColumnsIMDB

from .connect import engine, start_connection
from .handle_sql_abc import HandleSQLABC
from .tables_factory import IMDBTableFactory


class HandleSQLIMDB(HandleSQLABC):
    """Class for handling SQL queries and data persistence.

    This class defines an abstract interface for handling SQL queries and persisting data
    into a database.

    Args:
        HandleSQLABC (type): Abbstract class for handling SQL queries and data persistence.

    Raises:
        NotImplementedError: If any abstract method is not implemented in the subclass.

    Attributes:
        data (CrawlResult): The refined data result to be persisted.
        table_name (str): The name of the table in the database to save the data.

    """

    def __init__(self, data: CrawlResult, table_name: str):
        """__init__ constructor

        Args:
            data (CrawlResult): The refined data result to be persisted.
        table_name (str): The name of the table in the database to save the data.
        """
        self.__data = data
        start_connection()
        self.__table = IMDBTableFactory.create_table(table_name)

    def persisting(self) -> None:
        """Persist the data into the database.

        Raises:
            NotImplementedError: If the method is not implemented in the subclass.
        """
        items = []
        with Session(bind=engine) as session:
            for movie, year, sinopsis, director, artists, rating, ranking in zip(
                self.__data[ColumnsIMDB.MOVIE.value],
                self.__data[ColumnsIMDB.YEAR.value],
                self.__data[ColumnsIMDB.SINOPSIS.value],
                self.__data[ColumnsIMDB.DIRECTOR.value],
                self.__data[ColumnsIMDB.ARTISTS.value],
                self.__data[ColumnsIMDB.RATING.value],
                self.__data[ColumnsIMDB.RANKING.value],
            ):
                item = self.__table(
                    movie=movie,
                    year=year,
                    sinopsis=sinopsis,
                    director=director,
                    artists=artists,
                    rating=rating,
                    ranking=ranking,
                )
                items.append(item)
            session.add_all(items)
            session.commit()
            session.close()
