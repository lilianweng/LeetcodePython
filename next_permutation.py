#!/usr/bin/env python
'''
Leetcode: Next Permutation

Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers. If such arrangement is not possible, it must rearrange it as the lowest possible order (ie, sorted in ascending order).

Here are some examples. Inputs are in the left-hand column and its corresponding outputs are in the right-hand column.
1,2,3 -> 1,3,2
3,2,1 -> 1,2,3
1,1,5 -> 1,5,1

No extra memory!!!!
'''
from __future__ import division
import random

### scan from the last digit to find the first element < the left element.
# Example 1:
# 1,5,3,4,2 (find 3,4)
# 2,5,4,3,2 (switch 3,4)
# Example 2:
# 1,5,4,3,2,1,0 (find 1,5; the first element < the left element.)
# 1,5,4,3,2,1,0 (find 2, the first element that > 1 from the end)
# 2,5,4,3,1,1,0 (switch 1,2)
# 2,0,1,1,3,4,5 (reverse 5,4,3,1,1,0)
def next_permu(L):
    n = len(L)
    if n == 0: return []
    if n == 1: return L
    
    i = n - 2
    while i >= 0:
        if L[i] < L[i+1]: break
        i -=1
    # All elements are larger than the right element
    if i < 0: return L[::-1]
    
    j = n - 1
    while L[j] <= L[i]:
        j -= 1
    # Switch i-th and j-th elements
    L[i], L[j] = L[j], L[i]
    # Reverse L[i+1:]
    L = L[:i+1] + L[i+1:][::-1]
    return L


'''
Iteratively permute a string and print out lexicographically
O(1) in space.
'''
def iter_permutation(L):
    L = sorted(L)
    n = len(L)
    print L
    while True:
        i = n - 2
        # Find i-th element that < right element
        while i >= 0:
            if L[i] < L[i+1]: break
            i -=1
        # All elements are larger than the right element
        if i < 0: break
        
        j = n - 1
        while L[j] <= L[i]:
            j -= 1
        # Switch i-th and j-th elements
        L[i], L[j] = L[j], L[i]
        # Reverse L[i+1:]
        L = L[:i+1] + L[i+1:][::-1]
        print L



if __name__ == '__main__':
    next_permu([1,2,3,4])
    next_permu([9,9,9,8])
    next_permu([0,2,1,1])
    next_permu([2,3,1])
    next_permu([3,2,1])
    next_permu([1,5,3,4,2])
    next_permu([1,5,4,3,2])
    next_permu([1,5,4,3,2,1])


