#!/usr/bin/env python
from __future__ import division
import random

def add_str(a,b):
    carry = 0
    sum = ""
    i = len(a)-1; j = len(b)-1
    while i >= 0 and j >= 0:
        x, y = int(a[i]), int(b[j])
        carry, z = divmod(x+y+carry, 10)
        sum = str(z) + sum
        i -= 1; j -= 1
    
    while i >= 0:
        carry, z = divmod(carry+int(a[i]), 10)
        sum = str(z) + sum
        i -= 1
    while j >= 0:
        carry, z = divmod(carry+int(b[j]), 10)
        sum = str(z) + sum
        j -= 1
    # leftover
    if carry != 0: sum = str(carry) + sum
    #print a+' + '+b+' = '+sum
    return sum


def sub_str(a,b):
    pass


def div_str(a,b):
    pass


'''
Leetcode: Multiple Strings
Given two numbers represented as strings, return multiplication of the numbers as a string.
Note: The numbers can be arbitrarily large and are non-negative.
'''
def multi_str(a,b):
    tmp_sums = []
    if len(b) > len(a): a,b = b,a
    i = 0
    for y in reversed(b):
        y = int(y)
        carry = 0
        tmp_sum = ""
        for x in reversed(a):
            carry, z = divmod(int(x)*y+carry, 10)
            tmp_sum = str(z) + tmp_sum
        if carry > 0: tmp_sum = str(carry) + tmp_sum
        tmp_sums.append(tmp_sum + '0'*i)
        i += 1
    
    final = '0'
    for s in tmp_sums: final = add_str(final, s)
    print a+' * '+b+' = '+final
    return final


def multi_str2(a,b):
    orig_a = a; orig_b = b
    a = map(int, a[::-1])
    b = map(int, b[::-1])
    # multiply into digit by digit
    final = ''
    carry = 0
    ### IMPORTANT PART ###
    for s in range(len(a)+len(b)-1):
        for i in range(len(a)):
            j = s-i
            if 0 <= j <= len(b)-1:
                #print i,j
                carry += a[i]*b[j]
        final += str(carry % 10)
        carry //= 10
    
    if carry > 0: final += str(carry)
    final = final[::-1]
    print orig_a + ' * '+ orig_b +' = '+final
    return final


if __name__ == '__main__':
    multi_str("1999", "0")
    multi_str("989", "120")
    multi_str("9999999", "9999999")
    multi_str2("1999", "0")
    multi_str2("989", "120")
    multi_str2("9999999", "9999999")


