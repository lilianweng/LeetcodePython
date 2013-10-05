#!/usr/bin/env python
'''
Leetcode: Search Insert Position
Given a sorted array and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.
You may assume no duplicates in the array.
Here are few examples.
    [1,3,5,6], 5 --> 2
    [1,3,5,6], 2 --> 1
    [1,3,5,6], 7 --> 4
    [1,3,5,6], 0 --> 0
'''
from __future__ import division
import random

def search_insert_pos(L, val):
    l = 0; r = len(L)-1
    while l < r:
        mid = (l+r+1)//2
        if L[mid] == val: return mid
        elif L[mid] < val: l = mid+1
        else: r = mid-1
    return l if L[l] > val else l+1

if __name__ == '__main__':
    print search_insert_pos([1,3,5,6], 5)
    print search_insert_pos([1,3,5,6], 2)
    print search_insert_pos([1,3,5,6], 7)
    print search_insert_pos([1,3,5,6], 0)


