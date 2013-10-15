#!/usr/bin/env python
'''
Leetcode: Scramble String
Given a string s1, we may represent it as a binary tree by partitioning it to two non-empty substrings recursively.

Below is one possible representation of s1 = "great":
    great
   /    \
  gr    eat
 / \    /  \
g   r  e   at
           / \
          a   t

To scramble the string, we may choose any non-leaf node and swap its two children.
For example, if we choose the node "gr" and swap its two children, it produces a scrambled string "rgeat".
    rgeat
   /    \
  rg    eat
 / \    /  \
r   g  e   at
           / \
          a   t
We say that "rgeat" is a scrambled string of "great".
Similarly, if we continue to swap the children of nodes "eat" and "at", it produces a scrambled string "rgtae".
    rgtae
   /    \
  rg    tae
 / \    /  \
r   g  ta  e
       / \
      t   a
We say that "rgtae" is a scrambled string of "great".
Given two strings s1 and s2 of the same length, determine if s2 is a scrambled string of s1.
'''
from __future__ import division
import random


### 3-dimensional DP:
# f(i,j,n) is true iff substring s1[i:i+n] and s2[j:j+n] are scrambled
# f(i,j,n) |= ((f(i,j,m) && f(i+m,j+m,n-m)) || f(i,j+n-m,m) && f(i+m,j,n-m)) 
#             for 1 < m < n
def scramble_str_DP(s1, s2):
    if len(s1) != len(s2): return False
    f = {}
    l = len(s1)
    for i in range(l):
        for j in range(l):
            f[i,j,0] = True
            f[i,j,1] = (s1[i] == s2[j])
    
    #print f
    for n in range(2,l+1):
        for i in range(l-n+1):
            for j in range(l-n+1):
                f[i,j,n] = False
                for m in range(1,n):
                    #print i,j,m,'-',i+m,j+m,n-m,'-',i,j+n-m,m,'-',i+m,j,n-m
                    f[i,j,n] |= (f[i,j,m] and f[i+m,j+m,n-m]) or (f[i,j+n-m,m] and f[i+m,j,n-m])
    
    #print f
    return f[0,0,l]


# Only works when there is no duplication!!
# index s2 based on the order of characters in s1
# can always find a partition so that all the numbers in one part are smaller than all the numbers in the other part. Do this partition recursively until only one character is left in one partition.
# For example, s1='great', s2='rgtae', index s2=[1,0,4,3,2]
# 10432 --> 10 | 432
# 10 --> 1 | 0
# 432 --> 4 | 32
# 32 --> 3 | 2
# True!
# For example, s1='tiger', s2='tgrie', index s2=[0,2,4,1,3]
# 02413 --> 0 | 2413
# 2413 --> False!
def partition(L):
    if len(L) == 1: return True
    for i in range(1,len(L)):
        x, y = L[:i], L[i:]
        if max(x) < min(y) or max(y) < min(x):
            #print L, '->', x, y
            return partition(x) and partition(y)
    return False


### @Only work without duplications
def scramble_str1(s1, s2):
    ch2idx = dict((ch,i) for i,ch in enumerate(s1))
    l = [ch2idx[ch] for ch in s2]
    return partition(l)


### Similarly but compare character sets
# s1 = 'attention', s2 = 'itnottena'
# atten | tion <---> itno | ttena
# a | tten <---> tten | a
# ti | on <---> it | no
# o | n <---> n | o
# t | i <---> i | t
def elem(s):
    return ''.join(sorted(s))

def same_elems(s1, s2):
    return elem(s1) == elem(s2)

def matching(s1, s2):
    #print s1, s2
    if s1 == s2: return True
    if len(s1) != len(s2): return False
    for i in range(1,len(s1)):
        x1, y1 = s1[:i], s1[i:]
        x2, y2 = s2[:i], s2[i:]
        x3, y3 = s2[-i:], s2[:-i]
        
        if same_elems(x1,x2) and same_elems(y1,y2) and \
           matching(x1, x2) and matching(y1, y2):
            return True
        
        if same_elems(x1,x3) and same_elems(y1,y3) and \
           matching(x1,x3) and matching(y1,y3):
            return True
    
    return False


def scramble_str2(s1, s2):
    return matching(s1, s2)


### @Only work without duplications
def scramble_str_merge(s1, s2):
    ch2idx = dict((ch,i) for i,ch in enumerate(s1))
    l = [ch2idx[ch] for ch in s2]
    # a stack of interval
    stack = [(i,i) for i in l]
    stack_merged = []
    while stack:
        cur = stack.pop() # pop out an interval
        if not stack_merged:
            stack_merged.append(cur)
        else:
            while stack_merged and (stack_merged[-1][0] - cur[1] == 1 or \
                              stack_merged[-1][1] + 1 == cur[0]):
                other = stack_merged.pop()
                cur = (min(cur[0],other[0]), max(cur[1],other[1]))
            stack_merged.append(cur)
    return len(stack_merged) == 1


'''
It is proposed in this blog a similar merge and check approach, instead of merge them as integer intervals by their index, we can merge its sub strings.

For string str2: aabcdbcba, we create a stack S1 to stores each of its characters (as a string) while another stack S2 to be the auxiliary stack.
S1:["a","a","b","c","d","b","c","b","a"] S2:[]
The algorithm goes as follows:
1) Build two strings comStr1 = S1.peek() + S2.peek() and comStr2 = S2.peek() + S1.peek()
  1.1) if str1 contains neither of them, push S1.pop to S2.
  1.2) if Str1 contains only one of them, push the combined string to S1. Before the push one needs to first do S1.pop and S2.pop.
  1.3) if Str1 contains both of them
    1.3.1) if comStr1 == comStr2, then push either combined string to S1. Before the push one needs to first do S1.pop and S2.pop.
    1.3.2) if comStr1 != comStr2, then we have two candidates. In this case we need to choose the better one. We try to see if both the candidates can merge with the new S1.Peek() or S2.Peek(). This is a recursive approach. It is very similar to the Step 1) but in this case comStr1 = candidiate+S2.peek(), comStr2 = S2.peek() + candidiate (if neither of them can not merged with S2.peek(), one needs to repeat the process by replacing S2.peek() with s1.peek()). After the comparison, there should be only one candidate left. Then one can push it to S1. There is only one case where both multiple candidates can be observed, that is, all the candidates are the same as the S1, that is the end of the comparison.
2) In the end, that is, when S1 is empty, check if S2 contains only one element.
'''
def scramble_str_merge2(s1, s2):
    pass


if __name__ == '__main__':
    print scramble_str_DP('great', 'rgtae')
    print scramble_str_DP('tiger', 'tgrie')
    print scramble_str_DP('lawyers', 'ywlaser')
    print scramble_str_DP('lawyers', 'ryalwse')
    print scramble_str_DP('attention', 'itnottena')
    print scramble_str_DP('attention', 'tnoatitne')
    print
    print scramble_str2('great', 'rgtae')
    print scramble_str2('tiger', 'tgrie')
    print scramble_str2('lawyers', 'ywlaser')
    print scramble_str2('lawyers', 'ryalwse')
    print scramble_str2('attention', 'itnottena')
    print scramble_str2('attention', 'tnoatitne')


