#!/usr/bin/env python3
import typing


def to_kv(k: str, v: typing.Union[int, float]) -> typing.Tuple[str, float]:
    """
    a function that takes a string and a float and returns a tuple

    Attributes:
        k(str): a string
        v(int | float): a value that is squared

    Returns:
        tuple(str, float): a tuple with a string and a squared value
    """
    return (k, v**2)
