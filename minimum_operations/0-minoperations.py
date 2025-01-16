#!/usr/bin/python3

"""
This module provides a function to calculate the minimum number
of operations required to achieve a target number starting from 1.
"""

import math

def min_operations(n):
    """
    Calculate the minimum number of operations required to achieve n from 1.

    Args:
        n (int): The target number.

    Returns:
        int: The minimum number of operations required. If n is not
             a positive integer, returns 0.
    """

    if n <= 1:
        return 0

    operations = 0
    for i in range(2, int(math.sqrt(abs(n))) + 1):
        while n % i == 0:
            operations += i
            n //= i

    if n > 1:
        operations += n

    return operations
