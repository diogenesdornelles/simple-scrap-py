from typing import List
from task_utils import Task
from task_utils.data_getter import DataGetter
from utils import convert_to_float, convert_to_int, logger, treat_str
from .models import CrawlRawResult, CrawlResult


class Pipelines:
    """Class responsible for preprocessing data from CrawlRawResult to CrawlResult based on task definitions.

    This class handles the conversion and preprocessing of data from a CrawlRawResult object to a CrawlResult object
    according to the defined data getters in a Task object.

    Attributes:
        __data (CrawlRawResult): The raw data to be preprocessed.
        _results (CrawlResult): The preprocessed data.
        _data_getters (List[DataGetter]): List of data getters from the task object.
    """

    def __init__(self, data: CrawlRawResult, task: Task):
        """Initialize Pipelines instance.

        Args:
            data (CrawlRawResult): The raw data to be preprocessed.
            task (Task): The task object containing data getter definitions.
        """
        self.__data = data
        self._results: CrawlResult = {}
        self._data_getters: List[DataGetter] = task.data_getters

    @property
    def results(self) -> CrawlResult:
        """CrawlResult: The preprocessed data."""
        return self._results

    async def preprocess_data(self) -> None:
        """Preprocess data from CrawlRawResult to CrawlResult based on task definitions."""
        if len(self.__data) > 0:
            for key in self.__data:
                for getter in self._data_getters:
                    if key == getter.name.value and getter.preprocess:
                        match getter.type.value:
                            case "float":
                                self._results[key] = [convert_to_float(element) for element in self.__data[key]]
                            case "int":
                                self._results[key] = [convert_to_int(element) for element in self.__data[key]]
                            case "string":
                                self._results[key] = [treat_str(element) for element in self.__data[key]]
                            case "list":
                                if getter.subtype:
                                    match getter.subtype.value:
                                        case "float":
                                            self._results[key] = [
                                                [convert_to_float(element) for element in sublist]
                                                for sublist in self.__data[key]
                                            ]
                                        case "int":
                                            self._results[key] = [
                                                [convert_to_int(element) for element in sublist]
                                                for sublist in self.__data[key]
                                            ]
                                        case "string":
                                            self._results[key] = [
                                                [treat_str(element) for element in sublist]
                                                for sublist in self.__data[key]
                                            ]

            lengths: List[int] = [len(self._results[key]) for key in self._results]
            if not all(length == lengths[0] for length in lengths):
                msg = ""
                for key in self._results:
                    msg += f"{key}: length: {len(self._results[key])}\n"
                logger.warning("Columns do not have the same length:\n %s", msg)
                raise ValueError("Columns do not have the same length")
