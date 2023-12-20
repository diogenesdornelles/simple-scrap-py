from typing import Dict, Type

from .handle_sql_abc import HandleSQLABC
from .handle_sql_books_to_scrap import HandleSQLBooksToScrap
from .handle_sql_imdb import HandleSQLIMDB
from .handle_sql_olx import HandleSQLOlx

type TDatabases = Dict[str, Type[HandleSQLABC]]

DATABASES: TDatabases = {"imdb": HandleSQLIMDB, "books_to_scrap": HandleSQLBooksToScrap, "olx_cars_rs": HandleSQLOlx}
