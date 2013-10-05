#!/usr/bin/env python
'''
Leetcode: Longest Consecutive Sequence
Given an unsorted array of integers, find the length of the longest consecutive elements sequence.

For example, Given [100, 4, 200, 1, 3, 2], The longest consecutive elements sequence is [1, 2, 3, 4]. Return its length: 4.

Your algorithm should run in O(n) complexity.
'''
from __future__ import division
import random

# Using bitmap
def consecutive_seq(L):
    bitmap = 0
    for x in L: bitmap |= 1 << x
    max_len = cur_len = 0
    print bitmap, bin(bitmap)
    while bitmap > 0:
        bitmap, r = divmod(bitmap, 2)
        if r == 1:
            cur_len += 1
        else:
            max_len = max(max_len, cur_len)
            cur_len = 0
    return max_len


# Using extra space to merge seq
# Think as cluster merge, a single number is a length=1 cluster.
# Map lowest and highest to length. To merge two neighbor clusters, only need to update it's new lowest and highest, with new length.
# For every a[i], checking its neighbor a[i]-1 and a[i]+1 is enough.
def merge(seq, x, y):
    a, b = min(seq[x][0], seq[y][0]), max(seq[x][1], seq[y][1])
    seq[x] = [a,b]; seq[y] = [a,b]
    seq[a] = [a,b]; seq[b] = [a,b]
    return seq

def consecutive_seq2(L):
    seq = {} # mapping: x -> sequence [a,b] that contains x
    for x in L:
        if x in seq: continue
        seq[x] = [x,x]
        if x-1 in seq: seq = merge(seq, x, x-1)
        if x+1 in seq: seq = merge(seq, x, x+1)
    print seq
    return max([b-a+1 for a,b in seq.values()])


if __name__ == '__main__':
    print consecutive_seq2([4,10,8,200,1,3,30,5,12,3,1,2,2,7,70,6,9,9,11,18,16,19])


