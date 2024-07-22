#!/usr/bin/env python3
<<<<<<< HEAD
import csv
import math
from typing import List


def index_range(page: int, page_size: int) -> tuple:
    """cal start & end index"""
    start = (page - 1) * page_size
    end = start + page_size
    return (start, end)

=======
""" 1. Simple pagination
"""

import csv
from typing import List, Tuple


>>>>>>> a55c8c28a9f53dd6b86e7572b50fd90d115517cb
class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
<<<<<<< HEAD
        assert type(page) == int or type(page_size) == int, "AssertionError raised when page and/or page_size are not ints"
        assert page >= 0 or page_size >= 0, "negative values"

        indexex = index_range(page, page_size)
        start, end =  indexex[0], indexex[1]
        data = self.dataset()
        print(data[start])
        return data
            
=======
        """ Finds the correct indexes to paginate dataset.
        """
        assert type(page) == int
        assert type(page_size) == int
        assert page > 0
        assert page_size > 0
        csv_size = len(self.dataset())
        start, end = index_range(page, page_size)
        end = min(end, csv_size)
        if start >= csv_size:
            return []
        return self.dataset()[start:end]


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """ Returns a tuple containing a start and end index.
    """
    return ((page - 1) * page_size, page * page_size)
>>>>>>> a55c8c28a9f53dd6b86e7572b50fd90d115517cb
