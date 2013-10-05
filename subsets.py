#!/usr/bin/env python

from __future__ import division
import random


'''
Leetcode: Subsets
Given a set of distinct integers, S, return all possible subsets.
Note:
    Elements in a subset must be in non-descending order.
    The solution set must not contain duplicate subsets.
For example,
    If S = [1,2,3], a solution is:
[
  [3],
  [1],
  [2],
  [1,2,3],
  [1,3],
  [2,3],
  [1,2],
  []
]
'''
def subsets_generator(S):
    if len(S) == 1: yield S
    else:
        for i in range(len(S)):
            ch = S[i]
            yield [ch]
            if S[i+1:]:
                for other in subsets_generator(S[i+1:]):
                    yield [ch] + other


def subsets(S):
    print '\nSubsets of', S
    S = sorted(S)
    for sset in subsets_generator(S):
        print sset
    print []


def subsets_iter(S):
    print '\nSubsets of', S
    S = sorted(S)
    ss = []
    for ch in S:
        if ss:
            ss += [sset + [ch] for sset in ss]
        else:
            ss.append([])
            ss.append([ch])
    print ss
    return ss


'''
Leetcode: Subsets ||
Given a collection of integers that might contain duplicates, S, return all possible subsets.
Note:
    Elements in a subset must be in non-descending order.
    The solution set must not contain duplicate subsets.
For example,
    If S = [1,2,2], a solution is:
[
  [2],
  [1],
  [1,2,2],
  [2,2],
  [1,2],
  []
]
'''
def subsets2_generator(S):
    if len(S) == 1: yield S
    else:
        checked = set()
        for i in range(len(S)):
            ch = S[i]
            if ch in checked: continue
            checked.add(ch)
            yield [ch]
            if S[i+1:]:
                for other in subsets2_generator(S[i+1:]):
                    yield [ch] + other


def subsets2(S):
    print '\nSubsets of', S
    S = sorted(S)
    for sset in subsets_generator2(S):
        print sset
    print []


# interesting solution!
def subsets2_iter(S):
    print '\nSubsets of', S
    S = sorted(S)
    ss = [[]]
    start = 0
    for i in range(len(S)):
        cur_size = len(ss)
        for j in range(start, cur_size):
            sub = list(ss[j])
            sub.append(S[i])
            ss.append(sub)
        if i < len(S)-1 and S[i+1] == S[i]:
            # if next character is duplicated
            # only add it to the last few subarrays in the prev loop
            start = cur_size
        else:
            start = 0
    print ss
    return ss


## Print out all the subsets of an array without storing any subset.
## Index all the elements, and print out subsets according to binary numbers.
def subset_binary(L):
    n = len(L)
    for b in range(2**n):
        selected_indices = []
        i = 0
        while b > 0:
            b, bit = divmod(b, 2)
            if bit == 1: selected_indices.append(i)
            i += 1
        #print selected_indices
        yield [L[k] for k in selected_indices]


if __name__ == '__main__':
    '''
    subsets_iter([1,2,3])
    subsets_iter([10,1,4,3])
    subsets2_iter([1,2,2,2])
    subsets2_iter([1,1,1,1])
    '''
    for x in subset_binary([1,2,3,4]): print x


