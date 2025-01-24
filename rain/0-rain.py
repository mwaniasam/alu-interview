#!/usr/bin/python3
""" Rain Module """
def rain(walls):
    if not walls:
        return 0
    water = 0
    for i in range(1, len(walls) - 1):
        left = walls[i]
        for j in range(i):
            left = max(left, walls[j])
        right = walls[i]
        for j in range(i + 1, len(walls)):
            right = max(right, walls[j])
        water += max(0, min(left, right) - walls[i])
    return water
