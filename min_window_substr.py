#!/usr/bin/env python
'''
Leetcode: Minimum Window Substring
Given a string S and a string T, find the minimum window in S which will contain all the characters in T in complexity O(n).

For example,
S = "ADOBECODEBANC"
T = "ABC"
Minimum window is "BANC".

Note: If there is no such window in S that covers all characters in T, return the emtpy string "". If there are multiple such windows, you are guaranteed that there will always be only one unique minimum window in S.
'''

from __future__ import division
import random

# O(|S|log|T|)
def min_window_substr(S, T):
    if S == '' or T == '': return ''
    last_seen = {}
    start = 0; end = len(S)-1
    T = set(T)
    # find such a substring ended at i-th character.
    for i, ch in enumerate(S):
        if ch not in T: continue
        last_seen[ch] = i
        if len(last_seen) == len(T):
            # all chars have been seen
            first = min(last_seen.values()) #**We can use a priority queue, O(logn)
            if i-first+1 < end-start+1:
                start = first; end = i
    
    window = S[start:end+1] if len(last_seen) == len(T) else ""
    print window, len(window)
    return window


if __name__ == '__main__':
    print min_window_substr("AFDOBECODEBANCD", "ABCF")
    print min_window_substr("AAABDFBFFHGKOAAFDOPPQDQPFVCCDEC", "ACD")
    print min_window_substr("AAABBBB", "AB")
    print min_window_substr("", "")


