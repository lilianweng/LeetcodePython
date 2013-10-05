#!/usr/bin/env python
'''
Leetcode: Distinct Subsequences

Given a string S and a string T, count the number of distinct subsequences of T in S. A subsequence of a string is a new string which is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (ie, "ACE" is a subsequence of "ABCDE" while "AEC" is not).
Here is an example: 
    S = "rabbbit", T = "rabbit"
    Return 3.
ra[b]bbit
rab[b]bit
rabb[b]it
'''
from __future__ import division
import random

# DP: 
# f(i,j) = #distinct subsequences of S[:i] and T[:j]
# f(i,j) = f(i-1,j) if not use S[i-1]
# f(i,j) = f(i-1,j-1) if S[i-1] == T[j-1] and use S[i-1]
# Thus, f(i,j) = f(i-1,j) + (S[i-1] == T[j-1])*f(i-1,j-1)
def distinct_subseq(S, T):
    n=len(S); m=len(T)
    W = {}
    # Initialization
    for i in range(n+1): W[0] = 1 # if T is empty
    for j in range(1, m+1): W[j] = 0 # if S is empty but T is not.
    for i in range(1, n+1):
        for j in range(1, m+1):
            # W[j] --> short for W[i,j]
            W[j] += W[j-1]*(S[i-1]==T[j-1])
    return W[m]


# DP: Let f(i,j) to be the number of distinct subsequences of T(j:) in S(i:). 
# Consider the ith character in S:
# If we can use it to match T[j], namely S[i] == T[j], then f(i,j) = f(i+1,j+1).
# If we do not want use it in our matching, then f(i,j) = f(i+1,j).
# Thus, f(i,j) = f(i+1,j) + (S[i] == T[j])*f(i+1,j+1)
# It is very much the same as how we solve C(n, m) or the knapsack problem.
def distinct_subseq2(S, T):
    m = len(S); n = len(T)
    f = dict((j,0) for j in range(n+1))
    f[n] = 1
    for i in reversed(xrange(m)):
        for j in xrange(n):
            f[j] += (S[i] == T[j])*f[j+1]
    return f[0]


if __name__ == '__main__':
    print distinct_subseq("rabbbit", "rabbit")


