#!/usr/bin/env python
'''
Leetcode: Wildcard Matching
Implement wildcard pattern matching with support for '?' and '*'.

'?' Matches any single character.
'*' Matches any sequence of characters (including the empty sequence).

The matching should cover the entire input string (not partial).
The function prototype should be:
bool isMatch(const char *s, const char *p)
Some examples:
isMatch("aa","a") ? false
isMatch("aa","aa") ? true
isMatch("aaa","aa") ? false
isMatch("aa", "*") ? true
isMatch("aa", "a*") ? true
isMatch("ab", "?*") ? true
isMatch("aab", "c*a*b") ? false
'''
from __future__ import division
import random

def wildcard_match(s, p):
    if len(p) == 0: return len(s) == 0
    # s can be empty
    if p[0] == '?':
        return len(s) > 0 and wildcard_match(s[1:], p[1:])
    elif p[0] == '*':
        # match nothing or
        # match one and continue, AB* = A*
        return wildcard_match(s, p[1:]) or \
               (len(s) > 0 and wildcard_match(s[1:], p))
    else: 
        return len(s) > 0 and s[0] == p[0] and wildcard_match(s[1:], p[1:])
    
    return False


if __name__ == '__main__':
    print wildcard_match("aa","a")
    print wildcard_match("aa","aa")
    print wildcard_match("aaa","aa")
    print wildcard_match("aa", "*")
    print wildcard_match("aa", "a*")
    print wildcard_match("ab", "?*")
    print wildcard_match("aab", "c*a*b")


