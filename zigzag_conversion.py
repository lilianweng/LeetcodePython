#!/usr/bin/env python
'''
Leetcode: ZigZag Conversion
The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"
Write the code that will take a string and make this conversion given a number of rows:
string convert(string text, int nRows);
convert("PAYPALISHIRING", 3) should return "PAHNAPLSIIGYIR".
'''
from __future__ import division
import random

# x = k+(k-2)
# row 0: 0, x, 2x, 3x, ...
# row 1: 1, x-1,x+1, 2x-1,2x+1, ...
# row i: i, x-i,x+i, 2x-i,2x+i, ...
# row k-1: k-1, x+k-1, 2x+k-1, ...
def convert(S, k):
    n = len(S); print 'n =', n
    x = 2*k-2
    rets = ""
    for i in range(k):
        if i >= n: break # in case the string is too short.
        rets += S[i]
        j = x
        while j-i < n:
            if i == 0: 
                rets += S[j+0]
            elif i == k-1: 
                if j+i <= n-1: rets += S[j+i]
            else: 
                rets += S[j-i]
                if j+i <= n-1: rets += S[j+i]
            j += x
    print rets
    return rets
    

if __name__ == '__main__':
    convert("PAYPALISHIRING", 3)
    convert("ABCD", 5)
    convert("ABCDEFGHIJKLMNOPQRSTUVWXYZ", 5)
    convert("ABCDEFGHIJKLMNOPQRSTUVWXYZ", 10)


