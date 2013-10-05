#!/usr/bin/env python
'''
Leetcode: Surrounded Regions
Given a 2D board containing 'X' and 'O', capture all regions surrounded by 'X'. A region is captured by flipping all 'O's into 'X's in that surrounded region .

For example,
X X X X
X O O X
X X O X
X O X X

After running your function, the board should be:
X X X X
X X X X
X X X X
X O X X
'''
from __future__ import division
import random

# Naive
# grow a set of 'O', add all neighboring 'O'
# flip it all 'O' in the set have neighbors.
# ~O(n^2+n)
def surrounded_region(M):
    m = len(M); n = len(M[0])
    # Detect all connected regions
    regions = []
    for i in range(m):
        for j in range(n):
            if M[i][j] == 'O':
                find_reg = False
                for reg in regions:
                    if (i+1,j) in reg or (i-1,j) in reg or (i,j-1) in reg or (i,j+1) in reg:
                        reg.add((i,j))
                        find_reg = True
                if not find_reg:
                    regions.append( set([(i,j)]) )
    
    # Scan all regions
    for reg in regions:
        surrounded = True
        for i,j in reg:
            if i==0 or i==m-1 or j==0 or j==n-1:
                # Any element is on the boundary
                surrounded = False
                break
        if surrounded:
            # replace 'O' with 'X'.
            for i,j in reg:
                M[i][j] = 'X'
    
    print '\n'.join(map(str,M)), '\n'
    return M


# Starting from 'O' on the boundary and flip all connected 'O' to 'T'
# Go through again flip everything other than 'T'-->'X' and flip 'T'-->'O'
# O(n)
def BFS_marker(M, i, j):
    m = len(M); n = len(M[0])
    # BFS uses queue; DFS uses stack
    queue = [(i,j)]
    while queue:
        x,y = queue.pop(0)
        M[x][y] = 'T'
        if x-1>=0 and M[x-1][y] == 'O': queue.append((x-1,y))
        if x+1<=m-1 and M[x+1][y] == 'O': queue.append((x+1,y))
        if y-1>=0 and M[x][y-1] == 'O': queue.append((x,y-1))
        if y+1<=n-1 and M[x][y+1] == 'O': queue.append((x,y+1))


def surrounded_region2(M):
    m = len(M); n = len(M[0])
    # BFS uses queue; DFS uses stack
    queue = []
    for i in range(m):
        if M[i][0] == 'O': BFS_marker(M,i,0)
        if M[i][n-1] == 'O': BFS_marker(M,i,n-1)
    for j in range(n):
        if M[0][j] == 'O': BFS_marker(M,0,j)
        if M[m-1][j] == 'O': BFS_marker(M,m-1,j)
    
    print '\n'.join(map(str,M)), '\n'
    
    for i in range(m):
        for j in range(n):
            if M[i][j] == 'T': M[i][j] = 'O'
            else: M[i][j] = 'X'
    
    print '\n'.join(map(str,M)), '\n'
    return M


if __name__ == '__main__':
    M = [['X','X','X','X','O','X'],
         ['X','O','O','X','X','X'],
         ['X','X','O','X','O','X'],
         ['X','O','X','O','O','O'],
         ['X','X','X','X','O','O']]
    print '\n'.join(map(str,M)), '\n'
    
    surrounded_region2(M)

