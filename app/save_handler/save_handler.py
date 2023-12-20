import json
import os
from time import time

import pandas as pd
from crawlers.models import CrawlResult
from sql_utils import DATABASES, HandleSQLABC
from utils.log import logger

from .i_save_handler import ISaveHandler


class SaveHandler(ISaveHandler):
    """Handles the saving of data in various formats such as dataframe, JSON, and MySQL database.

    SaveHandler is responsible for managing the different ways data can be saved in databases.

    Args:
        ISaveHandler (class): Interface for SaveHandler.
    """

    def __init__(self, name: str, data: CrawlResult, target_dir: str):
        """Initialize SaveHandler with necessary parameters.

        Args:
            name (str): The database name.
            data (CrawlResult): The refined result data.
            target_dir (str): The target directory.
        """
        self.__name = name
        self.__data = data
        self.__target_dir = target_dir

        self.__target_dir = os.path.join(self.__target_dir, self.__name)
        os.makedirs(self.__target_dir, exist_ok=True)

    def to_df(self) -> None:
        """Saves data to a DataFrame."""
        logger.debug("Saving as a DataFrame...")
        try:
            d_f = pd.DataFrame(self.__data)
            file_path = os.path.join(self.__target_dir, f"{self.__name}_{int(time())}.xlsx")
            d_f.to_excel(file_path, sheet_name=self.__name, index=False)
        except Exception as e:
            print(e)
            logger.critical("Failed to save as a DataFrame...")

    def to_json(self) -> None:
        """Saves data to a JSON file."""
        logger.debug("Saving as JSON data...")
        try:
            file_path = os.path.join(self.__target_dir, f"{self.__name}_{int(time())}.json")
            with open(file_path, "w", encoding="utf-8") as json_file:
                json.dump(self.__data, json_file)
        except Exception as e:
            print(e)
            logger.critical("Failed to save as JSON...")

    def to_mysql(self) -> None:
        """Saves data to a MySQL database."""
        logger.debug("Saving on a MySQL database...")
        try:
            sql = DATABASES[self.__name](self.__data, self.__name)
            if isinstance(sql, HandleSQLABC):
                sql.persisting()
        except Exception as e:
            print(e)
            logger.critical("Failed to save on a MySQL database...")
