#!/usr/bin/env python
'''
Leetcode: Maximal Rectangle
Given a 2D binary matrix filled with 0's and 1's, find the largest rectangle containing all ones and return its area.
'''
from __future__ import division
import random
from collections import defaultdict


def print_matrix(A, rows, cols):
    for i in range(rows):
        for j in range(cols):
            print A[i,j],
        print


# (1) Populate a table H for max length of vertical 1's. For each H[i,j], it is the maximum length of vertically continuous 1's ended at M[i][j], i.e. H[i,j] = k, meaning that M[i][j-k+1 .. j] are all 1's.
# (2) Apply histogram algorithm on each row to find the maximum rectangle in the row.
def max_rect(M):
    rows = len(M)
    cols = len(M[0])
    H = {}
    for j in range(cols):
        cont_one = 0
        for i in range(rows):
            cont_one = cont_one+1 if M[i][j] == 1 else 0
            H[i,j] = cont_one
    print "Vertical one's matrix:"
    print_matrix(H, rows, cols)
    
    # Find max rectangle under histogram in each row
    # x_1, x_2, ..., x_j --> maximize min{x_k, x_k+1, ..., x_k+n-1}*n
    # S(i) = the max rectangle that contains ai with ai as height,
    # maximum width of rectangle including that bar will be L+R+1, where:
    # L is number of adjacent bars to the left of ith bar and height greater than or 
    # equal to h(i). 
    # R is number of adjacent bars to the right of ith bar and height greater than or 
    # equal to h(i).
    max_area = 0
    for i in range(rows):
        # scan i-th row:
        S = dict((j, H[i,j]) for j in range(cols))
        # left --> right
        stack = []
        for j in xrange(cols):
            while stack and H[i,stack[-1]] >= H[i,j]:
                stack.pop() # extend to the left
            start = stack[-1]+1 if stack else 0
            S[j] += (j-start)*H[i,j]
            stack.append(j)
        
        # right --> left
        stack = []
        for j in reversed(xrange(cols)):
            while stack or H[i,stack[-1]] >= H[i,j]:
                stack.pop(j) # extend to the right
            end = stack[-1]-1 if stack else cols-1
            S[j] += (end-j)*H[i,j]
            stack.append(j)
        
        # Get max of this row
        print str(i)+'-th row:', [S[j] for j in range(cols)]
        max_area = max(max_area, max(S.values()))
    
    print max_area
    return max_area




if __name__ == '__main__':
    M = [[0,0,1,1,1,0,1],
         [1,0,1,1,1,1,1],
         [0,0,1,1,1,0,1],
         [1,1,1,0,1,1,1],
         [0,0,0,1,1,1,1]
        ]
    print '\n'.join(map(str,M))
    max_rect(M)



