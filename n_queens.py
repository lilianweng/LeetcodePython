#!/usr/bin/env python

from __future__ import division
import random


'''
Leetcode: N-Queens
The n-queens puzzle is the problem of placing n queens on an nxn chessboard such that no two queens attack each other.

Given an integer n, return all distinct solutions to the n-queens puzzle.
Each solution contains a distinct board configuration of the n-queens' placement, where 'Q' and '.' both indicate a queen and an empty space respectively.

For example,
There exist two distinct solutions to the 4-queens puzzle:
[
 [".Q..",  // Solution 1
  "...Q",
  "Q...",
  "..Q."],

 ["..Q.",  // Solution 2
  "Q...",
  "...Q",
  ".Q.."]
]'''


def translate_cols(cols, n):
    solutions = [
        ['.'*c+'Q'+'.'*(n-c-1) for c in col]
        for col in cols
    ]
    return solutions


def print_solutions(sols):
    for sol in sols:
        for row in sol:
            print row
        print


# Given the col positions, whether (i,j) conflicts with any existing queen
def check_conflict(cols, n, i, j):
    # check column
    if j in set(cols): return True
    # check diagonals
    x, y = i-1, j-1
    while x >= 0 and y >= 0:
        if cols[x] == y: return True
        x, y = x-1, y-1
    x, y = i-1, j+1
    while x >= 0 and y <= n-1:
        if cols[x] == y: return True
        x, y = x-1, y+1
    return False


# cols = [col_0, col_1, ..., col_n-1]
# Queen is put on row i, col prevs[i]
# Currently there are len(cols) row
def n_queens_place(cols, n, rets):
    if len(cols) == n:
        # has finished placing queens
        rets.append(cols)
    else:
        for j in range(n):
            if not check_conflict(cols, n, len(cols), j):
                n_queens_place(cols+[j], n, rets)


def n_queens(n):
    rets = []; cols = []
    n_queens_place(cols, n, rets)
    sols = translate_cols(rets, n)
    print_solutions(sols)
    print '#Solutions:', len(sols)


'''
Leetcode: N-Queens II
Follow up for N-Queens problem. Now, instead outputting board configurations, return the total number of distinct solutions.
http://www.matrix67.com/blog/archives/266
'''
# row, ld, rd are three bitmap showing which bits have been taken before

def n_queens2(n, row, ld, rd):
    global counter
    FULL = 1 << n - 1
    if row != FULL:
        pos = FULL & ~(row | ld | rd)
        #print bin(row), bin(ld), bin(rd), '-->', bin(pos)
        while pos > 0:
            # go through all non-zero digit
            p = pos & (~pos + 1)  # get the right-most 1.
            pos = pos - p         # remove the right-most available pos.
            n_queens2(n, row+p, (ld+p)<<1, (rd+p)>>1)
    else:
        counter += 1


if __name__ == '__main__':
    n = 12; counter = 0
    
    n_queens(n)
    n_queens2(n,0,0,0)
    print counter
