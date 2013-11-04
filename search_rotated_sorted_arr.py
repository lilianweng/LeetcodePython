#!/usr/bin/env python
'''
Leetcode: Search in Rotated Sorted Array
Leetcode: Search in Rotated Sorted Array II
http://leetcode.com/2010/04/searching-element-in-rotated-array.html
'''
from __future__ import division
import random


'''
Suppose a sorted array is rotated at some pivot unknown to you beforehand.
(i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).
You are given a target value to search. 
If found in the array return its index, otherwise return -1.
You may assume no duplicate exists in the array.
'''
# modified binary search, O(logn)
# Search in L[i:j]
def search_rotated_arr(L, val):
    l = 0; r = len(L)-1
    while l <= r:
        mid = (l + r + 1)//2
        if L[mid] == val: return mid
        if L[l] <= L[mid]:
            # the lower half is sorted
            if L[l] <= val <= L[mid]: r = mid-1
            else: l = mid+1
        else:
            # the upper half is sorted
            if L[mid] <= val <= L[r]: l = mid+1
            else: r = mid-1
    return -1


def find_rotated_pivot(L):
    l = 0; r = len(L)-1
    while L[l] > L[r]:
        mid = (l + r + 1)//2
        if L[mid] > L[r]: l = mid+1
        else: r = mid
    return l

'''
What if duplicates are allowed?
Would this affect the run-time complexity? How and why?
Write a function to determine if a given target is in the array.
'''
def search_rotated_arr2(L, val, i, j):
    #print L[i:j]
    if i == j-1:
        return L[i] == val
    elif i >= j-1:
        return False
    else:
        mid = (i+j)//2
        if L[mid] == val: return True
        lower = upper = False
        if (L[i] >= L[mid]) or (val < L[mid]):
            lower = search_rotated_arr2(L, val, i, mid)
        if (L[mid] >= L[j-1]) or (L[mid] < val):
            upper = search_rotated_arr2(L, val, mid, j)
        return lower or upper


if __name__ == '__main__':
    print search_rotated_arr([4,5,6,7,0,1,2], 6, 0, 7)
    print search_rotated_arr([4,5,6,7,0,1,2], 0, 0, 7)
    print search_rotated_arr([4,5,6,7,0,1,2], 3, 0, 7)
    print
    print search_rotated_arr2([4,5,7,0,1,2,4,4], 7, 0, 8)
    print search_rotated_arr2([4,5,6,7,0,0,1,2], 0, 0, 8)
    print search_rotated_arr2([4,4,4,4,5,2], 3, 0, 6)


