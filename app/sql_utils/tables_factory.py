from datetime import datetime
from time import time
from typing import Annotated, Any, List, Type

from sqlalchemy import Float, Integer, Text, func
from sqlalchemy.dialects.mysql import JSON
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, registry
from abc import abstractmethod, ABC

from .connect import engine

InTpk = Annotated[int, mapped_column(Integer, primary_key=True)]

timestamp = Annotated[
    datetime,
    mapped_column(nullable=False, server_default=func.CURRENT_TIMESTAMP()),
]

reg = registry()


class TableFactory(ABC):
    @staticmethod
    @abstractmethod
    def create_table() -> Type[DeclarativeBase]:
        """
        'A static abstract method that should be implemented by subclasses.

        Subclasses need to implement this method to define and create a specific type
        of database table using SQLAlchemy's DeclarativeBase or a subclass of it.

        Returns:
            Type[DeclarativeBase]: A SQLAlchemy DeclarativeBase subclass representing
            the table structure.

        Raises:
            NotImplementedError: This exception is raised if the method is not implemented
            by a subclass.
        """
        raise NotImplementedError


class IMDBTableFactory(TableFactory):
    """IMDBTableFactory _summary_

    Args:
        TableFactory (_type_): _description_

    Returns:
        _type_: _description_
    """

    @staticmethod
    def create_table(table_name: str) -> Any:
        """create_table: create Table as SQLAlchemy declarative mode

        Args:
            table_name (str): table name

        Returns:
            Any: Table class
        """

        @reg.mapped_as_dataclass(kw_only=True)
        class IMDB:
            """define a class (IMDB) that models an IMDb-like entity and maps its attributes to a database table using
            an ORM SQLAlchemy
            """

            __tablename__ = f"{table_name}_{int(time())}"
            id: Mapped[InTpk] = mapped_column(init=False)
            movie: Mapped[str] = mapped_column(Text, nullable=False, unique=True)
            year: Mapped[int] = mapped_column(Integer, nullable=False)
            sinopsis: Mapped[str] = mapped_column(Text, nullable=False)
            director: Mapped[List[str]] = mapped_column(JSON, nullable=False)
            artists: Mapped[List[str]] = mapped_column(JSON, nullable=False)
            rating: Mapped[float] = mapped_column(Float, nullable=False)
            ranking: Mapped[int] = mapped_column(Integer, nullable=False)
            created_at: Mapped[timestamp] = mapped_column(init=False)

        reg.metadata.create_all(bind=engine)
        return IMDB


class BooksToScrapTableFactory(TableFactory):
    """BooksToScrapTableFactory _summary_

    Args:
        TableFactory (_type_): _description_

    Returns:
        _type_: _description_
    """

    @staticmethod
    def create_table(table_name: str) -> Type[DeclarativeBase]:
        """create_table _summary_

        Returns:
            Type[DeclarativeBase]: _description_
        """

        class Base(DeclarativeBase):
            pass

        class BooksToScrap(Base):
            """BooksToScrap _summary_

            Args:
                Base (_type_): _description_
            """

            __tablename__ = f"{table_name}_{int(time())}"
            id: Mapped[InTpk]
            price: Mapped[float] = mapped_column(Float(precision=2, decimal_return_scale=2))
            link: Mapped[str] = mapped_column(Text)
            title: Mapped[str] = mapped_column(Text)

        Base.metadata.create_all(bind=engine)
        return BooksToScrap


class OlxTableFactory(TableFactory):
    """OlxTableFactory _summary_

    Args:
        TableFactory (_type_): _description_

    Returns:
        _type_: _description_
    """

    @staticmethod
    def create_table(table_name: str) -> Type[DeclarativeBase]:
        """create_table _summary_

        Returns:
            Type[DeclarativeBase]: _description_
        """

        class Base(DeclarativeBase):
            pass

        class Olx(Base):
            """BooksToScrap _summary_

            Args:
                Base (_type_): _description_
            """

            __tablename__ = f"{table_name}_{int(time())}"
            id: Mapped[InTpk]
            price: Mapped[float] = mapped_column(Float(precision=2, decimal_return_scale=2))
            name: Mapped[str] = mapped_column(Text)
            description: Mapped[str] = mapped_column(Text)

        Base.metadata.create_all(bind=engine)
        return Olx
