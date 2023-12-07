#!/usr/bin/env python3
'''
module containing a type-annotated function floor which takes a float n as\
    argument and returns the floor of the float.
'''
import math


def floor(n: float) -> int:
    '''
    a type-annotated function floor which takes a float n as argument
    and returns the floor of the float.
    '''
    return math.floor(n)
