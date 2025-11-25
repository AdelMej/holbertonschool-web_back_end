#!/usr/bin/env python3
""" a module containing a function that wait n times wait random """
import asyncio
import typing

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> typing.List[float]:
    """
    a function that create n coroutines and returns
    a sorted list of wait_random

    Attributes:
        n(int): the number of wait_random coroutine to run
        max_delay(int): the maximum delay for each wait_random coroutines

    Returns:
        a sorted list of wait_random dealays sorted in ascending order
    """
    if n == 0:
        return []

    tasks = [task_wait_random(max_delay) for _ in range(n)]

    output = []
    for task in asyncio.as_completed(tasks):
        result = await task
        output.append(result)

    return output
