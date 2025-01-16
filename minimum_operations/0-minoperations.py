#!/usr/bin/python3

"""
This module provides a function to calculate the minimum number
of operations required to achieve a target number starting from 1.
"""


def min_operations(n):
    """
    Calculate the minimum number of operations required to achieve n from 1.

    Args:
        n (int): The target number.

    Returns:
        int: The minimum number of operations required. If n is not
             a positive integer, returns 0.
    """
    if not isinstance(n, int) or n <= 1:
        return 0

    operations = 0
    divisor = 2

    while n > 1:
        while n % divisor == 0:
            operations += divisor
            n //= divisor
        divisor += 1

    return operations
