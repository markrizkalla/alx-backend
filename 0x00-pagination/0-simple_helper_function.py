#!/usr/bin/env python3
"""return tuple contain start and end index"""


def index_range(page: int, page_size: int) -> tuple:
    """cal start & end index"""
    start = (page - 1) * page_size
    end = start + page_size
    return (start, end)
