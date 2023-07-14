#!/usr/bin/env python3
"""Contains a method tha returns a task"""
import asyncio

wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    Returns a task that waits for a rand number of secs
    Args:
        max_delay: max number of seconds that the task will wait
    Returns: an asyncio.Task object
    """
    return asyncio.create_task(wait_random(max_delay))
