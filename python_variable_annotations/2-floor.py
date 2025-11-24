#!/usr/bin/env python3
""" a module that contains a floor function that floor a float"""


def floor(n: float) -> int:
    """
    a function that returns the floor of a float

    Attributes:
        n(float): a float to find the floor of

    Returns:
        (int) the floor of n
    """
    return n.__floor__()
