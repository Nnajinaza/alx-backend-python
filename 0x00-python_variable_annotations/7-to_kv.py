#!/usr/bin/env python3
from typing import Union, Tuple
"""Write a type-annotated function to_kv
that takes a string k and an int OR float
vas arguments and returns a tuple.
"""


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """The first element of the tuple is the string
    k. The second element is the square of
    the int/float v
    and should be annotated as a float."""
    return (k, float(v**2))
