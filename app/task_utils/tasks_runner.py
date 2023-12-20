from constants import TARGET_DIR
from crawlers.models import CrawlResult
from save_handler import SaveHandler
from utils.log import logger
from .task_protocol import TaskProtocol


class TasksRunner:
    """Class responsible for running multiple tasks in a sequential manner.

    TasksRunner manages the execution of multiple tasks defined by TaskProtocol instances. It performs
    crawling, post-processing, and handling of the obtained results.

    Attributes:
        _spiders (list[TaskProtocol]): List of TaskProtocol instances representing the tasks to run.
    """

    def __init__(self) -> None:
        """Initialize TasksRunner."""
        self._spiders: list[TaskProtocol] | list = []

    def add_spiders(self, *args: TaskProtocol) -> None:
        """Add TaskProtocol instances to be executed by the TasksRunner.

        Args:
            *args (TaskProtocol): Variable number of TaskProtocol instances to add.
        """
        for spider in args:
            self._spiders.append(spider)

    async def run(self):
        """Execute the tasks added to TasksRunner."""
        for spider in self._spiders:
            logger.info("Initializing tasks...")
            await spider.crawl()
            await spider.posprocess_data()
            result: CrawlResult = spider.results
            file_handler: SaveHandler = SaveHandler(spider.name, result, TARGET_DIR)
            file_handler.to_json()
            file_handler.to_df()
            file_handler.to_mysql()
            logger.info("All tasks completed.")
