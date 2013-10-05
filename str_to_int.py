#!/usr/bin/env python
'''
Leetcode: atoi
Implement atoi to convert a string to an integer.

Hint: Carefully consider all possible input cases. If you want a challenge, please do not see below and ask yourself what are the possible input cases.

Notes: It is intended for this problem to be specified vaguely (ie, no given input specs). You are responsible to gather all the input requirements up front.

-----------------------------------------------------------------------
http://www.cplusplus.com/reference/cstdlib/atoi/:
The function first discards as many whitespace characters (as in isspace) as necessary until the first non-whitespace character is found. Then, starting from this character, takes an optional initial plus or minus sign followed by as many base-10 digits as possible, and interprets them as a numerical value.

The string can contain additional characters after those that form the integral number, which are ignored and have no effect on the behavior of this function.

If the first sequence of non-whitespace characters in str is not a valid integral number, or if no such sequence exists because either str is empty or it contains only whitespace characters, no conversion is performed and zero is returned.

If no valid conversion could be performed, a zero value is returned. If the correct value is out of the range of representable values, INT_MAX (2147483647) or INT_MIN (-2147483648) is returned.
'''
from __future__ import division
import random

INT_MAX = 2147483647
INT_MIN = -2147483648

# remove white spaces
# +/- followed by base-10 digits
# other characters are ignored
def atoi(s):
    s = s.strip()
    neg = False
    if s[0] == '-':
        neg = True
        s = s[1:]
    elif s[0] == '+':
        s = s[1:]
    
    digits = ''
    for ch in s:
        if ch.isdigit():
            digits += ch
        else:
            if len(digits) == 0: return 0
            elif not neg and digits > '2147483647': return INT_MAX
            elif neg and digits > '2147483648': return INT_MIN
            else:
                number = int(digits)
                return -number if neg else number
    # leftover
    if not neg and digits > '2147483647': return INT_MAX
    elif neg and digits > '2147483648': return INT_MIN
    else:
        number = int(digits)
        return -number if neg else number


if __name__ == '__main__':
    print atoi('-112ddfs')
    print atoi('12345')
    print atoi('+01')
    print atoi('+0.2312')
    print atoi('-1900.2312')
    print atoi('a')
    print atoi('21474836472147483647')
    


