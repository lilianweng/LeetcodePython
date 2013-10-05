#!/usr/bin/env python
'''
Leetcode: Interleaving String
Given s1, s2, s3, find whether s3 is formed by the interleaving of s1 and s2.
For example, Given:
s1 = "aa b c c",
s2 = "dbb ca",
When s3 = "aa d b b c bca c", return true.
When s3 = "aa dbb b accc", return false.
'''
from __future__ import division
import random

def interleaving(s1,s2,s3):
    if (s3 == '' and  s1 == '' and s2 == '') or (s1 == '' and s2 == s3) or (s2 == '' and s1 == s3):
        return True
    elif s1 == '' or s2 == '' or s3 == '':
        return False
    else:
        ch = s3[0]
        if ch == s1[0] and ch != s2[0]:
            return interleaving(s1[1:], s2, s3[1:])
        elif ch != s1[0] and ch == s2[0]:
            return interleaving(s1, s2[1:], s3[1:])
        elif ch == s1[0] and ch == s2[0]:
            return interleaving(s1, s2[1:], s3[1:]) or \
                   interleaving(s1[1:], s2, s3[1:])
        else:
            return False


# DP?
# I(i,j) = whether s3[:i+j] is an interleaving string of s1[:i] and s2[:j]
# I(i+1,j) = I(i,j) if s1[i] == s3[i+j]
# I(i,j+1) = I(i,j) if s2[i] == s3[i+j]
def interleaving_DP(s1, s2, s3):
    n, m = len(s1), len(s2)
    if len(s3) != n+m: return False
    I = {}
    I[0,0] = True
    for ij in range(1, n+m+1):
        for i in range(min(n+1, ij+1)):
            j = ij - i
            if j > m: continue
            I[i,j] = (i >= 1 and I[i-1,j] and (s1[i-1] == s3[ij-1])) or \
                     (j >= 1 and I[i,j-1] and (s2[j-1] == s3[ij-1]))
    return I[n,m]


if __name__ == '__main__':
    s1 = "aabcc"
    s2 = "dbbca"
    print interleaving(s1, s2, "aadbbcbcac"), interleaving_DP(s1, s2, "aadbbcbcac")
    print interleaving(s1, s2, "aadbbbaccc"), interleaving_DP(s1, s2, "aadbbbaccc")


