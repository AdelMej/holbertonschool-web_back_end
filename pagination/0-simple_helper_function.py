#!/usr/bin/env python3
""" this module contains a function that handle pagination parameters """
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
