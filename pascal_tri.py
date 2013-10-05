#!/usr/bin/env python

from __future__ import division
import random


'''
Leetcode: Pascal's Triangle
Given numRows, generate the first numRows of Pascal's triangle.
For example, given numRows = 5,
Return
[
     [1],
    [1,1],
   [1,2,1],
  [1,3,3,1],
 [1,4,6,4,1]
]'''
def pascal(n):
    if n == 0: return []
    rows = [[1]]
    row = [1]
    for i in range(1,n):
        row = [1] + [row[j]+row[j+1] for j in range(len(row)-1)] + [1]
        rows.append(row)
    print '\n'.join(map(str,rows))
    return rows


'''
Leetcode: Pascal's Triangle II
Given an index k, return the kth row of the Pascal's triangle.
For example, given k = 3, return [1,3,3,1].
Note: Could you optimize your algorithm to use only O(k) extra space?
'''
def pascal2(k):
    # k-th row: C(k,0), C(k,1), ..., C(k,k)
    # C(k,i+1) = C(k,i) * (k-i) / (i+1)
    row = [1]
    C = 1
    for i in range(k):
        C *= (k-i)/(i+1)
        row.append( int(C) )
    print row
    return row


if __name__ == '__main__':
    pascal(5)
    pascal2(4)


