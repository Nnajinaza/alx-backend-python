#!/usr/bin/env python3
from typing import List, Union
"""Write a type-annotated function sum_list"""


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """akes a list mxd_lst of floats and intger as argument and
    returns their sum as a float"""
    return float(sum(mxd_lst))