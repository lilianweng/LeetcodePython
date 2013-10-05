#!/usr/bin/env python
''' 
Leetcode: Search for a Range
Given a sorted array of integers, find the starting and ending position of a given target value.
Your algorithm's runtime complexity must be in the order of O(log n).
If the target is not found in the array, return [-1, -1].
For example,
    Given [5, 7, 7, 8, 8, 10] and target value 8,
    return [3, 4].
'''
from __future__ import division
import random

# O(log n) in time.
# Search in L[i:j]
def binary_range_search(L, val, i, j):
    if L[i] == L[j-1] == val: return range(i,j)
    if i == j-1 and L[i] != val: return []
    if i > j-1: return []
    
    # L[i:mid], L[mid:j]
    mid = (i+j)//2
    lower = []; upper = []
    if val <= L[mid]:
        lower = binary_range_search(L, val, i, mid)
    if val >= L[mid]:
        upper = binary_range_search(L, val, mid, j)
    return lower + upper


def search_range(L, val):
    return binary_range_search(L, val, 0, len(L))


if __name__ == '__main__':
    print search_range([1,2,3,3,3,3,3,3,3,4,5,6,6,6,6,6,7], 3)
    print search_range([1,2,3,3,4,5,5,6,7,8,9], 3)
    print search_range([1,2,3], 3)
    print search_range([3], 3)
    print search_range([3,3,4,5], 3)


