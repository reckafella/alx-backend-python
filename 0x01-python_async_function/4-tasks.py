#!/usr/bin/env python3
'''
Take the code from wait_n and alter it into a new function task_wait_n.\
    The code is nearly identical to wait_n except task_wait_random is\
        being called.
'''
import asyncio
from typing import List
twr = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    '''
    function will spawn task_wait_random n times with the specified max_delay.
    '''
    res = await asyncio.gather(*(twr(max_delay) for _ in range(n)))
    return sorted(res)
