#!/usr/bin/env python3
'''
module contains a function that computes and returns a list of lengths of\
    sequences passed as argument
'''
from typing import Iterable, List, Sequence, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    '''
    Computes the length of a list of sequences
    '''
    return [(i, len(i)) for i in lst]
