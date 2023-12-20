import asyncio
import time

from crawlers import IMDB  # , BooksToScrap, Olx
from task_utils import TasksRunner
from tasks import imdb_tasks  # books_to_scrap_tasks, , olx_cars_rs_task
from utils import logger

if __name__ == "__main__":

    async def main() -> None:
        """main program"""
        init = time.perf_counter()

        # books_to_scrap: BooksToScrap = BooksToScrap(books_to_scrap_tasks)
        imdb: IMDB = IMDB(imdb_tasks)
        tasks: TasksRunner = TasksRunner()
        tasks.add_spiders(imdb)
        await tasks.run()
        final = time.perf_counter()
        total = final - init
        logger.info("Time execution: %s", total)

    asyncio.run(main())
