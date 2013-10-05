#!/usr/bin/env python
'''
Leetcode: Insert Interval.
Given a set of [[[non-overlapping]]] intervals, insert a new interval into the intervals (merge if necessary). You may assume that the intervals were initially sorted according to their start times.
Example 1: Given intervals [1,3],[6,9], insert and merge [2,5] in as [1,5],[6,9].
Example 2: Given [1,2],[3,5],[6,7],[8,10],[12,16], insert and merge [4,9] in as [1,2],[3,10],[12,16]. This is because the new interval [4,9] overlaps with [3,5],[6,7],[8,10].
'''
from __future__ import division
import random

# interval tree? segment tree?

# [1,3],[6,9] --> index 
# [-inf. 1)->0; [1,3]->1; (3,6)->2; [6,9]->3; (9,inf.)->4
def insert_interval(intvs, new_intv):
    left, right = new_intv
    ret_intvs = []
    new_intv_inserted = False
    for a,b in intvs:
        if left > b: # not overlap at all
            ret_intvs.append([a,b])
        elif right < a:
            if not new_intv_inserted: # not overlap at all
                ret_intvs.append([left,right])
                new_intv_inserted = True
            ret_intvs.append([a,b])
        else:
            # starting/ending point in the interval
            if a <= left <= b: left = a
            if a <= right <= b: right = b
    # leftover
    if not new_intv_inserted:
        ret_intvs.append([left,right])
    return ret_intvs


## in-place
def insert_interval2(intvs, new_intv):
    intvs = sorted(intvs, key=lambda x:x[0])
    i = 0
    while i < len(intvs):
        cur = intvs[i]
        if new_intv[1] < cur[0] or new_intv[0] > cur[1]:
            i += 1
        else:
            left = min(cur[0], new_intv[0])
            right = max(cur[1], new_intv[1])
            new_intv = [left, right]
            del intvs[i]
    intvs.append(new_intv)
    return intvs


if __name__ == '__main__':
    intvs = [[1,2],[3,5],[6,7],[8,10],[12,16]]; new_intv = [4,9]
    print insert_interval2(intvs, new_intv)
    
    intvs = [[1,10],[12,16]]; new_intv = [2,8]
    print insert_interval2(intvs, new_intv)
    
    intvs = [[1,10],[12,16]]; new_intv = [-5,0]
    print insert_interval2(intvs, new_intv)
    
    intvs = [[1,10],[12,16]]; new_intv = [20,20]
    print insert_interval2(intvs, new_intv)


