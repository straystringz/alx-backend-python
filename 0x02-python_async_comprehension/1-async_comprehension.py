#!/usr/bin/env python3
""" a python module to returns 10 rand nums using async comprehension"""
from typing import List
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
    async_comprehension- func to return 10 ranm numbs
    Arguments:
        no args
    Returns:
        10 rand nums
    """
    rslt = [i async for i in async_generator()]
    return rslt
