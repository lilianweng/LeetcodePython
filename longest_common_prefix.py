#!/usr/bin/env python
'''
Leetcode: Longest Common Prefix
Write a function to find the longest common prefix string amongst an array of strings.
'''
from __future__ import division
import random

### Solution#1: Build a trie tree: O(nm)


### Solution#2: Hash the first string as f, fl, flo, flow, flowe, flower, and initialize the max_prefix_len=5.
# For every other string s, start checking the prefix with min{max_prefix_len, len(s)}. If match go to the next string; if not, remove the last character and re-compare. ~O(n+m) 
def longest_prefix(strings):
    first = strings[0]
    prefixs = set([first[:i] for i in range(len(first))])
    max_prefix_len = len(first)
    i = 1
    while i < len(strings) and max_prefix_len > 0:
        s = strings[i]
        # Adjust the length
        l = min(len(s), max_prefix_len)
        s = s[:l]
        max_prefix_len = l
        while s not in prefixs:
            s = s[:-1]
            max_prefix_len -= 1
        i += 1
    return first[:max_prefix_len]


if __name__ == '__main__':
    print longest_prefix(['hello','hell','heaven','heavy'])


