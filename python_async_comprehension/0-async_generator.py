#!/usr/bin/env python3
"""
a module containing a function that generate asynchronically
random numbers 10 times
"""
import typing
import random
import asyncio


async def async_generator() -> typing.Generator[float, None, None]:
    """
    a function that generate an AsyncGenerator that returns 10 random values
    and await 1 second

    Returns:
        an asyncGenerator that can be iterated
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
