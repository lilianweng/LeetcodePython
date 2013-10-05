#!/usr/bin/env python
'''
Leetcode: Gray Code
The gray code is a binary numeral system where two successive values differ in only one bit. Given a non-negative integer n representing the total number of bits in the code, print the sequence of gray code. A gray code sequence must begin with 0.

For example, given n = 2, return [0,1,3,2]. Its gray code sequence is:
00 - 0
01 - 1
11 - 3
10 - 2
Note:
For a given n, a gray code sequence is not uniquely defined. For example, [0,2,3,1] is also a valid gray code sequence according to the above definition.

http://www.matrix67.com/blog/archives/266
n-th gray code: n xor (n >> 1)
'''
from __future__ import division
import random

def print_int(codes):
    for c in codes:
        print c, '-', int(c,2)


def gray_code(n):
    if n == 1: return ['0','1']
    prev_codes = grey_code(n-1)
    codes = []
    for c in prev_codes:
        codes.append('0'+c)
    for c in reversed(prev_codes):
        codes.append('1'+c)
    return codes


def gray_code_iter(n):
    codes = ['0','1']
    for i in range(1,n):
        new_codes = ['0'+c for c in codes] + \
                    ['1'+c for c in reversed(codes)]
        codes = new_codes
    return codes


def gray_code_bit(n):
    ret = []
    count = 1 << n;
    for i in range(count):
        ret.append( bin(i ^ (i >> 1)) )
    return ret


if __name__ == '__main__':
    print_int(gray_code_bit(3))
    print_int(gray_code_iter(3))


