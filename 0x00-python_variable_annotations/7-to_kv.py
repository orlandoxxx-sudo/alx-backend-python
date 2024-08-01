#!/usr/bin/env python3
""" Variable Annotation
"""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """Function thaat takes a string and int/float to return a Tuple
    """
    return (k, v**2)
