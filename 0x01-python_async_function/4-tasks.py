#!/usr/bin/env python3
"""
    Take the code from wait_n and alter it
"""
import asyncio
from typing import List

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    task_wait_n()

    Args:
      - n -> number of times to spawn async requests
      - max_delay -> max delay value

    Return:
      - floats
    """
    result = await asyncio.gather(
        *[task_wait_random(max_delay) for i in range(n)]
    )
    return sorted(result)
