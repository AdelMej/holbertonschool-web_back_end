#!/usr/bin/env python3
""" a module containing a function that sums a list of float"""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """
    a function that sum a list of float

    Attributes:
        input_list(list[float]): a list of floats

    Returns:
        the sums of the floats
    """
    result = 0.0
    for f in input_list:
        result += f

    return result
