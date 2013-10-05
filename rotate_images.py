#!/usr/bin/env python
'''
Leetcode: Rotate Image
You are given an n x n 2D matrix representing an image.
Rotate the image by 90 degrees (clockwise).
Follow up: Could you do this in-place?
'''
from __future__ import division
import random

# rotate cell by cell
# (i,j) --> (j, n-1-i) --> (n-1-i,n-1-j) --> (n-1-j,i) --> (i,j)
def rotate_image(M):
    print '\n'.join(map(str,M)) + '\n'
    n = len(M)
    if n % 2 == 0: x = y = n//2
    else: x = n//2+1; y = n//2
    # the range part is tricky
    for i in range(x):
        for j in range(y):
            print (i,j),'->',(j, n-1-i),'->',(n-1-i,n-1-j),'->',(n-1-j,i)
            last = M[n-1-j][i]
            M[n-1-j][i] = M[n-1-i][n-1-j]
            M[n-1-i][n-1-j] = M[j][n-1-i]
            M[j][n-1-i] = M[i][j]
            M[i][j] = last
    print '\n'.join(map(str,M))
    return M


if __name__ == '__main__':
    M = [[2,0,2,1,3,0,7],
         [1,0,1,4,1,5,1],
         [0,5,10,1,4,8,2],
         [1,1,12,5,1,1,2],
         [4,6,0,5,1,2,1],
         [0,10,1,4,1,5,9],
         [0,5,101,11,4,8,2]
        ]
    rotate_image(M)
    print
    M = [[2,0,2],
         [1,0,1],
         [0,5,10]
        ]
    rotate_image(M)
    print
    M = [[1,2,3,4],
         [5,6,7,8],
         [9,10,11,12],
         [13,14,15,16]
        ]
    rotate_image(M)
