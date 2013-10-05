#!/usr/bin/env python
'''
Leetcode: Set Matrix Zeroes
Given a m x n matrix, if an element is 0, set its entire row and column to 0. 
Do it in place.
Did you use extra space?
A straight forward solution using O(mn) space is probably a bad idea.
A simple improvement uses O(m + n) space, but still not the best solution.
Could you devise a constant space solution?
'''
from __future__ import division
import random


# O(1) in space
# use the first row and column as a buffer
def set_matrix_zeros(M):
    m = len(M); n = len(M[0])
    first_row_zero = first_col_zero = False
    # find zeros in first row/column
    for i in range(m):
        if M[i][0] == 0:
            first_col_zero = True
            break
    for j in range(n):
        if M[0][j] == 0:
            first_row_zero = True
            break
    # record zeros in other places
    for i in range(1,m):
        for j in range(1,n):
            if M[i][j] == 0:
                M[0][j] = 0
                M[i][0] = 0
    # set zeros
    for i in range(m):
        if M[i][0] == 0:
            for j in range(1,n):
                M[i][j] = 0
    for j in range(n):
        if M[0][j] == 0:
            for i in range(1,m):
                M[i][j] = 0
    
    print '\n'.join(map(str,M))


if __name__ == '__main__':
    
    M = [[2,5,2,1,3,6,7],
         [1,2,1,4,1,0,1],
         [7,5,10,1,4,8,2],
         [1,1,12,5,1,1,2],
         [4,0,2,5,1,2,1],
         [3,10,1,4,1,5,9],
         [3,5,101,11,4,8,2]
        ]
    print '\n'.join(map(str,M)), '\n'
    set_matrix_zeros(M)
    
    

