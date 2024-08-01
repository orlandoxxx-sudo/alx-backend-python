#!/usr/bin/env python3
"""
Complex-type annotated function
"""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """
    A function that takes a list of floats and
    returns the sum of all its components
    """
    return sum(input_list)
