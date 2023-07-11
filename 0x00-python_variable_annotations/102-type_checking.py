#!/usr/bin/env python3
"""
Contains a func that returns  a list of ints
multiplied by certain factor.
"""
from typing import Tuple, List


def zoom_array(lst: Tuple, factor: int = 2) -> List:
    """Returns a list of ints multiplied by certain factor.
    Args:
        lst: A tuple of ints.
        factor: An integer.
    Returns:
        A list of ints.
    """
    zoomed_in: List = [
        item for item in lst
        for i in range(factor)
    ]
    return zoomed_in


array: Tuple = (12, 72, 91)

zoom_2x = zoom_array(array)

zoom_3x = zoom_array(array, 3)
