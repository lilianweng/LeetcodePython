#!/usr/bin/env python
'''
Leetcode: Longest Substring Without Repeating Characters
Given a string, find the length of the longest substring without repeating characters. For example, the longest substring without repeating letters for "abcabcbb" is "abc", which the length is 3. For "bbbbb" the longest substring is "b", with the length of 1.
http://leetcode.com/2011/05/longest-substring-without-repeating-characters.html
'''
from __future__ import division
import random

### Naive, ~O(n(n-1)/2)
def longest_substr_no_repeat(s):
    n = len(s)
    max_len = 0
    for i in range(n):
        cur_len = 1 # length of no-repeat substr starting at index i
        chars = set([s[i]])
        for j in range(i+1, n):
            if s[j] in chars:
                max_len = max(cur_len, max_len)
                break
            else:
                cur_len += 1
                chars.add(s[j])
        print i, '-', s[i], chars, cur_len, max_len
        max_len = max(cur_len, max_len)
        if max_len == n-i: return max_len # others cannot be longer
    return max_len


### DP: time ~ O(n); space ~ O(n)
# L(i) = length of no-repeat substr starting at index i
# L(i+1) = L(i) + 1 if last_seen[s[i+1]] <= i-L[i];
#          i + 1 - last_seen[s[i+1]]
def longest_substr_no_repeat2(s):
    last_seen = {s[0]:0}
    L = {0:1}
    for i in range(1,len(s)):
        if last_seen.get(s[i], -1) <= (i-1)-L[i-1]:
            L[i] = L[i-1] + 1
        else:
            L[i] = i - last_seen[s[i]]
        last_seen[s[i]] = i
    print 'last_seen:', last_seen
    print 'L{}:', L
    return max(L.values())


### http://leetcode.com/2011/05/longest-substring-without-repeating-characters.html
# use a cache to record existing characters
def longest_substr_no_repeat3(s):
    n = len(s)
    max_len = i = j = 0
    exist = dict((ch,False) for ch in range(257)) # ascii code
    while j < n:
        if exist[ord(s[j])]:
            max_len = max(max_len, j-i)
            # move i until the duplicate s[j] is removed
            while s[i] != s[j]:
                exist[ord(s[i])] = False
                i += 1
            i += 1
            j += 1
        else:
            exist[ord(s[j])] = True
            j += 1
    # leftover
    max_len = max(max_len, n-i)
    return max_len


if __name__ == '__main__':
    print longest_substr_no_repeat("abcabcbbecaf")
    print longest_substr_no_repeat("bbbbbb")
    print longest_substr_no_repeat("ababa")
    print longest_substr_no_repeat("aaaaabcdefgggggghijklxyzzzz")
    print
    print longest_substr_no_repeat2("abcabcbbecaf")
    print longest_substr_no_repeat2("bbbbbb")
    print longest_substr_no_repeat2("ababa")
    print longest_substr_no_repeat2("aaaaabcdefgggggghijklxyzzzz")


