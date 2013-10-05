#!/usr/bin/env python
'''
Leetcode: Word Search
Given a 2D board and a word, find if the word exists in the grid.
The word can be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once.
For example,
    Given board =
    [
      ["ABCE"],
      ["SFCS"],
      ["ADEE"]
    ]
    word = "ABCCED", -> returns true,
    word = "SEE", -> returns true,
    word = "ABCB", -> returns false.
'''
from __future__ import division
import random

# start from i,j
def word_search_from_cell(M, word, i, j):
    if len(word) == 0:
        return True
    
    if i is not None and j is not None:
        cands = ((i+1,j), (i-1,j), (i,j+1), (i,j-1))
    else:
        cands = ((x,y) for x in range(len(M)) for y in range(len(M[0])))
    
    # (x,y) are adjacent cell to (i,j)
    for x,y in cands:
        if 0 <=x< len(M) and 0<=y<len(M[0]) and M[x][y] == word[0]:
            M[x][y] = '-'
            if word_search_from_cell(M, word[1:], x, y):
                return True
            M[x][y] = word[0]
    return False


def word_search(M, word):
    M2 = [list(row[0]) for row in M]
    print M2
    return word_search_from_cell(M2,word,None,None)


if __name__ == '__main__':
    M = [
      ["ABCE"],
      ["SFCS"],
      ["ADEE"]
    ]
    
    print word_search(M, "ABCCED")
    print word_search(M, "SEE")
    print word_search(M, "ABCB")
    


