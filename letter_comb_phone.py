#!/usr/bin/env python
'''
Leetcode: Letter Combinations of a Phone Number
Given a digit string, return all possible letter combinations that the number could represent.

A mapping of digit to letters:
1() 2(abc) 3(def)
4(ghi) 5(jkl) 6(mno)
7(pgrs) 8(tuv) 9(wxyz)

Input:Digit string "23"
Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
'''
from __future__ import division
import random

num2lett = {
    1:'', 2:'abc',3:'def', 
    4:'ghi',5:'jkl',6:'mno', 
    7:'pqrs',8:'tuv',9:'wxyz', 
    0:' '}

def letter_comb_phone(num2lett, digits):
    ret = ['']
    for d in digits:
        if (not d.isdigit()) or (int(d) not in num2lett): return []
        cands = list(num2lett[int(d)])
        ret = [x+y for x in ret for y in cands]
    return ret



''' What if we have a dictionary? '''
def get_cands(num2lett, digits):
    ret = ['']
    for d in digits:
        if (not d.isdigit()) or (int(d) not in num2lett): return []
        cands = list(num2lett[int(d)])
        ret = [x+y for x in ret for y in cands]
    return ret

def phone_mapping(num2lett, dictionary, number): 
    if len(number) == 0: yield []
    else:
        n = len(number)
        for i in range(1,n+1):
            sub = number[:i]
            words = [c for c in get_cands(num2lett, sub) if c in dictionary]
            if not words: continue
            for w in words:
                for other_words in phone_mapping(num2lett, dictionary, number[i:]):
                    yield [w] + other_words


''' How to optimize it? Mometization '''
memo = {}
def phone_mapping2(num2lett, dictionary, number, words): 
    global memo
    
    if len(number) == 0: return True
    
    if number in memo: return memo[number]
    
    n = len(number)
    can_split = False
    for i in range(1,n+1):
        sub = number[:i]
        cands = [c for c in get_cands(num2lett, sub) if c in dictionary]
        if not cands: continue
        if phone_mapping2(num2lett, dictionary, number[i:], words):
            words.append(cands[0])
            can_split = True
            memo[number] = True
            break
    memo[number] = can_split
    return can_split


if __name__ == '__main__':
    #print letter_comb_phone("23052")
    #print letter_comb_phone("47825")
    words = []
    phone_mapping2(num2lett, set(['a','aa','aaa','aaaa']), '22223', words)
    print memo
    print words


