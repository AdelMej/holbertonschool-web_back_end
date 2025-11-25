#!/usr/bin/env python3
"""
a module that has a function that collect 10 numbers from async_generator
"""
import typing
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> typing.List[float]:
    """
    a function that returns a list of 10 randomly generated floats
    Returns:
        a list of randomly generated floats
    """
    result = []
    async for value in async_generator():
        result.append(value)

    return result
