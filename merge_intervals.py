#!/usr/bin/env python
'''
Leetcode: Merge Intervals
Given a collection of intervals, merge all overlapping intervals.
For example,
Given [1,3],[2,6],[8,10],[15,18],
return [1,6],[8,10],[15,18].
'''
from __future__ import division
import random


def is_overlapped(intv1, intv2):
    return intv2[0]<=intv1[0]<=intv2[1] or intv2[0]<=intv1[1]<=intv2[1]


def merged_intv(intv1, intv2):
    return [min(intv1[0], intv2[0]), max(intv1[1], intv2[1])]


# Naive:
# start from the first interval and compare it with all other intervals for overlapping, if it overlaps with any other interval, then remove the other interval from list and merge the other into the first interval. 
# Repeat the same steps for remaining intervals after first. 
# O(n^2)
def merge_intervals(intvs):
    merged_intvs = []
    i = 0
    while i < len(intvs):
        cur = intvs[i]
        merged_indices = []
        for j in range(i+1, len(intvs)): # compared with other intervals
            other = intvs[j]
            if is_overlapped(cur, other):
                # has overlapping
                merged = merged_intv(cur, other)
                intvs[i] = merged
                cur = merged
                merged_indices.append(j)
        
        if merged_indices:
            # the current interval is changed!
            for idx in sorted(merged_indices, reverse=True):
                del intvs[idx]
            #print 'remove', merged_indices, intvs
        else:
            i += 1
    
    print intvs
    return intvs


# Sorted it first based on the starting element
# if intvs[i] doesn't overlap with intvs[i-1], then intvs[i+1] cannot overlap with intvs[i-1] because intvs[i+1][0] >= intvs[i][0]. 
# O(nlogn + n)
def merge_intervals2(intvs):
    intvs = sorted(intvs, key=lambda x:x[0])
    stack = []
    for intv in intvs:
        if (not stack) or (not is_overlapped(intv, stack[-1])):
            stack.append(intv)
        else:
            other = stack.pop()
            merged = merged_intv(other, intv)
            stack.append(merged)
    print stack
    return stack


if __name__ == '__main__':
    merge_intervals([[1,3],[8,10],[2,6],[15,18],[15,18]])
    merge_intervals([[1,3],[8,11],[15,18],[2,9],[18,20]])
    merge_intervals([[1,1],[0,0],[1,1],[0,0]])
    
    merge_intervals2([[1,3],[8,10],[2,6],[15,18],[15,18]])
    merge_intervals2([[1,3],[8,11],[15,18],[2,9],[18,20]])
    merge_intervals2([[1,1],[0,0],[1,1],[0,0]])



