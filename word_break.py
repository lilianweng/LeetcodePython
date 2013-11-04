#!/usr/bin/env python
'''
http://thenoisychannel.com/2011/08/08/retiring-a-great-interview-problem/
'''
from __future__ import division
import random


'''
Leetcode: Word Break
Given a string s and a dictionary of words dict, determine if s can be segmented into a space-separated sequence of one or more dictionary words.
For example, given 
s = "leetcode", 
dict = ["leet", "code"].
Return true because "leetcode" can be segmented as "leet code".
'''
def wordbreak(s, words):
    if len(s) == 0: return True
    # Test all prefixes
    for i in range(1, len(s)+1):
        sub = s[:i]
        if not sub in words: continue
        if wordbreak(s[i:], words):
            return True
    return False


### DP? O(n^2)
# cut(i) = s[:i] can be splitted
# cut(i+1) = OR{cut(j) and s[j:i] is a word for 0 <= j < i}
def wordbreak_DP(s, words):
    words = set(words)
    cut = {0: True}
    for i in range(1,len(s)+1):
        cut[i] = False
        for j in range(i):
            if cut[j] and s[j:i] in words:
                cut[i] = True
                break
    return cut[len(s)]


memo = {}
def wordbreak_memo(s, words):
    if s == '': return True
    global memo
    if s in memo: return memo[s]
    for i in range(1,len(s)+1):
        sub = s[:i]
        if not sub in words: continue
        if wordbreak_memo(s[i:], words):
            memo[s] = True#; print memo
            return True
    return False

'''
Leetcode: Word Break II
Given a string s and a dictionary of words dict, add spaces in s to construct a sentence where each word is a valid dictionary word. Return all such possible sentences.
For example, given
s = "catsanddog",
dict = ["cat", "cats", "and", "sand", "dog"].
A solution is ["cats and dog", "cat sand dog"].
'''
# ~O(exponential)
def wordbreak2_generator(s, words):
    if len(s) == 0: yield []
    else:
        # Test all prefixes
        for i in range(1, len(s)+1):
            sub = s[:i]
            if not sub in words: continue
            for others in wordbreak2_generator(s[i:], words):
                yield [sub] + others

def wordbreak2(s, words):
    words = set(words)
    for combo in wordbreak2_generator(s, words):
        print combo


'''
What if we allow unmatched characters, but they should be as few as possible.
Capitalize unmatched string.
For example, given
s = "ithinktomlikescatsanddog",
dict = ["think", "like", "likes", "cat", "cats", "and", "sand", "dog"].
A solution is ["I think TOM likes cats and dog", "I think TOM likes cat sand dog"].
'''
def wordbreak3_match(s, words):
    global MAX_UNMATCHED
    if s == '':
        yield 0, ''
    else:
        for u in range(MAX_UNMATCHED+1):
            sub = s[u:]
            for i in range(1, len(sub)+1):
                first = sub[:i]
                if first not in words: continue
                for unmatched, split in wordbreak3_match(sub[i:], words):
                    yield unmatched+u, s[:u].upper() + ' '+ first + ' ' + split

MAX_UNMATCHED = 0
def wordbreak3(s, words):
    global MAX_UNMATCHED
    MAX_UNMATCHED = len(s)
    
    min_unmatched = len(s)
    best_split = []
    for u, split in wordbreak3_match(s, words):
        if u < min_unmatched:
            min_unmatched = u
            best_split = split
    print best_split
    return best_split



if __name__ == '__main__':
    '''
    s = "catsanddogseat"
    words = set(["cat", "cats", "and", "sand", "dog", "dogs", "eat", "seat"])
    print wordbreak(s, words)
    print wordbreak_DP(s, words)
    print wordbreak_memo(s, words)
    wordbreak2(s, words)
    '''
    
    s = "ithinktomlikescatsanddog"
    dict = ["think", "like", "likes", "cat", "cats", "and", "sand", "dog"]
    wordbreak3(s, dict)
    
    
