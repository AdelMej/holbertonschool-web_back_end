#!/usr/bin/env python3
""" a function that sum up float and ints """
from typing import List
from typing import Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    a function that sums a mixed list of int and floats

    Attributes:
        mxd_lst(list(union[int, float])): a list of int and float

    Returns:
        result(float): the sum of all the values in the list
    """
    result = 0.0
    for value in mxd_lst:
        result += value

    return result
