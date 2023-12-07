#!/usr/bin/env python3
'''
module for annotations
'''
from typing import Iterable, List, Sequence, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    '''
    more annotations example
    '''
    return [(i, len(i)) for i in lst]
