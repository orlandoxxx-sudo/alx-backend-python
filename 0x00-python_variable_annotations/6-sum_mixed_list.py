#!/usr/bin/env python3
"""
Complex types - mixed list
"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    A function that takes a list containing floats and integers,
    and returns the sum of all
    """
    return sum(mxd_lst)
