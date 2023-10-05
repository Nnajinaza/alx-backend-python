#!/usr/bin/env python3
from typing import List
"""Write a type-annotated function sum_list"""


def sum_list(input_list: List[float]) -> float:
    """akes a list input_list of floats as argument and
    returns their sum as a float"""
    return float(sum(input_list))