#!/usr/bin/env python

from __future__ import division
import random


'''
Leetcode: Integer to Roman
Given an integer, convert it to a roman numeral.
Input is guaranteed to be within the range from 1 to 3999.

1) I can be placed before V and X to make 4 units (IV) and 9 units (IX)
2) X can be placed before L and C to make 40 (XL) and 90 (XC)
3) C can be placed before D and M to make 400 (CD) and 900 (CM)
'''
def int_to_roman(num):
    print num, 
    if num <= 0: return None
    val2sym = {1:'I', 5:'V', 10:'X', 50:'L', 100:'C', 500:'D', 1000:'M'}
    vals = sorted(val2sym.keys(), reverse=True)
    roman = ''
    for val in vals:
        n, num = divmod(num, val)
        last_digit = roman[-1] if len(roman) > 0 else ''
        if n == 4 and val == 1:
            roman = roman[:-1]+'IX' if last_digit=='V' else roman+'IV'
        elif n == 4 and val == 10:
            roman = roman[:-1]+'XC' if last_digit=='L' else roman+'XL'
        elif n == 4 and val == 100:
            roman = roman[:-1]+'CM' if last_digit=='D' else roman+'CD'
        else:
            roman += val2sym[val]*n
    print roman
    return roman


'''
Leetcode: Roman to Int
Given a roman numeral, convert it to an integer.
Input is guaranteed to be within the range from 1 to 3999.
1) I can be placed before V and X to make 4 units (IV) and 9 units (IX)
2) X can be placed before L and C to make 40 (XL) and 90 (XC)
3) C can be placed before D and M to make 400 (CD) and 900 (CM)
'''
def roman_to_int(roman):
    val2sym = {1:'I', 5:'V', 10:'X', 50:'L', 100:'C', 500:'D', 1000:'M'}
    sym2val = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
    # Replace 4, 9, 40, 90, 400, 900
    for i in [1,10,100]:
        roman = roman.replace(val2sym[i]+val2sym[5*i], val2sym[i]*4)
        roman = roman.replace(val2sym[i]+val2sym[10*i], val2sym[5*i]+val2sym[i]*4)
    
    ret = sum([sym2val[ch] for ch in roman])
    print roman, ret
    return ret


if __name__ == '__main__':
    int_to_roman(290)
    roman_to_int('CCIX')


