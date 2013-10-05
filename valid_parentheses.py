#!/usr/bin/env python
'''
Leetcode: Valid Parentheses
Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
The brackets must close in the correct order, "()" and "()[]{}" are all valid but "(]" and "([)]" are not.
'''
from __future__ import division
import random


# Use stack; never push right parenthesis but only try to 
# match it with left ones in the stack
def valid_parentheses(s):
    lefts = {'(':0, '{':1, '[':2}
    rights = {')':0, '}':1, ']':2}
    stack = []
    for ch in s:
        if ch in lefts:
            stack.append(lefts[ch])
        elif ch in rights:
            if not stack: return False
            if stack[-1] == rights[ch]: stack.pop()
            else: return False
        else:
            return False
    return True


if __name__ == '__main__':
    print valid_parentheses('[{}[]((()))]')
    print valid_parentheses('[{[(((]))})]')


