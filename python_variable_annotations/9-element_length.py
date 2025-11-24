#!/usr/bin/env python3
""" a function that takes a list and returns a list of each content lenght"""
import typing


def element_length(lst: typing.Iterable[typing.Sequence]) -> typing.List[
        typing.Tuple[typing.Sequence, int]
        ]:
    return [(i, len(i)) for i in lst]
