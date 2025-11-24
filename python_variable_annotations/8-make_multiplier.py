#!/usr/bin/env python3
"""
a module that contains a function that takes a multiplier
and returns a function
"""
import typing


def make_multiplier(multiplier: float) -> typing.Callable[[float], float]:
    """
    function that takes a multiplier and returns a function

    Attributes:
        multiplier(float): a multiplier

    Returns:
        a function that multiplies by the multiplier
    """
    return (lambda x: x*multiplier)
