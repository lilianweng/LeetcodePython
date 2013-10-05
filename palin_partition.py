#!/usr/bin/env python

from __future__ import division
import math
from valid_palin import valid_palin

'''
Leetcode: Palindrome partition I
Given a string s, partition s such that every substring of the partition is a palindrome. Return all possible palindrome partitioning of s.

For example, given s = "aaba",
Return
  [
    ["a","a","b","a"],
    ["aa","b","a"],
    ["a","aba"]
  ]'''
memo_palin = {}
def palin_partition(s):
    global memo_palin
    n = len(s)
    if n == 0: yield []
    elif n == 1: yield [s]
    else:
        s = list(s)
        for i in range(n):
            first = s[:i+1]
            if first in memo_palin:
                # Use memotization to save time
                is_palin = memo_palin[first]
            else:
                is_palin = valid_palin(first)
                memo_pali[first] = is_palin
            if is_palin:
                for p in pali_partition(s[i+1:]):
                    yield [first_sub] + p


'''
Leetcode: Palindrome partition II
Given a string s, partition s such that every substring of the partition is a palindrome. Return the minimum cuts needed for a palindrome partitioning of s.

For example, given s = "aab",
Return 1 since the palindrome partitioning ["aa","b"] could be produced using 1 cut.
'''
memo_palin = {}
def palin_partition_min_cut(s):
    global memo_palin
    n = len(s)
    if n == 0: yield []
    elif n == 1: yield [s[0]]
    else:
        for i in range(n):
            first = s[:i+1]
            if first in memo_palin:
                # Use memotization to save time
                is_palin = memo_palin[first]
            else:
                is_palin = valid_palin(first)
                memo_palin[first] = is_palin
            if is_palin:
                min_cut = n-i
                min_p = None
                for p in palin_partition_min_cut(s[i+1:]):
                    if len(p) < min:
                        min_cut = len(p)
                        min_p = p
                yield [first] + min_p


# DP?
# palin(i,j) = True if s[i:j+1] is a palindrome
# palin(i,j) = s[i] == s[j] and (j-i<2 or palin(i+1,j-1))
# cut(j) = minimum cut on s[:j+1] to produce a palindrome partition
# cut(j) = min{cut(i-1)+1, cut(j)} if palin(i,j) == True
def palin_min_cut(s):
    n = len(s)
    # single letter is a palinfrom
    palin = dict(((i,i), True) for i in range(n))
    # cut between every consecutive letters
    cut = dict((i,i) for i in range(0,n))
    cut[-1] = 0
    for k in xrange(1,n-1):
        for i in xrange(n):
            j = i+k
            if j >= n: continue
            print i,j
            if s[i] == s[j] and (j-i < 2 or palin[(i+1,j-1)]):
                palin[(i,j)] = True
                cut[j] = min(cut[j], cut[i-1]+1)
            else:
                palin[(i,j)] = False
    return cut[n-1]-1


#################################################################
def is_palin(S):
    i = 0; j = len(S)-1
    while i <= len(S)-1 and j >= 0 and i < j:
        if S[i] == S[j]: i+=1; j -=1
        else: break
    return i >= j

#cut(i) = the min cut for palin partitioning of L[:i]
#cut(i) = min{cut(j)+1 (if L[j:i] is a palin for 0<=j<i), cut(i)}
def palin_min_cut(s):
    memo = {}
    cut = dict((i,i-1) for i in range(len(s)+1))
    for i in range(len(s)+1):
        for j in range(i):
            sub = s[j:i]
            is_p = memo[sub] if sub in memo else is_palin(sub)
            memo[sub] = is_p
            if is_p:
                cut[i] = min(cut[i], cut[j]+1)
    print cut


if __name__ == '__main__':
    
    for p in palin_partition('abaabaa'): print p
    
    
    