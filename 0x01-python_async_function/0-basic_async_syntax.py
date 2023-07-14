#!/usr/bin/env python3
"""Contains a coroutine that delays an amount of time and returns it"""

import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """
    Returns a random float range 0 and max_delay
    Args:
        max_delay: The maxi delay to return
    Returns:
        A random float range 0 and max_delay
    """
    rand = random.uniform(0, max_delay)
    await asyncio.sleep(rand)
    return rand
