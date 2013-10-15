#!/usr/bin/env python
'''
Leetcode: Valid Sudoku
Determine if a Sudoku is valid, according to: Sudoku Puzzles - The Rules.
The Sudoku board could be partially filled, where empty cells are filled with the character '.'.
A partially filled sudoku which is valid.
'''
from __future__ import division
import random

INVALID = '.'

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


# whether the sudoku is valid
def is_valid_sudoku(M):
    N = 9
    assert len(M) == N and len(M[0]) == N
    # row; no repetition between 0~9.
    for i in range(N):
        if not valid_array(M[i]):
            return False
    # col
    for j in range(N):
        if not valid_array([M[i][j] for i in range(N)]):
            return False
    
    # 3x3 cells
    for x in range(0,9,3):
        for y in range(0,9,3):
            A = [M[i][j] for i in range(x,x+3) for j in range(y,y+3)]
            if not valid_array(A):
                return False
    return True


def valid_array(A):
    if len(set(A)) == len(A) and min(A) >= 1 and max(A) <= 9: return True
    return False


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
    print check_conflict(M, 0, 2, 4)
    print check_conflict(M, 5, 3, 9)
    print check_conflict(M, 8, 6, 5)


