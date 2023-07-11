#!/usr/bin/env python3
"""Contains a func that converts a Python var to a KV pair."""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """Converts a Python var to a KV pair."""
    return k, v ** 2
