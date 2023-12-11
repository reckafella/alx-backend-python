#!/usr/bin/env python3
'''
Module imports wait_random from '0-basic_async_syntax.py'\
    then implements an async routine called wait_n that takes in 2 arguments\
        in this order: n and max_delay.\
            It will spawn wait_random n times with the specified max_delay.
'''
import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    '''
    function will spawn wait_random n times with the specified max_delay.
    '''
    res = await asyncio.gather(*(wait_random(max_delay) for _ in range(n)))
    return sorted(res)
