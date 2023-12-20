import os

from dotenv import find_dotenv, load_dotenv
from sqlalchemy import create_engine, text

load_dotenv(find_dotenv())
PASSWORD = os.environ.get("DB_PASSWORD")

engine = create_engine(f"mysql+pymysql://root:{PASSWORD}@localhost:3306/scrap_database", echo=True)


def start_connection() -> None:
    """start_connection start connection with database
    """
    try:
        with engine.connect() as connection:
            result = connection.execute(text("select 'is connected'"))
            print(result.all())
    except Exception as err:
        print(f"Unexpected Error: {err}")
