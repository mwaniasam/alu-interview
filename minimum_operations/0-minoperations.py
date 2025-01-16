#!/usr/bin/python3

def min_operations(n):
    """
    Calculate the minimum number of operations required to achieve n from 1.

    Args:
        n (int): The target number.

    Returns:
        int: The minimum number of operations.
    """
    if n <= 1:
        return 0

    operations = 0
    divisor = 2

    while n > 1:
        while n % divisor == 0:
            operations += divisor
            n //= divisor
        divisor += 1

    return operations
