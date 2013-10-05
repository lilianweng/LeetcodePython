#!/usr/bin/env python

from __future__ import division
import random


'''
Leetcode: Unique Paths
A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below). The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below). How many possible unique paths are there?
Note: m and n will be at most 100.
'''
# i = 0,1,...,m-1; j = 0,1,...,n-1
# P(i,j) = P(i-1,j) + P(i,j-1)
# P(i,j) = C(i+j, i)
def uniq_paths(m,n):
    ret = 1
    # What is C(m+n-2, n-1)
    # m/1 * (m+1)/2 * ... * (m+n-2)/(n-1)
    for i in range(1,n):
        ret *= (m+i-1)/i
    return ret


'''
Leetcode: Unique Paths II
Now consider if some obstacles are added to the grids. How many unique paths would there be? An obstacle and empty space is marked as 1 and 0 respectively in the grid.
For example, There is one obstacle in the middle of a 3x3 grid as illustrated below.
[
  [0,0,0],
  [0,1,0],
  [0,0,0]
]
The total number of unique paths is 2.
Note: m and n will be at most 100.
'''
# P(i,j) = 0 if M[i][j] == 1
#          P(i-1,j) + P(i,j-1) otherwise
def uniq_paths_II(M):
    m = len(M); n = len(M[0])
    P = {}
    for i in range(m): P[i,0] = 1-M[i][0]
    for j in range(n): P[0,j] = 1-M[0][j]
    for i in range(1,m):
        for j in range(1,n):
            P[i,j] = (P[i-1,j]+P[i,j-1])*(1-M[i][j])
    
    for i in range(m):
        for j in range(n):
            print P[i,j],
        print
    
    return P[m-1,n-1]
    


if __name__ == '__main__':
    print uniq_paths(5,7)
    print uniq_paths(3,3)
    
    M = [[0,0,0,1,0,0],
         [0,1,0,0,0,1],
         [0,0,0,0,1,0],
         [1,0,0,0,0,0]]
    print '\n'.join(map(str,M)),'\n'
    uniq_paths_II(M)
    
    M = [[0,0,0],
         [0,1,0],
         [0,0,0]]
    print '\n'.join(map(str,M)),'\n'
    uniq_paths_II(M)

