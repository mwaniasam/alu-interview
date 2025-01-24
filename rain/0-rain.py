#!/usr/bin/python3
"""
Rain Module

This module provides a function to calculate the amount of rainwater
that can be trapped between walls of varying heights.
"""


def rain(walls):
    """
    Calculate the total amount of rainwater retained.

    :param walls: List of non-negative integers representing wall heights.
    :return: Total amount of water retained as an integer.
    """
    if not walls:
        return 0

    water = 0
    for i in range(1, len(walls) - 1):
        left_max = walls[i]
        for j in range(i):
            left_max = max(left_max, walls[j])

        right_max = walls[i]
        for j in range(i + 1, len(walls)):
            right_max = max(right_max, walls[j])

        water += max(0, min(left_max, right_max) - walls[i])

    return water
