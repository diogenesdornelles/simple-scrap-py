import os

DIR = os.getcwd()
TARGET_DIR = os.path.join(DIR, "files")
HEADERS = {"user-agent": "my-app/0.0.1"}
PARSER = "html.parser"
IMDB_BASE_URL = "https://www.imdb.com/"
IMDB_URL = "chart/top/"
BOOKS_TO_SCRAP_BASE_URL = "https://books.toscrape.com/catalogue/category/books_1/"
BOOKS_TO_SCRAP_URL = "index.html"
OLX_CARS_RS_BASE_URL = "https://www.olx.com.br"
OLX_CARS_RS_URL = "/autos-e-pecas/estado-rs"
