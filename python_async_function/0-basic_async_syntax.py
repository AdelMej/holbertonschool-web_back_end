#!/usr/bin/env python3
"""
a module containing a function that does asyncio sleep on random uniform values
"""
import random
import asyncio


async def wait_random(max_delay: int = 10) -> float:
    """
    a function that takes a delay in parameters
    does an async wait and returns the delay

    Attributes:
        max_delay(int): maximum delay possible

    Returns:
        waited(float) the amount of time waited
    """
    waited = random.uniform(0, max_delay)
    await asyncio.sleep(waited)
    return waited
