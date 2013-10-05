#!/usr/bin/env python
'''
Leetcode: Substring with Concatenation of All Words
You are given a string, S, and a list of words, L, that are all of the same length. Find all starting indices of substring(s) in S that is a concatenation of each word in L exactly once and without any intervening characters.

For example, given:
S: "barfoothefoobarman"
L: ["foo", "bar"]
You should return the indices: [0,9].
(order does not matter).
'''
from __future__ import division
import random


# Naive, O(len(S)*len(L)*len(word))
def concat_words(S, L):
    k = len(L[0])
    rets = []
    for i in range(len(S)-k+1):
        words = set(L)
        start = i
        while words:
            if S[start:start+k] in words:
                words.remove(S[start:start+k])
                start += k
            else:
                break
        if not words: rets.append(i)
    return rets


# check concatenation at
#   first 0, k, 2k, ..., n-1; 
#   then 1, k+1, 2k+1, ..., n-1; 
#   then 2, k+2, 2k+2, ..., n-1, etc.; 
#   until k-1, 2k-1, 3k-1, ..., n-1.
def concat_words2(S,L):
    k = len(L[0])
    rets = []
    for start in range(k):
        matched = []
        unmatched = set(L)
        for i in range(start, len(S)-k+1, k):
            # Shift left for k pos
            # benefit from the previous match
            if matched:
                unmatched.add(matched[0])
                matched = matched[1:]
            
            # Consider substring starting at i pos
            pos = i
            while unmatched:
                word = S[pos:pos+k]
                if word in unmatched: # Continue when matched.
                    unmatched.remove(word)
                    matched.append(word)
                else:
                    break # Leave when unmatched.
                pos += k
            if not unmatched:
                rets.append(i)
            else:
                # clear; prepare for re-matching at the next pos
                matched = []
                unmatched = set(L)
    print rets
    return rets


if __name__ == '__main__':
    print concat_words("barfoothefoobarman", ["foo","bar"])
    print concat_words("skyesskikeyyesskiandkeyskiyes", ["key","ski","yes"])
    print concat_words2("barfoothefoobarman", ["foo","bar"])
    print concat_words2("skyesskikeyyesskiandkeyskiyes", ["key","ski","yes"])


