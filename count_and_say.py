#!/usr/bin/env python
'''
Leetcode: Count and say
The count-and-say sequence is the sequence of integers beginning as follows:
1, 11, 21, 1211, 111221, ...

1 is read off as "one 1" or 11.
11 is read off as "two 1s" or 21.
21 is read off as "one 2, then one 1" or 1211.

Given an integer n, generate the nth sequence.
Note: The sequence of integers will be represented as a string.
'''
from __future__ import division
import random

def count_and_say(n):
    if n == 0: return []
    prev_s = '1'
    seqs = [prev_s]
    for i in range(1,n):
        cur_s = ''
        prev_char = prev_s[0]
        prev_char_count = 1
        for char in prev_s[1:]:
            # update counter
            if char != prev_char:
                cur_s += str(prev_char_count) + prev_char
                prev_char = char
                prev_char_count = 0
            prev_char_count += 1
        # leftover
        cur_s += str(prev_char_count) + prev_char
        seqs.append(cur_s)
        prev_s = cur_s
    
    # pretty print
    for i in range(1,n+1): print str(i)+'-th:', seqs[i-1]
    return seqs


if __name__ == '__main__':
    print count_and_say(10)


