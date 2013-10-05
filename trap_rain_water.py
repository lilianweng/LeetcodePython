#!/usr/bin/env python
'''
Leetcode: Trapping Rain Water
Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it is able to trap after raining.

For example, 
    Given [0,1,0,2,1,0,1,3,2,1,2,1], return 6.
    http://www.leetcode.com/wp-content/uploads/2012/08/rainwatertrap.png
'''
from __future__ import division
import random

# Naive
# For any i that L[i] > L[i+1], it can be a potential left bar.
# Try to find the first j > i and L[j] >= i, then i-->j is a container
def trap_water(L):
    n = len(L)
    water = 0
    i = 0
    while i < n-1:
        if L[i] > L[i+1]:
            # may be a left bar
            j = i+2
            while j < n and L[j] < L[i]: j += 1
            if j < n:
                water += (j-i-1)*L[i] - sum(L[i+1:j])
                i = j-1
        i += 1
    print water
    return water


# Try to use stack
# ~ O(n)
def trap_water_stack(L):
    stack = []
    water = 0
    for i in range(len(L)):
        if not stack or L[i] < L[stack[-1]]:
            # Push when empty stack or current element < stack top
            stack.append(i)
        else:
            prev = stack.pop()
            # When popping, add water whenever the left bar > right bar
            while stack and L[i] >= L[stack[-1]]:
                cur = stack.pop()
                if L[cur] > L[prev]:
                    w = (i-cur-1)*(L[cur]-L[prev])
                    water += w
                prev = cur
            stack.append(i)
    
    print water
    return water


### O(n) solution. for each bar, find the max height bar on the left and right. then for this bar it can hold min(max_left, max_right) - height
def trap_water_col(L):
    n = len(L)
    # find the max height on the left of each column
    maxL = {}
    cur_max = 0
    for i in xrange(n):
        maxL[i] = cur_max
        cur_max = max(cur_max, L[i])
    # find the max height on the right of each column
    maxR = {}
    cur_max = 0
    for i in reversed(xrange(n)):
        maxR[i] = cur_max
        cur_max = max(cur_max, L[i])
    water = 0
    for i in xrange(n):
        w = min(maxL[i], maxR[i]) - L[i]
        water += max(w, 0)
    print water
    return water


'''
What if water is trapped in 2-D matrix!
'''
### For each cell (i,j), the max water it can trap is:
### min height{max height of cells up/down/left/right} - heigh(i,j)
def trap_water_2D(M):
    m = len(M[0]); n = len(M)
    U, D, L, R = {}, {}, {}, {}
    # Max height of left and right cell for each entry
    for i in xrange(n):
        maxL = maxR = 0
        for j in xrange(m):
            L[i,j] = maxL
            maxL = max(maxL, M[i][j])
        for j in reversed(xrange(m)):
            R[i,j] = maxR
            maxR = max(maxR, M[i][j])
    # Max height of up/down-cell for each entry
    for j in xrange(m):
        maxU = maxD = 0
        for i in xrange(n):
            U[i,j] = maxU
            maxU = max(maxU, M[i][j])
        for i in reversed(xrange(n)):
            D[i,j] = maxD
            maxD = max(maxD, M[i][j])
    
    water = 0
    for i in xrange(n):
        for j in xrange(m):
            h = min(L[i,j], R[i,j], U[i,j], D[i,j])
            if h > M[i][j]: water += h-M[i][j]
    print water
    return water


if __name__ == '__main__':
    #trap_water([0,1,0,2,1,0,1,3,2,1,2,1,4,1])
    #trap_water_stack([0,1,0,2,1,0,1,3,2,1,2,1,4,1])
    #trap_water_col([0,1,0,2,1,0,1,3,2,1,2,1,4,1])
    
    M = [[2,2,2,1,1,1,1],
        [2,0,2,1,1,3,1],
        [2,2,2,1,3,0,3],
        [1,1,3,3,3,3,3],
        [1,1,1,1,1,1,1]]
    trap_water_2D(M)
    
