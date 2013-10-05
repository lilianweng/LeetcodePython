#!/usr/bin/env python
'''
Leetcode: 3Sum Closest

Given an array S of n integers, find three integers in S such that the sum is closest to a given number, target. Return the sum of the three integers. You may assume that each input would have exactly one solution.

    For example, given array S = {-1 2 1 -4}, and target = 1.
    The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).

'''
from __future__ import division
import random

### DP? Given a list L
# S(i, k, target) = True if we can find k elements among L[:i] to sum up to target
# S(i, k, target) = S(i-1, k-1, target-L[i-1]) or S(i-1, k, target)
def sum_closest(L, num_k, target):
    import math
    n = len(L)
    S = {}
    prev = {}
    max_t = sum([x for x in L if x > 0])
    min_t = sum([x for x in L if x <= 0])
    print 'target range: [%d, %d]' %(min_t, max_t)
    
    # Initialization:
    # S(0,any,any) = False
    # S(any,0,any) = False
    # S(any,0,0) = True
    for i in range(n+1): 
        for t in range(min_t, max_t+1):
            S[(i,0,t)] = False
    for k in range(num_k+1):
        for t in range(min_t, max_t+1):
            S[(0,k,t)] = False
    for i in range(n+1):
        S[(i,0,0)] = True
    
    for i in range(1,n+1):
        for k in range(1,num_k+1):
            for t in range(min_t, max_t+1):
                with_elem = S[(i-1,k-1,t-L[i-1])] if min_t <= t-L[i-1] <= max_t else False
                without_elem = S[(i-1,k,t)]
                
                S[(i,k,t)] = with_elem or without_elem
                if with_elem: prev[(i,k,t)] = (i-1,k-1,t-L[i-1])
                elif without_elem: prev[(i,k,t)] = (i-1,k,t)
    
    # min{|t-target| for S[(n,num_k,t)] == True}
    cands = [t for t in range(min_t, max_t+1) if S[(n,num_k,t)]]
    output_t = min(cands, key=lambda x:math.fabs(x-target))
    
    # print out
    output = []
    i,k,t = n,num_k,output_t
    while (i,k,t) in prev:
        next_i,next_k,next_t = prev[(i,k,t)]
        if next_k == k-1: output.append(L[next_i])
        i,k,t = next_i,next_k,next_t
    print 'output:', output, 'sum(output):', sum(output)
    return output


if __name__ == '__main__':
    sum_closest([-1, 2, 1, -3, 6], 2, 2)


