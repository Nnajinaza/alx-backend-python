#!/usr/bin/env python3
import random
import asyncio

"""Write an asynchronous"""


async def wait_random(max_delay: int = 10) -> float:
    """
    Args:
      - max_delay -> max delay value with default of 10

    Return:
      - floats
    """
    result = random.uniform(0, max_delay)
    await asyncio.sleep(result)
    return (result)
