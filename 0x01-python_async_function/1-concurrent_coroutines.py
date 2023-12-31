#!/usr/bin/env python3
"""
Contains the definition of the wait_n() coroutine which
spawns multiple async processes
"""
import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Args:
      - n -> number of times to spawn the requests
      - max_delay -> max delay value

    Return:
      - list of floats
    """
    result = await asyncio.gather(*[wait_random(max_delay) for i in range(n)])
    return sorted(result)
