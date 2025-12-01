#!/usr/bin/env python3
"""
a function that benchmark the async_comprehension function
"""
import time
import asyncio
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    a function that benchmark 4 coroutines of async_comprehension
    Return:
        total time it took to run the 4 coroutines
    """
    start = time.perf_counter()
    await asyncio.gather(*[async_comprehension() for _ in range(4)])
    end = time.perf_counter()
    return (end - start)
