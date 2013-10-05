#!/usr/bin/env python

from __future__ import division
import random


'''
Leetcode: Merge Two Sorted Lists
Merge two sorted linked lists and return it as a new list. The new list should be made by splicing together the nodes of the first two lists. '''
# O(n+m)
def merge_two(A, B):
    merged = []
    m = len(A); n = len(B)
    i = j = -1
    while True:
        if (j >= n-1) or (i+1 <= m-1 and A[i+1] <= B[j+1]):
            # go one step on list A
            i += 1
            merged.append(A[i])
        else:
            j += 1
            merged.append(B[j])
        if i == m-1 and j == n-1:
            break
    print A, B, '-->', merged
    return merged


'''
Leetcode: Merge k Sorted Lists
Merge k sorted linked lists and return it as one sorted list. Analyze and describe its complexity. '''
# O(kn)
def merge_k(Ls):
    merged = []
    k = len(Ls)
    frontiers = dict((i, -1) for i in range(k))
    final_length = sum([len(l) for l in Ls])
    print 'final length:', final_length
    while True:
        next = None
        for i in range(k):
            j = frontiers[i]
            if j >= len(Ls[i])-1: continue # has reached the last element
            if (next is None) or (Ls[i][j+1] < Ls[next][frontiers[next]+1]):
                next = i
        frontiers[next] += 1
        merged.append( Ls[next][frontiers[next]] )
        if len(merged) == final_length: break
    
    print Ls, '-->', merged
    return merged


'''
Leetcode: Merge Sorted Array
Given two sorted integer arrays A and B, merge B into A as one sorted array.
Note: You may assume that A has enough space to hold additional elements from B. The number of elements initialized in A and B are m and n respectively. '''
def merge_two_into_one(A, B):
    merged = []
    m = len(A); n = len(B)
    A += [0]*n
    while n > 0:
        if m <= 0 or A[m-1] < B[n-1]:
            n -= 1
            A[n+m] = B[n]
        else:
            m -= 1
            A[n+m] = A[m]
    print B, 'merged into:', A
    return merged



if __name__ == '__main__':
    merge_two([1,3,5,7], [2,3,4,5,6,7])
    merge_two([4,5,6,7,8,9,10], [1,2,3])
    merge_two([1,1,1,1], [2,2,2,2])
    merge_two([0],[0,0])
    print
    merge_k([[1,3,5,7], [2,3,4,5,6,7], [4,5,6,7,8,9,10], [1,2,3]])
    merge_k([[1,1,1,1], [2,2,2,2],[0],[0,0],[-1,2,3]])
    print
    merge_two_into_one([1,3,5,7], [2,3,4,5,6,7])
    merge_two_into_one([4,5,6,7,8,9,10], [1,2,3])
    merge_two_into_one([1,1,1,1], [2,2,2,2])
    merge_two_into_one([0],[0,0])

