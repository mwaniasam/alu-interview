#!/usr/bin/python3

"""
This module provides a function to calculate the fewest number
of operations needed to result in exactly n H characters in a file.
"""


def min_operations(n):
    """
    Calculate the minimum number of operations required to achieve n H characters.

    Operations:
    - Copy All
    - Paste

    Args:
        n (int): The target number of H characters.

    Returns:
        int: The minimum number of operations required. If n is impossible
             to achieve, returns 0.
    """
    if n <= 1:
        return 0

    operations = 0
    divisor = 2  # Start checking from the smallest prime number
    while n > 1:
        while n % divisor == 0:
            operations += divisor
            n //= divisor
        divisor += 1

    return operations
