#!/usr/bin/env python3
'''
Module does:
From the '1-concurrent_coroutines.py', import wait_n

Creates a measure_time function with integers n and max_delay as arguments\
    that measures the total execution time for wait_n(n, max_delay), and\
        returns total_time / n. the function should return a float.
Uses the time module to measure an approximate elapsed time.
'''
import asyncio
import time
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    '''
    measures and returns the average total run time for wait_n
    '''
    start: float = time.perf_counter()
    asyncio.run(wait_n(n, max_delay))
    elapsed: float = time.perf_counter() - start
    return (elapsed / n)
