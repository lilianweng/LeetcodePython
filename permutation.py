#!/usr/bin/env python

from __future__ import division
import random


'''
Leetcode: Permutations
Given a collection of numbers, return all possible permutations.
For example,
[1,2,3] have the following permutations:
[1,2,3], [1,3,2], [2,1,3], [2,3,1], [3,1,2], and [3,2,1].
'''

'''
Leetcode: Permutations II
Given a collection of numbers that might contain duplicates, return all possible unique permutations.
For example,
[1,1,2] have the following unique permutations:
[1,1,2], [1,2,1], and [2,1,1]
'''

def gen_permu(L):
    n = len(L)
    if n == 0: yield []
    elif n == 1: yield L
    else:
        checked = set() # cache digit that has been put at this position
        for i in range(n):
            if L[i] in checked: continue
            checked.add(L[i])
            for p in gen_permu(L[:i] + L[i+1:]):
                yield [L[i]] + p


def permu(L):
    counter = 0
    for p in gen_permu(L):
        print p
        counter += 1
    print 'Total:', counter

if __name__ == '__main__':
    permu([1,2,3,4])
    print
    permu([1,1,2,3])


