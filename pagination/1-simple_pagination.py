#!/usr/bin/env python3
""" this module contains a function that handle pagination parameters """
import csv
import math
from typing import List
import typing


def index_range(page: int, page_size: int) -> typing.Tuple[int, int]:
    """
    a function that returns the index of a page

    Attributes:
        page(int): the page we are in
        page_size(int): the page size

    Returns:
        a tuple containing the start and end index of the page
    """
    start_idx = (page - 1) * page_size
    end_idx = start_idx + page_size
    return (start_idx, end_idx)


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
        """
        method that get a page with a specific page size and page index

        Attributes:
            page(int): the page number
            page_size(int): the page size

        Returns:
            a list of list containing the relevant data
            empty if the index is out of range
        """
        assert isinstance(page, int) and isinstance(page_size, int)
        assert page > 0
        assert page_size > 0

        start_idx, end_idx = index_range(page, page_size)

        dataset = self.dataset()

        if start_idx >= len(dataset):
            return []

        return dataset[start_idx:end_idx]
