#!/usr/bin/env python
'''
Leetcode: Sudoku Solver
Write a program to solve a Sudoku puzzle by filling the empty cells.
Empty cells are indicated by the character '.'.
You may assume that there will be only one unique solution.
'''
from __future__ import division
import sys

INVALID = 0

# fill in (x,y) with val@
def check_conflict(M, x, y, val):
    # column
    for i in range(9):
        if M[i][y] != INVALID:
            if M[i][y] == val:
                return True
    # row
    for j in range(9):
        if M[x][j] != INVALID:
            if M[x][j] == val:
                return True
    # cubes
    for i in range((x//3)*3, (x//3)*3+3):
        for j in range((y//3)*3, (x//3)*3+3):
            if M[i][j] != INVALID:
                if M[i][j] == val:
                    return True
    return False


def sudoku_fill_one(M, empty, rows, cols, cubes):
    print len(empty), 'to fill'
    # if no cell to fill
    if len(empty) == 0: return True
    i,j = empty[0]
    
    # need to fill in
    occupied = rows[i] | cols[j] | cubes[i//3,j//3]
    cands = set(range(1,10)) - occupied
    if not cands: return False
    
    for c in cands:
        #print 'Fill', c, 'in (%d,%d).' % (i,j)
        M[i][j] = c
        rows[i].add(c)
        cols[j].add(c)
        cubes[i//3,j//3].add(c)
        if sudoku_fill_one(M, empty[1:], rows, cols, cubes):
            return True
        # trace back
        M[i][j] = INVALID
        rows[i].remove(c)
        cols[j].remove(c)
        cubes[i//3,j//3].remove(c)


def sudoku_solver(M):
    # keep a set of elements for each row, column and cube
    # rows[i]
    rows = dict( \
              (i, set([M[i][j] for j in range(9) if M[i][j] != INVALID])) \
              for i in range(9))
    # cols[j]
    cols = dict( \
              (j, set([M[i][j] for i in range(9) if M[i][j] != INVALID])) \
              for j in range(9))
    # cubes[i//3, j//3]
    cubes = dict(\
              ((i,j), set([M[x][y] \
                      for x in range(i*3,i*3+3) \
                      for y in range(j*3,j*3+3) \
                      if M[x][y] != INVALID])\
              ) for i in range(3) for j in range(3))
    # empty cells
    empty = [(i,j) for i in range(9) for j in range(9) if M[i][j] == INVALID]
    
    print rows
    print cols
    print cubes
    print empty
    sudoku_fill_one(M, empty, rows, cols, cubes)
    print '\n'.join(map(str,M))


if __name__ == '__main__':
    M = [[5,3,0,0,7,0,0,0,0],
         [6,0,0,1,9,5,0,0,0],
         [0,9,8,0,0,0,0,6,0],
         [8,0,0,0,6,0,0,0,3],
         [4,0,0,8,0,3,0,0,1],
         [7,0,0,0,2,0,0,0,6],
         [0,6,0,0,0,0,2,8,0],
         [0,0,0,4,1,9,0,0,5],
         [0,0,0,0,8,0,0,7,9]]
    sudoku_solver(M)


