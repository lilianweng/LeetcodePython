#!/usr/bin/env python
'''
Leetcode: Maximum Subarray
Find the contiguous subarray within an array (containing at least 
one number) which has the largest sum.
For example, given the array [-2,1,-3,4,-1,2,1,-5,4], 

'''
from __future__ import division
import random

# form S[i] = sum(A[0],...A[i])
# maximize |S[j] - S[i]| where j > i
def max_subarray(A):
    n = len(A)
    S = [A[0]]*n
    for i in range(1,n): S[i] = S[i-1] + A[i]
    print 'S:', S
    i = 0; j = n-1
    max_sum = None
    run = 0
    while j >= i:
        max_sum = max(max_sum, S[j] - S[i])
        # move one step at one time.
        if run % 2 == 0: i += 1
        else: j -= 1
        run += 1
    return max_sum


''' More practice: If you have figured out the O(n) solution, 
try coding another solution using the divide and conquer approach, 
which is more subtle.'''
# DP: S[i] = max sum of subarray ending at A[i]
def max_subarray_DP(A):
    S = {}
    S[0] = A[0]
    for i in range(1, len(A)):
        S[i] = max(A[i], S[i-1]+A[i])
    return max(S.values())


if __name__ == '__main__':
    print max_subarray([-2,1,-3,4,-1,2,1,-5,4])
    print max_subarray_DP([-2,1,-3,4,-1,2,1,-5,4])
    print max_subarray([0,0,0,0])
    print max_subarray_DP([0,0,0,0])





