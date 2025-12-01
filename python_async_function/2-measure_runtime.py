#!/usr/bin/env python3
"""
A module containing a function that mesure the time it takes to run wait_n
"""
import time
import asyncio
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    a function that mesure the time it takes to run wait_n

    Attributes:
        n(int): number of repetition in wait_n
        max_delay(int): max_delay of wait_n
    Returns:
        the time it took to run all coroutines
    """
    start = time.perf_counter()
    asyncio.run(wait_n(n, max_delay))
    end = time.perf_counter()

    return (end - start)
