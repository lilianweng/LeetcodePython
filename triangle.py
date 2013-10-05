#!/usr/bin/env python
'''
Leetcode: Triangle
Given a triangle, find the minimum path sum from top to bottom. Each step you may move to adjacent numbers on the row below.
For example, given the following triangle
  [  [2],
    [3,4],
   [6,5,7],
  [4,1,8,3]]
The minimum path sum from top to bottom is 11 (i.e., 2 + 3 + 5 + 1 = 11).

Note: Bonus point if you are able to do this using only O(n) extra space, where n is the total number of rows in the triangle.
'''
from __future__ import division
import random

# S[i][j] = min{S[i-1][j-1], S[i-1][j]} + T[i][j]
# We only need to keep the record of the last row
# S[j] = min{S[j-1], S[j]} + T[i][j]
# top-down
def triangle(T):
    if not T: return 0
    S = [ T[0][0] ]
    for i in range(1,len(T)):
        print S
        newS = []
        for j in range(len(T[i])):
            if j == 0: newS.append( S[0] + T[i][j] )
            elif j == len(S): newS.append( S[len(S)-1] + T[i][j] )
            else: newS.append( min(S[j-1], S[j]) + T[i][j] )
        S = newS
    print newS
    return min(newS)


# More pretty code: bottom-up
def triangle2(T):
    if not T: return 0
    n = len(T)
    S = [0]*(n+1)
    while n >= 0:
        # There are n+1 elements on n-th row
        for i in range(0, n):
            S[i] = T[n-1][i] + min(S[i],S[i+1])
        n -= 1
    return S[0]


if __name__ == '__main__':
    T = [ [2],
          [3,4],
          [6,5,7],
          [4,1,8,3]]
    triangle2(T)


