from typing import Dict, List, TypeAlias, Union

""" _summary_
"""
CrawlRawResult: TypeAlias = Dict[str, List[str]]

CrawlResult = Dict[str, List[Union[str, int, float, list, dict]]]
