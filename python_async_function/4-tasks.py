#!/usr/bin/env python3
""" a module containing a function that wait n times wait random """
import asyncio
import heapq

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> list[float]:
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

    coroutines = [task_wait_random(max_delay) for _ in range(n)]
    result = await asyncio.gather(*coroutines)

    # creating a heap with resulting gather
    heap = []
    for value in result:
        heapq.heappush(heap, value)

    # sort array by popping items from the heap they come with smallest first
    sorted_array = [heapq.heappop(heap) for _ in range(len(heap))]

    return sorted_array
