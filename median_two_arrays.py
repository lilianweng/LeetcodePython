#!/usr/bin/env python
'''
Leetcode: Median of Two Sorted Arrays
There are two sorted arrays A and B of size m and n respectively. Find the median of the two sorted arrays. The overall run time complexity should be O(log(m+n)).
'''
from __future__ import division
import random

def median_two_arrays(A, B):
    m, n = len(A), len(B)
    if (m+n) % 2 == 1:
        k1 = k2 = (m+n)//2
    else: 
        k1 = (m+n)//2 - 1
        k2 = (m+n)//2
    # print k1, k2
    i = j = -1 # starts with -1 not 0!!!
    medians = 0
    while i+j+1 < k2:
        # this condition is tricky:
        # B is not reaching the end
        # the next step on A is valid and 
        # the next step is the next larger element.
        if j+1 >= n or (i+1 <= m-1 and A[i+1] <= B[j+1]):
            # go one step on A
            i += 1
            # '+1' is tricky
            if i+j+1 == k1: medians += A[i]
            if i+j+1 == k2: medians += A[i]
        else:
            j += 1
            if i+j+1 == k1: medians += B[j]
            if i+j+1 == k2: medians += B[j]
    print A, B, '-->', medians/2
    return medians/2


### use binary search
# http://leetcode.com/2011/03/median-of-two-sorted-arrays.html
# KEY: #elements being disposed from each array must be the same.
# ~O(logn + logm)
def median_two_arrays2(A, B):
    #print A, B, '--->',
    median = None
    while A and B and (len(A) > 2 or len(B) > 2):
        m = len(A); n = len(B)
        i = m//2
        j = n//2
        if A[i] <= B[j]:
            # Median is between [A[i], B[j]], so
            # we can ignore A's left part, A[0:i], length = i
            # we can ignore B's right part, B[j+1:n], length = n-j-1
            l, r = i, n-j-1
            ### THIS IS TRICKY!
            # '+1' helps include the medians in A & B.
            # when l == r, we can safely ignore current medians.
            k = min(l,r)+1 if l != r else min(l,r)
            A = A[k:]
            B = B[:-k]
        elif A[i] > B[j]:
            # Median is between [B[j], A[i]]
            l,r = j, m-i-1
            k = min(l,r)+1 if l != r else min(l,r)
            A = A[:-k]
            B = B[k:]
    
    if not A: median = median_one_array(B)
    elif not B: median = median_one_array(A)
    else: median = median_one_array(sorted(A+B))
    
    print median
    return median

def median_one_array(A):
    m = len(A)
    if m%2 == 1: return A[m//2]
    else: return (A[m//2-1]+A[m//2])/2



##########################################################
'''
Find kth smallest in two sorted arrays.
'''
def kth_two_arrays(A, B, k):
    k -= 1
    m, n = len(A), len(B)
    # print k1, k2
    i = j = -1 # starts with -1 not 0!!!
    while i+j+1 < k:
        print i,j
        if j+1 >= n or (i+1 <= m-1 and A[i+1] <= B[j+1]):
            # go one step on A
            i += 1
            if i+j+1 == k: return A[i] # '+1' is tricky
        else:
            j += 1
            if i+j+1 == k: return B[j]
    return None


# Using binary search
# If sum of mid indices of A and B < k
#    if A's mid > B's mid, we can ignore the first half of B, adjust k.
#    else ignore the first half of A, adjust k.
# Else if sum of mid indices of A and B > k:
#    if A's mid > B's mid, we can safely ignore second half of A
#    else we can ignore second half of B
def kth_two_arrays2(A,B,k):
    #print A, B, 'k:', k, '--->',
    kth = None
    while k > 1 and A and B:
        i = len(A)//2
        j = len(B)//2
        if i+j < k:
            # ignore the first half of the sequence with smaller mid element
            if A[i] >= B[j]:
                j = max(j,1)
                B = B[j:]
                k -= j
            else:
                i = max(i,1)
                A = A[i:]
                k -= i
        else:
            # ignore the second half of the sequence with larger mid element
            if A[i] >= B[j]:
                A = A[:i]
            else:
                B = B[:j]
    
    if k == 0: kth = min(A[0], B[0])
    else: kth = sorted(A+B)[k-1]
    
    return kth


if __name__ == '__main__':
    #median_two_arrays([3,5], [9,10])
    #median_two_arrays2([3,5], [9,10])
    print kth_two_arrays([3,5], [9,10],3)
    
    #median_two_arrays([1,3,5,7], [2,3,4,5,6,7])
    #median_two_arrays2([1,3,5,7], [2,3,4,5,6,7])
    print kth_two_arrays([1,3,5,7], [2,3,4,5,6,7],5)
    
    #median_two_arrays([4,5,6,7,8,9,10], [1,2,3])
    #median_two_arrays2([4,5,6,7,8,9,10], [1,2,3])
    #print kth_two_arrays([4,5,6,7,8,9,10], [1,2,3],7)
    
    #median_two_arrays([1,1,1,1], [2,2,2,2])
    #median_two_arrays2([1,1,1,1], [2,2,2,2])
    print kth_two_arrays([1,1,1,1], [2,2,2,2],5)
    
    #median_two_arrays([0],[0,0])
    #median_two_arrays2([0],[0,0])
    print kth_two_arrays([0],[0,0],1)
    

