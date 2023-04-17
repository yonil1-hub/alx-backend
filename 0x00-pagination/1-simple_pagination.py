#!/usr/bin/env python3
""" Pagination class """


import csv
from typing import List


class Server:
    """A class for paginating a database of popular baby names"""

    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def index_range(self, page: int, page_size: int) -> List[int]:
        """Returns the start and end indexes for a given page and page size"""
        start_index = (page - 1) * page_size
        end_index = start_index + page_size
        return [start_index, end_index]

    def dataset(self) -> List[List[str]]:
        """Returns the cached dataset of popular baby names"""
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
                self.__dataset = dataset[1:]
        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List[str]]:
        """Returns the data for a given page and page size"""

        assert page > 0 and page_size > 0, "Error"
        start_index, end_index = self.index_range(page, page_size)
        return self.dataset()[start_index:end_index]
