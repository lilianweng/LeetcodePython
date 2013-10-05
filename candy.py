#!/usr/bin/env python
'''
Leetcode:
There are N children standing in a line. Each child is assigned a rating value.

You are giving candies to these children subjected to the following requirements:

Each child must have at least one candy.
Children with a higher rating get more candies than their neighbors.
What is the minimum candies you must give?

'''
from __future__ import division
import random

def candy(scores):
    print scores
    n = len(scores)
    candies = [1]*n
    # left --> right
    # add one if score > child on the right
    for i in range(1,n):
        if scores[i] > scores[i-1]:
            candies[i] = max(candies[i], candies[i-1]+1)
        elif scores[i] == scores[i-1]:
            candies[i] = max(candies[i], candies[i-1])
    print candies
    # right --> left
    # add one if score > child on the left
    for i in reversed(range(n-1)):
        if scores[i] > scores[i+1]:
            candies[i] = max(candies[i], candies[i+1]+1)
        elif scores[i] == scores[i+1]:
            candies[i] = max(candies[i], candies[i+1])
    print candies
    return candies

if __name__ == '__main__':
    candy([1,2,3,7,2,0,0,3,2,10])


