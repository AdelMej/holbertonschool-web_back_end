#!/usr/bin/env python3
"""
a module containing a function that provides a task to be run by a coroutine
it uses wait_random
"""
import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    a function that provides a task for wait_random

    Atrributes:
        max_delay(int): the maximum delay possible for wait_random

    Returns:
        a task to execute with asyncio
    """
    return asyncio.create_task(wait_random(max_delay))
