#!/usr/bin/env python
'''
Leetcode: Search a 2D Matrix
Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:
    (1) Integers in each row are sorted from left to right.
    (2) The first integer of each row is greater than the last integer of the previous row.
For example,
Consider the following matrix:
[
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
http://leetcode.com/2010/10/searching-2d-sorted-matrix.html
http://leetcode.com/2010/10/searching-2d-sorted-matrix-part-ii.html
http://leetcode.com/2010/10/searching-2d-sorted-matrix-part-iii.html
'''
from __future__ import division
import random

# Solution#1
# O(m+n)
def search_matrix(M, val):
    m = len(M); n = len(M[0])
    i = 0; j = n-1
    while i < m and j >= 0:
        if M[i][j] == val: return val, (i, j)
        elif M[i][j] < val: i+=1
        else: j-=1
    return None

# Solution#2 Binary search
# O(log m + log n)
# Treat matrix as a one-dimensional array so we can do a binary search
# (i,j) --> index: im + j
def search_matrix_binary(M, val):
    m = len(M); n = len(M[0])
    i = 0; j = m*n-1
    while j >= i:
        mid = (i+j)//2
        x, y = divmod(mid, m)
        if M[x][y] == val: return val, (x,y)
        elif M[x][y] < val: i=mid+1
        else: j=mid-1
    return None

# Split the matrix into four small matrixs
# search in the one that the target that falls inside the range
# R1 | R2
# -------
# R3 | R4
# R1 min = (i_0, j_0), max = (i_mid-1, j_mid-1)
# R2 min = (i_0, j_mid), max = (i_mid-1, j_1)
# R3 min = (i_mid, j_0), max = (i_1, j_mid-1)
# R4 min = (i_mid, j_mid), max = (i_1, j_1)
def search_in_one_quad_matrix(M, val, i, j):
    print i, j
    if j[0] == j[1] and i[0] == i[1]:
        return M[i[0]][j[0]] == val
    if j[0] > j[1] and i[0] > i[1]:
        return False
    
    mid_i = (i[0]+i[1]+1)//2
    mid_j = (j[0]+j[1]+1)//2
    for a,b,c,d in [(i[0],j[0],mid_i-1,mid_j-1), \
                    (i[0],mid_j,mid_i-1,j[1]), \
                    (mid_i,j[0],i[1],mid_j-1), \
                    (mid_i,mid_j,i[1],j[1])]:
        if M[a][b] <= val <= M[c][d]:
            #print 'search_in_one_quad_matrix(M, val', '(',a,c,')', '(',b,d,') )'
            return search_in_one_quad_matrix(M, val, (a,c), (b,d))
    return False


# Solution#3 Search in 1/4 sub-matrix
# T(n) = T(n/4) + C
# ~ O(log n)
def search_matrix_quad(M, val):
    m = len(M); n = len(M[0])
    i = (0,m-1); j = (0,n-1)
    return search_in_one_quad_matrix(M, val, i, j)


if __name__ == '__main__':
    M = [[1, 3, 5, 7],
         [10, 11, 16, 20],
         [23, 30, 34, 50],
         [51, 100, 200, 300]
        ]
    print search_matrix(M,11)
    print search_matrix(M,150)
    
    print search_matrix_quad(M,11)
    print search_matrix_quad(M,150)
    

