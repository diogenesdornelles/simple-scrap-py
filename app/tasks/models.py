from task_utils.column import Column


class ColumnsIMDB(Column):
    """Enumeration defining columns specific to IMDB data.

    ColumnsIMDB enumerates the columns related to IMDB data such as movie, year, director,
    rating, artists, ranking, and sinopsis.

    Args:
        Enum (type): A Python enumeration for defining a set of named constants.

    Attributes:
        MOVIE: Represents the movie column.
        YEAR: Represents the year column.
        DIRECTOR: Represents the director column.
        RATING: Represents the rating column.
        ARTISTS: Represents the artists column.
        RANKING: Represents the ranking column.
        SINOPSIS: Represents the sinopsis column.

    """

    MOVIE = "movie"
    YEAR = "year"
    DIRECTOR = "director"
    RATING = "rating"
    ARTISTS = "artists"
    RANKING = "ranking"
    SINOPSIS = "sinopsis"


class ColumnsBooksToScrap(Column):
    """Enumeration defining columns specific to book data for scraping.

    ColumnsBooksToScrap enumerates the columns related to book data scraping, including
    price, title, and link.

    Args:
        Enum (type): A Python enumeration for defining a set of named constants.

    Attributes:
        PRICE: Represents the price column.
        TITLE: Represents the title column.
        LINK: Represents the link column.

    """

    PRICE = "price"
    TITLE = "title"
    LINK = "link"


class ColumnsOlx(Column):
    """Enumeration defining columns specific to OLX data.

    ColumnsOlx enumerates the columns related to OLX data such as name, price, and description.

    Args:
        Enum (type): A Python enumeration for defining a set of named constants.

    Attributes:
        NAME: Represents the name column.
        PRICE: Represents the price column.
        DESCRIPTION: Represents the description column.

    """

    NAME = "name"
    PRICE = "price"
    DESCRIPTION = "description"
