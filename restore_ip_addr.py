#!/usr/bin/env python
'''
Leetcode: Restore IP Addresses
Given a string containing only digits, restore it by returning all possible valid IP address combinations.
For example:
    Given "25525511135",
    return ["255.255.11.135", "255.255.111.35"]. (Order does not matter)
'''
from __future__ import division
import random


# each digit between 0~255
def gen_ip_addr(s, num_part):
    if num_part == 0 and len(s) == 0: yield []
    elif num_part == 1 and 1 <= len(s) <= 3: yield [s]
    else:
        for l in range(1, min(3,len(s))+1):
            digit = s[:l]
            if int(digit) > 255: continue
            for p in gen_ip_addr(s[l:], num_part-1):
                yield [digit] + p


def ip_addr(s):
    ips = []
    for p in gen_ip_addr(s, 4):
        print '.'.join(p)
        ips.append('.'.join(p))
    return ips


if __name__ == '__main__':
    ip_addr("25525511135")
    ip_addr("1122211120")


