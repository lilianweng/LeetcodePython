#!/usr/bin/env python
'''
Leetcode: Palindrome number

Determine whether an integer is a palindrome. Do this without extra space.
* Should be interesting if it is a float, but it is hard to determine the accuracy

http://leetcode.com/2012/01/palindrome-number.html
'''
from __future__ import division
import math

# number with k digit
# 10**(k-1) <= num < 10**k
def pali_num(num):
    print 'Check:', num, 
    if num < 0: return False
    if num == 0: return True
    k = int(math.log10(num)) + 1
    base = 10**(k-1)
    while num > 0 and base > 1:
        # left-most digit?
        left = num // base
        num -= left*base
        base /= 100
        # right-most digit?
        right = num % 10
        num = num // 10
        if left != right: return False
    return True


if __name__ == '__main__':
    print pali_num(12345)
    print pali_num(12321)
    print pali_num(123321)
    print pali_num(1236666321)
    print pali_num(-1)
    print pali_num(-0)
    print pali_num(0)
    