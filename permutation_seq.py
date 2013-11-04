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
#from math import factorial

# k = 0,1,...,(n!-1)
def permu_seq(n, k):
    fact = 1
    for i in range(1,n+1):
        fact *= i
    if k >= fact: return ""
    
    digits = range(1,n+1)
    seq = []
    while n > 0:
        fact = int(fact/n)
        i, k = divmod(k, fact)
        seq.append( digits[i] )
        digits.pop(i)
        n -= 1
    print seq
    return "".join(map(str,seq))


if __name__ == '__main__':
    permu_seq(3,3)
    permu_seq(5,55)


