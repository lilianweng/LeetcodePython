#!/usr/bin/env python
'''
Leetcode: Generate Parentheses
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses. For example, given n = 3, a solution set is: "((()))", "(()())", "(())()", "()(())", "()()()"
'''
from __future__ import division
import random

def parentheses_combination(left, right):
    if left == 0 and right == 0: yield ''
    if left > 0:
        for p in parentheses_combination(left-1, right):
            yield '('+p
    if right > left:
        for p in parentheses_combination(left, right-1):
            yield ')'+p


# Other ways?

if __name__ == '__main__':
    for p in parentheses_combination(4,4): print p


