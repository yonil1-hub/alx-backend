#!/usr/bin/env python3
""" Server class """

import csv
from typing import List


class Server:
    """
    A class for paginating a database of popular baby names
    """

    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def index_range(self, page: int, page_size: int) -> tuple:
        """
        Returns a tuple of size two containing a start index and an end index
        corresponding to the range of indexes to return for the given pagination
        parameters
        """
        start_index = (page - 1) * page_size
        end_index = start_index + page_size
        return (start_index, end_index)

    def dataset(self) -> List[List[str]]:
        """
        Returns the cached dataset of popular baby names read from a CSV file
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                self.__dataset = [row for row in reader][1:]
        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List[str]]:
        """
        Returns a list of baby names corresponding to the given pagination
        parameters
        """
        assert page > 0 and page_size > 0, "Both page and page_size must be positive integers"
        start_index, end_index = self.index_range(page, page_size)
        return self.dataset()[start_index:end_index]

