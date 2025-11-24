#!/usr/bin/env python3
""" a function that takes a list and returns a list of each content lenght"""
import typing


def element_length(lst: typing.Iterable[typing.Sequence]) -> typing.List[
        typing.Tuple[typing.Sequence, int]
        ]:
    """
    a function that takes a list of iterable Sequence
    and returns a list of tuple that associate a sequence and it's length

    Attributes:
        lst(list(sequence)): a list of iterable sequencee

    Returns:
        a list of tuple that associate a sequence and it's length
    """
    return [(i, len(i)) for i in lst]
