#!/usr/bin/env python3
'''Asyncronous Python
'''
import time
import asyncio


wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
        Args:
        - n -> number of times to spawns the requests
        - max_delay -> max delay value

        Return:
        - float
    """
    result = time.time()
    asyncio.run(wait_n(n, max_delay))
    return (time.time() - result)/n