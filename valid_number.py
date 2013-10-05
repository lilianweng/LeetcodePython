#!/usr/bin/env python
'''
Leetcode: Valid Number

Validate if a given string is numeric.
Some examples:
"0" => true
" 0.1 " => true
"abc" => false
"1 a" => false
"2e10" => true

Note: It is intended for the problem statement to be ambiguous. You should gather all requirements up front before implementing one.
'''

from __future__ import division
import sys, random

# integer: negative sign/integer
# float
# scientific notation: 'e'/'E'
# hex number??
# other base k number?
# complex number??
# fraction??
#
# [space*][+?/-?][digits*][.?][digits+][e/E][+?/-?][digits*][.?][digits+][space*]
def valid_number(s):
    print s,
    s = s.strip()
    subs = s.lower().split('e')
    if len(subs) > 2: return False  # too many e's
    if len(subs) == 2 and len(subs[1]) == 0: return False # no number after e
    
    for sub in subs:
        # each sub is a valid number (without 'e')
        # [+?/-?][digits*][.?][digits+]
        has_dot = False
        has_digits = 0
        if sub[0] in ['+','-']: sub = sub[1:]
        sub_secs = sub.split('.')
        if len(sub_secs) > 2: # two many dots
            return False
        # Each sub_secs should be empty or only digits
        for sec in sub_secs:
            for ch in sec:
                if not ch.isdigit():
                    return False
    return True


### Use finite turing machine


if __name__ == '__main__':
    print valid_number("0")
    print valid_number(" 0.1")
    print valid_number("abc")
    print valid_number("1 a")
    print valid_number("2.e5")
    print valid_number("2e10")
    print valid_number(" 3.5e4.5 ")
    print valid_number("56.8.9")
    print valid_number("-12.3E.11")
    print valid_number("-12.3E")
    print valid_number("+2.")
    
    
    