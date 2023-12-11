#!/usr/bin/env python3
'''
Module contains a coroutine called async_generator that takes no arguments.

The coroutine will loop 10 times, each time asynchronously wait 1 second,\
    then yield a random number between 0 and 10. Use the random module.
'''
import asyncio
from random import uniform
from typing import AsyncGenerator


async def async_generator() -> AsyncGenerator[float, None]:
    '''
    loops 10 times and each time sleep for 1 second and then yield a random\
        number from 0-10
    '''
    for _ in range(10):
        await asyncio.sleep(1)
        yield uniform(0, 10)
