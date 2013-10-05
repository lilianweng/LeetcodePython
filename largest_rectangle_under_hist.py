#!/usr/bin/env python
'''
Find largest rectangle under given histogram
'''
from __future__ import division
import random

# For each ai, we can determine 
# S(i) = the max rectangle that contains ai with ai as height,
# maximum width of rectangle including that bar will be L+R+1, where:
# L is number of adjacent bars to the left of ith bar and height greater than or equal to h(i). R is number of adjacent bars to the right of ith bar and height greater than or equal to h(i).

# O(n)
def largest_rectangle0(A):
    L, R = {}, {}
    # find Li: for i-th element in L, 
    # Li is from i to its left, the first element <= A[i]
    stack = [0]
    for i in xrange(1,n):
        while stack and A[i] <= A[stack[-1]]: stack.pop()
        if stack: L[i] = i-stack[-1]-1
        else: L[i] = i
        stack.append(i)
    # find Ri: for i-th element in L, 
    # Ri is from i to its right, the first element <= A[i]
    R = {n-1:0}; stack = [n-1]
    for i in reversed(xrange(n-1)):
        while stack and A[i] <= A[stack[-1]]: stack.pop()
        if stack: R[i] = stack[-1]-i-1
        else: R[i] = (n-1)-i
        stack.append(i)
    
    S = dict((i, A[i]*(L[i]+R[i]+1)) for i in range(len(a)))
    print 'L:', L
    print 'R:', R
    print S
    return max(S.values())


# O(n^2)
def largest_rectangle1(a):
    S = {}
    for i in range(len(a)):
        # check Left width
        j = i
        while j > 0 and a[j] >= a[i]: j -= 1
        if a[j] < a[i]: j = j+1
        L = i-j
        # check right width
        j = i
        while j < len(a)-1 and a[j] >= a[i]: j += 1
        if a[j] < a[i]: j = j-1
        R = j-i
        S[i] = (L+R)*a[i]
    print a
    print S
    return max(S.values())


### Use stack to track height and starting index
# compare current height with previous one, pop out previous one is the current < previous, and compute the rectangle area.
# Scan twice, left-->right than right-->left
def largest_rectangle2(a):
    S = {}
    # left --> right
    stack = []
    for i in xrange(len(a)):
        while stack:
            if a[i] < a[stack[-1]]:
                start_i = stack.pop()
                S[start_i] = a[start_i] * (i-1-start_i)
            else:
                break
        stack.append(i)
    while stack:
        start_i = stack.pop()
        S[start_i] = a[start_i] * (len(a)-1-start_i)
    
    # left --> right
    stack = []
    for i in reversed(xrange(len(a))):
        while stack:
            if a[i] < a[stack[-1]]:
                start_i = stack.pop()
                S[start_i] += a[start_i] * (start_i-i-1)
            else:
                break
        stack.append(i)
    while stack:
        start_i = stack.pop()
        S[start_i] += a[start_i] * start_i
    print S
    return max(S.values())


### DP: O(n^2)
# h(i,j) = the maximum height of a rectangle under the bars from ai to aj.
# h(i,j) = min{a_k for i<=k<=j}
# h(i,j+1) = min{h(i,j), a(j)}
def largest_rectangle3(a):
    n = len(a)
    h = {}
    for i in range(n): h[i,i] = a[i]
    for k in range(1,n):
        for i in range(n):
            j = i+k
            if j >= n: continue
            h[i,j] = min(h[i,j-1], a[j])
    
    S = dict(((i,j), (j-i)*h[i,j]) for i,j in h)
    print S
    return max(S.values())


# left[i] is the most-left side column that i can extend to;
# left[i] = max{j: h[j]<h[i] && j<i} + 1;
# right[i] is the most-right side column that i can reach at;
# right[i] = min{j: h[j]<h[i] && j>i} + 1;
#the rectangle area is calculated as: area[i] = (right[i]-left[i]-1) * h[i];


if __name__ == '__main__':
    a = [2,1,3,2,4,5,2,3,1]
    print largest_rectangle2(a)
    print largest_rectangle3(a)

