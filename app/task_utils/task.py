from typing import Any, Dict, List, Optional
from pydantic import BaseModel, Field, root_validator
from utils import is_valid_url
from .data_getter import DataGetter
from .link_getter import LinkGetter


class Task(BaseModel):
    """Model representing a task configuration for crawling data.

    Task defines a set of properties and configurations required for executing a crawling task,
    including the task name, URL, base URL, data getters, link getter, and page limits.

    Args:
        BaseModel (type): Base Pydantic model for defining attributes.

    Attributes:
        name (str): The name of the task.
        url (str): The URL to crawl.
        base_url (str): The base URL for constructing absolute URLs.
        data_getters (List[DataGetter]): List of data getters used to extract specific data from the web page.
        link_getter (Optional[LinkGetter]): Getter for extracting links (default is None).
        pages (Optional[int]): Limit for the number of pages to crawl (default is None).

    """

    name: str = Field(..., kw_only=True, title="task_name", min_length=3, pattern="^[a-zA-Z0-9_]{3,}$")
    url: str = Field(..., kw_only=True, title="url")
    base_url: str = Field(..., kw_only=True, title="base_url")
    data_getters: List[DataGetter] = Field(..., kw_only=True, title="get_tasks", min_length=1)
    link_getter: Optional[LinkGetter] = Field(default=None, kw_only=True, title="limit")
    pages: Optional[int] = Field(default=None, kw_only=True, title="limit")

    class Config:
        arbitrary_types_allowed = True

    def to_dict(self) -> Dict[str, Any]:
        """Converts Task object to a dictionary representation."""
        return {
            "name": self.name,
            "data_getters": self.data_getters,
            "url": self.url,
            "next": self.link_getter.to_dict() if self.link_getter else "",
        }

    @root_validator(skip_on_failure=True, allow_reuse=True)
    def validate_fields(cls, values: Dict[str, str]) -> Dict[str, str] | Any:
        """Validate the URL fields and their combinations."""
        url: Optional[str] = values.get("url")
        base_url: Optional[str] = values.get("base_url")
        concatStr: str = "".join(filter(None, [base_url, url]))
        if is_valid_url(concatStr):
            return values
        raise ValueError(f"An invalid URL was provided: {concatStr}")


if __name__ == "__main__":
    pass
