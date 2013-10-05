#!/usr/bin/env python
'''
Leetcode: Longest Valid Parentheses
Given a string containing just the characters '(' and ')', find the length of the longest valid (well-formed) parentheses substring.
For "(()", the longest valid parentheses substring is "()", which has length = 2.
Another example is ")()())", where the longest valid parentheses substring is "()()", 
which has length = 4.
'''
from __future__ import division
import random

### Use a stack to keep track of the positions of non-matching '('s. 
### Also need to keep track of the position of the last ')'.
def longest_valid_parentheses(s):
    max_len = 0
    start = end = -1
    last = -1 # the position of the last ')'
    stack_lefts = [] # positions of non-matching '('s
    for i, p in enumerate(list(s)):
        if p == '(':
            stack_lefts.append(i)
        elif not stack_lefts:
            # for ')': no matching left
            last = i
        else:
            # for ')': find a matching pair
            stack_lefts.pop()
            cur_start = stack_lefts[-1]+1 if stack_lefts else last+1
            cur_len = i-cur_start+1
            if cur_len > max_len:
                max_len = cur_len
                start = cur_start
                end = i
    print s, ':', max_len, s[start:end+1]
    return max_len


if __name__ == '__main__':
    longest_valid_parentheses(")()()(()()())())))")
    longest_valid_parentheses("(()")
    longest_valid_parentheses("")
    longest_valid_parentheses(")()(()(()(")
    longest_valid_parentheses("(((()(((")
    longest_valid_parentheses("))))))(((((")


