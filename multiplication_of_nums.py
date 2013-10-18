#!/usr/bin/env python
'''
Leetcode: There is an array A[N] of N numbers. You have to compose an array Output[N] such that Output[i] will be equal to multiplication of all the elements of A[N] except A[i]. Solve it without division operator and in O(n).

For example Output[0] will be multiplication of A[1] to A[N-1] and Output[1] will be multiplication of A[0] and from A[2] to A[N-1].
http://leetcode.com/2010/04/multiplication-of-numbers.html
'''
from __future__ import division
import random


def multi_of_nums(A):
    n = len(A)
    L = [1]*n
    R = [1]*n
    for i in range(n-1):
        L[i+1] = L[i]*A[i]
    for i in range(n-1,0,-1):
        R[i-1] = R[i]*A[i]
    ret = [L[i]*R[i] for i in range(n)]
    print ret
    return ret


if __name__ == '__main__':
    multi_of_nums([4,3,2,1,2,3])


