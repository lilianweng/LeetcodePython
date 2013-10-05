#!/usr/bin/env python
'''
Leetcode: Length of Last Word
Given a string s consists of upper/lower-case alphabets and empty space characters ' ', return the length of last word in the string.
If the last word does not exist, return 0. Note: A word is defined as a character sequence consists of non-space characters only.
For example, Given s = "Hello World", return 5.
'''
from __future__ import division
import random

def last_word(s):
    # upper/lower-case alphabets and empty space
    # remove spaces at the end
    while s and not s[-1].isalpha(): s = s[:-1]
    length = 0
    for i in reversed(xrange(len(s))):
        if s[i].isalpha(): length += 1
        else: return length
    return length

if __name__ == '__main__':
    print last_word("Hello World")
    print last_word("   ")
    print last_word(" a a a ")


