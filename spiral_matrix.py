#!/usr/bin/env python
'''
http://leetcode.com/2010/05/printing-matrix-in-spiral-order.html
'''

from __future__ import division
import random


'''
Leetcode: Spiral Matrix
Given a matrix of m x n elements (m rows, n columns), return all elements of the matrix in spiral order.
For example, Given the following matrix:
    [
     [ 1, 2, 3 ],
     [ 4, 5, 6 ],
     [ 7, 8, 9 ]
    ]
You should return [1,2,3,6,9,8,7,4,5].
'''
# Each circle starts at (i,i)
# (i,i)   -----> (i,m-1-i)
#    ^               |
#    |               v
# (n-1-i,i) <--- (n-1-i,m-1-i)
def spiral_matrix_traversal(M):
    rets = []
    m = len(M); n = len(M[0])
    for i in range(min(m,n)//2):
        # starting point (i,i)
        x,y = i,i
        # Those -1 or +1 are tricky; avoid duplication
        for y in range(i,n-i): rets.append(M[x][y])
        for x in range(i+1,m-i): rets.append(M[x][y])
        for y in reversed(range(i,n-i-1)): rets.append(M[x][y])
        for x in reversed(range(i+1,m-i-1)): rets.append(M[x][y])
    print rets
    return rets


'''
Leetcode: Spiral Matrix II
Given an integer n, generate a square matrix filled with elements from 1 to n2 in spiral order.
For example, Given n = 3,
You should return the following matrix:
    [
     [ 1, 2, 3 ],
     [ 8, 9, 4 ],
     [ 7, 6, 5 ]
    ]
'''
def spiral_matrix_print(n):
    # initialize
    M = [[0 for j in range(n)] for i in range(n)]
    cur = 1
    for i in range(n//2+1):
        # starting point (i,i)
        x,y = i,i
        # Those -1 or +1 are tricky; avoid duplication
        for y in range(i,n-i): M[x][y] = cur; cur += 1
        for x in range(i+1,n-i): M[x][y] = cur; cur += 1
        for y in reversed(range(i,n-i-1)): M[x][y] = cur; cur += 1
        for x in reversed(range(i+1,n-i-1)): M[x][y] = cur; cur += 1
    
    print '\n'.join(map(str,M)), '\n'
    return M


if __name__ == '__main__':
    M = [[1,2,3,4,5],
        [6,7,8,9,10],
        [11,12,13,14,15],
        [16,17,18,19,20]]
    #print '\n'.join(map(str,M))
    #spiral_matrix_traversal(M)
    spiral_matrix_print(3)
    spiral_matrix_print(5)
    spiral_matrix_print(6)


