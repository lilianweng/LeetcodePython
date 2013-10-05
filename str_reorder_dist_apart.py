#!/usr/bin/env python
'''
Leetcode: Given a string of lowercase characters, reorder them such that the same characters are at least distance d from each other.
Input: { a, b, b }, distance = 2
Output: { b, a, b }
'''
from __future__ import division
import sys, random
from collections import defaultdict


# Greedy strategy: the character that has the most duplicates has the highest priority of being chosen to put in the new list. If that character cannot be chosen (due to the distance constraint), we go for the character that has the next highest priority. We also use some tables to improve the efficiency. (i.e., keeping track of # of duplicates of each character.)
def reorder(L, d):
    n = len(L)
    freq = defaultdict(int)
    newL = [None]*n
    for ch in L: freq[ch] += 1
    while freq:
        ch = max(freq, key=lambda x:freq[x])
        first = 0 # first available pos
        while newL[first] is not None: first += 1
        for i in range(freq[ch]):
            if first >= n: print 'Cannot!'; sys.exit(1)
            newL[first] = ch
            first += d
        del freq[ch]
    print L, newL
    return newL


if __name__ == '__main__':
    reorder(['a','a','b','b','c','b','b','b'], 2)


