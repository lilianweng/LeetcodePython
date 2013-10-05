#!/usr/bin/env python
'''
Leetcode: Decode ways
A message containing letters from A-Z is being encoded to numbers using the following mapping:
'A' -> 1
'B' -> 2
...
'Z' -> 26
Given an encoded message containing digits, determine the total number of ways to decode it.

For example, Given encoded message "12", it could be decoded as "AB" (1 2) or "L" (12). The number of ways decoding "12" is 2.
'''
from __future__ import division
import random

# ord('A') = 65; ord('a') = 97
# mapping = dict((code-64, chr(code)) for code in range(ord('A'), ord('Z')+1))
def decode_ways(msg):
    if msg == '': return 1
    if len(msg) == 1 and int(msg) > 0: return 1
    if len(msg) == 1 and int(msg) == 0: return 0
    first_one = int(msg[0])
    first_two = int(msg[:2])
    x = decode_ways(msg[1:]) if 1 <= first_one <= 9 else 0
    y = decode_ways(msg[2:]) if 1 <= first_two <= 26 else 0
    return x+y


## DP:
# S[i] = #decoding ways for msg[:i], 0 <= i <= n
# S[i] = S[i-1] (if msg[i-1] > 0) + S[i-2] (if msg[i-2:i] between 1 and 26)
def decode_ways_iter(msg):
    S={}
    S[0] = 1
    S[1] = 1 if msg[0] != '0' else 0
    for i in range(2,len(msg)+1):
        x = S[i-1] if msg[i-1] != '0' else 0
        y = S[i-2] if 1 <= int(msg[i-2:i]) <= 26 else 0
        S[i] = x + y
    return S[len(msg)]


def decode_ways_content(msg, mapping):
    if len(msg) == 0:
        yield ''
    elif len(msg) == 1 and int(msg) > 0:
        yield mapping[int(msg)]
    else:
        first_one = int(msg[0])
        if 1 <= first_one <= 9:
            for d in decode_ways_content(msg[1:], mapping):
                yield mapping[first_one] + d
        first_two = int(msg[:2])
        if 1 <= first_two <= 26:
            for d in decode_ways_content(msg[2:], mapping):
                yield mapping[first_two] + d


def decode_ways_content_iter(msg, mapping):
    S={}
    S[0] = ['']
    S[1] = [mapping[int(msg[0])]] if msg[0] != '0' else []
    for i in range(2, len(msg)+1):
        S[i] = []
        first_one = int(msg[i-1:i])
        first_two = int(msg[i-2:i])
        if first_one > 0:
            for prev in S[i-1]:
                S[i].append( prev+mapping[first_one] )
        if 1 <= first_two <= 26:
            for prev in S[i-2]:
                S[i].append( prev+mapping[first_two] )
    return S[len(msg)]


if __name__ == '__main__':
    mapping = {}
    for i, code in enumerate(range(ord('A'), ord('Z')+1)):
        mapping[i+1] = chr(code)
    
    print decode_ways('00')
    print decode_ways('1201200')
    print decode_ways('12302415')
    
    print decode_ways_iter('0')
    print decode_ways_iter('00')
    print decode_ways_iter('120')
    print decode_ways_iter('12302415')
    
    for d in decode_ways_content('00', mapping): print d
    for d in decode_ways_content('12302415', mapping): print d
    
    print '00:'
    for d in decode_ways_content_iter('00', mapping): print d
    print '12302415:'
    for d in decode_ways_content_iter('12302415', mapping): print d


