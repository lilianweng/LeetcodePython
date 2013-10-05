#!/usr/bin/env python
'''
Leetcode: Regular Expression Matching
'.' Matches any single character.
'*' Matches zero or more of the preceding element.

The matching should cover the entire input string (not partial).
The function prototype should be: bool isMatch(const char *s, const char *p)
Some examples:
isMatch("aa","a") -> false
isMatch("aa","aa") -> true
isMatch("aaa","aa") -> false
isMatch("aa", "a*") -> true
isMatch("aa", ".*") -> true
isMatch("ab", ".*") -> true
isMatch("aab", "c*a*b") -> true

http://leetcode.com/2011/09/regular-expression-matching.html
DFA: http://swtch.com/~rsc/regexp/regexp1.html
'''
from __future__ import division
import random


def split_pattern(p):
    plist = []
    while len(p) > 0:
        if len(p) == 1:
            plist.append( p[0] )
            p = p[1:]
        else:
            if p[1] == '*':
                plist.append( p[:2] )
                p = p[2:]
            else:
                plist.append( p[0] )
                p = p[1:]
    print 'formatted pattern:', plist
    return plist


def is_match(s, plist):
    #print s, plist,
    if len(plist) == 0: return len(s) == 0
    '''if len(s) == 0: 
        for p in plist:
            if not p.endswith('*'): return False
        return True'''
    
    p = plist[0]
    # p has no '*'
    if not p.endswith('*'):
        #print 'matching', (s[0] if len(s) > 0 else ''), 'and', p
        if p.startswith('.'):
            return len(s) > 0 and is_match(s[1:], plist[1:])
        else:
            return len(s) > 0 and s[0] == p and is_match(s[1:], plist[1:])
    
    # p has '*'
    else:
        #print 'matching', p
        if p.startswith('.'):
            return is_match(s, plist[1:]) or (len(s) > 0 and is_match(s[1:], plist))
        else:
            return is_match(s, plist[1:]) or (len(s) > 0 and s[0] == p[0] and is_match(s[1:], plist))


if __name__ == '__main__':
    print is_match('aaaaaabc', split_pattern('aa*bc*.*'))
    print is_match('aaaaaabc', split_pattern('aa*b..'))
    print is_match('aaaaaa', split_pattern('aaa'))
    print is_match('', split_pattern('aaa'))
    print is_match('xyz', split_pattern('...'))



