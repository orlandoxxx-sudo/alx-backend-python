#!/usr/bin/env python3
"""
A simple Task
"""

import asyncio


wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    A function that takes an int 'max_delay' and returns a 'asyncio.Task'
    """
    task = asyncio.create_task(wait_random(max_delay))
    return task
