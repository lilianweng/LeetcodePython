#!/usr/bin/env python
'''
Leetcode: Sort Colors

Given an array with n objects colored red, white or blue, sort them so that objects of the same color are adjacent, with the colors in the order red, white and blue. Here, we will use the integers 0, 1, and 2 to represent the color red, white, and blue respectively.
Note: You are not suppose to use the library's sort function for this problem.
'''
from __future__ import division
import random


'''A rather straight forward solution is a two-pass algorithm using counting sort. First, iterate the array counting number of 0's, 1's, and 2's, then overwrite array with total number of 0's, then 1's and followed by 2's.'''
def sort_colors(L):
    from collections import Counter
    counter = Counter(L)
    for i,x in enumerate(counter.elements()): L[i] = x
    return L

'''
Follow up: Could you come up with an one-pass algorithm using only constant space?
'''

def sort_colors2(L):
    n = len(L)
    zero = 0; two = n-1
    # Write 1 at the beginning; 2 at the end.
    cur = 0
    while cur <= two:
        print cur, L, zero, two
        if L[cur] == 0:
            if cur > zero:
                L[zero], L[cur] = L[cur], L[zero]
                zero += 1
            else:
                # cur == zero and L[cur] == L[zero] == 0
                cur += 1
                zero += 1
        
        elif L[cur] == 2:
            if cur < two:
                L[two], L[cur] = L[cur], L[two]
                two -= 1
            else:
                break
        else:
            cur += 1
    print L, '\n'
    return L


def sort_colors3(A):
    n = len(A)
    k = 0; zero = 0; two = n-1
    while k <= two:
        if A[k] == 0 and zero < k:
            A[k], A[zero] = A[zero], A[k]
            while A[zero] == 0: zero += 1
            
        elif A[k] == 2 and k < two:
            A[k], A[two] = A[two], A[k]
            while A[two] == 2: two -= 1
        else:
            k += 1
        print k, zero, two, A
    print A


if __name__ == '__main__':
    sort_colors2([2,0,1,0,2,1,2,2,1,1])
    sort_colors2([2,1,2,1,2,0])
    sort_colors2([0,0,1,2,2,2,0,0,0])
