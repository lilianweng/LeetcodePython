#!/usr/bin/env python
'''
Leetcode: Minimum Path Sum
Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right which minimizes the sum of all numbers along its path.
Note: You can only move either down or right at any point in time.
'''
from __future__ import division
import random

# DP: S(i,j) = min path sum from (0,0)-->(i,j)
# S(i,j) = min{S(i-1,j), S(i,j-1)} + M(i,j)
# ~ O(mn)
def min_path_sum(M):
    rows, cols = len(M), len(M[0])
    S = {}; prev = {}
    S[0,0] = M[0][0]
    prev[0,0] = None
    for i in range(1,rows):
        S[i,0] = S[i-1,0] + M[i][0]
        prev[i,0] = (i-1,0)
    for j in range(1,cols):
        S[0,j] = S[0,j-1] + M[0][j]
        prev[0,j] = (0,j-1)
    
    for i in range(1, rows):
        for j in range(1, cols):
            if S[i-1,j] < S[i,j-1]:
                S[i,j] = S[i-1,j] + M[i][j]
                prev[i,j] = (i-1, j)
            else:
                S[i,j] = S[i,j-1] + M[i][j]
                prev[i,j] = (i,j-1)
    paths = []
    step = (rows-1, cols-1)
    while step and step in prev:
        paths.insert(0, step)
        step = prev[step]
    print 'path:', '-->'.join(map(str,paths))
    print S[rows-1, cols-1]
    return paths


if __name__ == '__main__':
    M = [[2,0,2,1,3,0,7],
         [1,0,1,4,1,5,1],
         [0,5,10,1,4,8,2],
         [1,1,12,5,1,1,2],
         [4,6,0,5,1,2,1]
        ]
    print '\n'.join(map(str,M))
    min_path_sum(M)


