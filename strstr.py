#!/usr/bin/env python
'''
Leetcode: Implement strstr()
Returns a pointer to the first occurrence of needle in haystack, or null if needle is not part of haystack.
'''
from __future__ import division
import random

### KMP
def generate_overlap_table(P):
    n = len(P)
    overlap = {0:0}
    for i in range(1,n): # consider P[:i]
        ch = P[i] # current character in P
        v = overlap[i-1]
        while P[v+1] != ch and v != 0: # until overlap can be extended
            v = overlap[v] # find next largest pre-computed overlap
        if P[v+1] == c: overlap[k] = v+1
        else: overlap[k+1] = 0
    print 'overlap:', overlap
    return overlap

def KMP(T, P):
    j = 0
    overlap = generate_overlap_table(P)
    matched = []
    for i in range(len(T)):
        while True:
            if T[i] == P[j]:
                j += 1
                if j == len(P):
                    matched.append((i-len(P)+1, i))
                    j = overlap[j]
                break
            elif j == 0: break
            else: j = overlap[j]
    print matched
    return matched


### Boyer-Moore string search algorithm


### Rabin-Karp algorithm


def strstr(s, p):
    if not p: return 0
    for i in range(len(s)-len(p)+1):
        si = i; pi = 0
        while si < len(s) and pi < len(p) and s[si] == p[pi]:
            si += 1
            pi += 1
        if pi == len(p): return i
    return -1


if __name__ == '__main__':
    print strstr("xxxxyzabcdabcdefabc", "abc")




