#!/usr/bin/env python
'''
Leetcode: Permutation Sequence
The set [1,2,3,...,n] contains a total of n! unique permutations.
By listing and labeling all of the permutations in order,
We get the following sequence (ie, for n = 3):
"123"
"132"
"213"
"231"
"312"
"321"
Given n and k, return the kth permutation sequence.
Note: Given n will be between 1 and 9 inclusive.
'''
from __future__ import division
import random

# k = 0,1,...,(n!-1)
def permu_seq(n, k):
    from math import factorial
    if k >= factorial(n): return ""
    digits = range(1,n+1)
    seq = []
    for _ in range(n):
        i, k = divmod(k, factorial(n-1))
        seq.append( digits[i] )
        digits.pop(i)
        n -= 1
    print seq
    return "".join(map(str,seq))


if __name__ == '__main__':
    permu_seq(3,3)
    permu_seq(5,55)


