#!/usr/bin/env python


from __future__ import division
import random


'''
Leetcode: 3Sum

Given an array S of n integers, are there elements a, b, c in S such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

Note:
Elements in a triplet (a,b,c) must be in non-descending order. (ie, a ? b ? c)
The solution set must not contain duplicate triplets.
    For example, given array S = {-1 0 1 2 -1 -4},
    A solution set is:
    (-1, 0, 1)
    (-1, -1, 2)
http://leetcode.com/2010/04/finding-all-unique-triplets-that-sums.html
'''
# ~ O(n^2)
def three_sum(s):
    s = sorted(s) # O(nlogn)
    output = set()
    for k in range(len(s)):
        target = -s[k]
        i,j = k+1, len(s)-1
        while i < j:
            sum_two = s[i] + s[j]
            if sum_two < target:
                i += 1
            elif sum_two > target:
                j -= 1
            else:
                output.add((s[k],s[i],s[j]))
                i += 1
                j -= 1
    return output


'''
Leetcode: Two sum
Given an array of integers, find two numbers such that they add up to a specific target number.
The function twoSum should return indices of the two numbers such that they add up to the target, where index1 must be less than index2. Please note that your returned answers (both index1 and index2) are not zero-based.
You may assume that each input would have exactly one solution.
Input: numbers={2, 7, 11, 15}, target=9
Output: index1=1, index2=2
'''
def two_sum(L, target):
    L = sorted(L)
    i = 0; j = len(L)-1
    while i < j:
        if L[i]+L[j] == target:
            return i+1, j+1
        elif L[i]+L[j] > target:
            j -= 1
        else:
            i += 1
    return -1,-1


# O(n^(k-1))
def k_sum(s, k, target):
    s = sorted(s) # O(nlogn)
    if k == 0:
        yield []
    
    elif k == 1:
        if target in set(s): yield [target]
    
    elif k == 2:
        i = 0; j = len(s)-1
        while i < j:
            sum_two = s[i] + s[j]
            if sum_two < target: i += 1
            elif sum_two > target: j -= 1
            else:
                yield [s[i], s[j]]
                i += 1
                j -= 1
    else:
        for i in range(len(s)):
            next_target = target - s[i]
            for p in k_sum(s[i+1:], k-1, next_target):
                yield [s[i]] + p


if __name__ == '__main__':
    #print three_sum([-1, 0, 1, 2, -1, -4])
    #for p in k_sum([1, 0, -1, 0, -2, 2, 3, 5, -3], 4, 0): print p
    print two_sum([2, 7, 11, 15, 3], 13)
