#!/usr/bin/env python

from __future__ import division
import random

'''
Leetcode: Jump Game
Given an array of non-negative integers, you are initially positioned at the first index of the array. Each element in the array represents your *maximum* jump length at that position.
Determine if you are able to reach the last index.
For example:
A = [2,3,1,1,4], return true.
A = [3,2,1,0,4], return false.
'''
# DP
# R(i) = whether we can arrive at the last index from i-th element
# R(i) = R(i+1) or R(i+2) or ... or R(i+A[i])
# R(len(A)-1) = True
def jump_game(A):
    n = len(A)
    R = {n-1:True}
    for pos in reversed(xrange(n-1)):
        R[pos] = False
        for next_pos in range(pos+1, min(pos+A[pos]+1, n)):
            R[pos] |= R[next_pos]
    print R
    return R[0]


'''
Leetcode: Jump Game II
Your goal is to reach the last index in the minimum number of jumps.
For example:
Given array A = [2,3,1,1,4]
The minimum number of jumps to reach the last index is 2. (Jump 1 step from index 0 to 1, then 3 steps to the last index.)
'''
# DP
# R(i) = minimum #steps we can arrive at the last index from i-th element (-1/None means we cannot)
# R(i) = min{R(i+1) or R(i+2) or ... or R(i+A[i])} + 1
# R(len(A)-1) = 0
def jump_game2(A):
    n = len(A)
    R = {n-1:0}
    for pos in reversed(xrange(n-1)):
        R[pos] = None
        for next_pos in range(pos+1, min(pos+A[pos]+1, n)):
            # Note any number > None
            if (R[next_pos] >= 0) and \
               ((R[pos] is None) or (R[next_pos]+1 < R[pos])):
                R[pos] = R[next_pos] + 1
    print R
    return R[0]


if __name__ == '__main__':
    print jump_game2([2,3,1,1,4])
    print jump_game2([3,2,1,0,4])


