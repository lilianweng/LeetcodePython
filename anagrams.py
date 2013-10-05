#!/usr/bin/env python
'''
Leetcode: Anagrams
Given an array of strings, return all groups of strings that are anagrams.
Note: All inputs will be in lower-case.
'''
from __future__ import division
import random

### Use permutation generator
def anagrams_generator(s):
    if len(s) == 1:
        yield s
    else:
        for i in range(len(s)):
            elem = s[i]
            # keep one element away
            for a in anagrams_generator(s[:i] + s[i+1:]):
                for j in range(len(a)+1):
                    # insert this element into any possible position
                    yield a[:j] + elem + a[j:]

def anagrams(s):
    print 'Anagrams of '+s+':',
    output = set([a for a in anagrams_generator(s)])
    print list(output)


### Other solution?
# Permutation with repetition?



if __name__ == '__main__':
    anagrams('aab')
    anagrams('hello')


