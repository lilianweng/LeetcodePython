#!/usr/bin/env python
'''
Leetcode: Container With Most Water
Given n non-negative integers a1, a2, ..., an, where each represents a point at coordinate (i, ai). n vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0). Find two lines, which together with x-axis forms a container, such that the container contains the most water.
Note: You may not slant the container.
'''
from __future__ import division
import random

# Find i < j to maximize (j-i)*min{ai, aj}, see 2sum
# O(n)
def container_water(a):
    i, j = 0, len(a)-1
    water = 0
    water_i = water_j = None
    while i < j:
        cur = (j-i)* min(a[i], a[j])
        if cur > water: water = cur; water_i = i; water_j = j
        if a[i] < a[j]: i += 1
        else: j -= 1
    print '(%d,%d): %d' % (water_i,water_j,water)
    return water


if __name__ == '__main__':
    a = [2,1,3,2,4,5,2,3,1,4]
    print container_water(a)