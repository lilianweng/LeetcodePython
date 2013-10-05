#!/usr/bin/env python
'''
Leetcode: First missing positive
Given an unsorted integer array, find the first missing positive integer.
For example,
Given [1,2,0] return 3,
and [3,4,-1,1] return 2.

Your algorithm should run in O(n) time and uses constant space.
'''
from __future__ import division
import random

## Use bitmap
def first_miss_pos(L):
    bitmap = 0
    for x in L:
        if x <= 0: continue
        bitmap |= (1 << (x-1))
    print L, bin(bitmap)
    pos = 0
    while bitmap > 0:
        bitmap,r = divmod(bitmap, 2)
        pos += 1
        if r == 0: return pos
    return pos+1


## Switch x to pos x, amortized time ~O(n)
def first_miss_pos2(L):
    n = len(L)
    print L, '-->',
    for i in range(len(L)):
        while L[i] > 0 and L[i] < n and L[i] != L[L[i]]:
            # switch tmp to postition tmp if it is valid (1 to n-1)
            tmp = L[i]
            L[i] = L[tmp]
            L[tmp] = tmp
        if L[i] >= n: L[i] = -1
    
    print L
    for i in range(1,n):
        if L[i] < 0: return i
    return n


if __name__ == '__main__':
    print first_miss_pos2([1,2,0])
    print first_miss_pos2([1,2,3])
    print first_miss_pos2([3,4,-1,1])


