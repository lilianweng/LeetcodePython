#!/usr/bin/env python
'''
Leetcode
Given a set of candidate numbers (C) and a target number (T), find all unique combinations in C where the candidate numbers sums to T. 
Note:
All numbers (including target) will be positive integers.
Elements in a combination (a1,a2,..,ak) must be in non-descending order. (ie, a1 <= a2 <= .. <= ak). The solution set must not contain duplicate combinations.
'''
from __future__ import division
import random


'''
The same repeated number may be chosen from C unlimited number of times.
For example, given candidate set 2,3,6,7 and target 7, a solution set is: 
    [7]
    [2, 2, 3]
'''
def comb_sum(C, k):
    if k == 0: yield []
    for x in C:
        if k >= x:
            for p in comb_sum(C, k-x):
                yield sorted([x] + p)


'''
Each number in C may only be used once in the combination.
For example, given candidate set 10,1,2,7,6,1,5 and target 8, 
A solution set is: 
[1, 7] 
[1, 2, 5] 
[2, 6] 
[1, 1, 6]
'''
def comb_sum2(C, k):
    if k == 0: yield []
    n = len(C)
    for i in range(n):
        if k >= C[i]:
            for p in comb_sum(C[:i]+C[i+1:], k-C[i]):
                yield sorted([C[i]] + p)


if __name__ == '__main__':
    c1 = set([",".join(map(str,p)) for p in comb_sum([2,3,6,7], 7)])
    c2 = set([",".join(map(str,p)) for p in comb_sum2([10,1,2,7,6,1,5], 8)])
    
    for p in c1: print p
    print
    for p in c2: print p
    print


