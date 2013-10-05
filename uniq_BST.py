#!/usr/bin/env python


from __future__ import division
import random
from BinaryTree import Node

'''
Leetcode: Unique Binary Search Trees
Given n, how many structurally unique BST's (binary search trees) that store values 1...n?
For example, Given n = 3, there are a total of 5 unique BST's.
       1         3     3      2      1
        \       /     /      / \      \
         3     2     1      1   3      2
        /     /       \                 \
       2     1         2                 3
'''
# P(n) = #structurally unique BST
# Pick a root r from 1,2,...,n
# 1,..,r-1 ---> P(r-1)
# r+1,...,n ---> P(n-r)
# P(n) = sum(P(r-1)*P(n-r) for r=1,2,...,n)
# So we have P(n) = (2n)!/n!*(n+1)! <--- catalan number
def uniq_BST(n):
    P = {0:1, 1:1}
    for i in range(2,n+1):
        P[i] = 0
        for root in range(1,i+1):
            P[i] += P[root-1] * P[i-root]
    return P[n]


'''
Leetcode: Unique Binary Search Trees II
Given n, generate all structurally unique BST's (binary search trees) that store values 1...n.
For example, given n = 3, your program should return all 5 unique BST's shown below.
       1         3     3      2      1
        \       /     /      / \      \
         3     2     1      1   3      2
        /     /       \                 \
       2     1         2                 3
'''
def gen_uniq_BST(i,j):
    if i > j: yield None
    elif i == j: yield Node(i)
    else:
        for root in range(i,j+1):
            node = Node(root)
            for left_node in gen_uniq_BST(i,root-1):
                for right_node in gen_uniq_BST(root+1,j):
                    node.left = left_node
                    node.right = right_node
                    yield node

def uniq_BST_II(n):
    print uniq_BST(n)
    total = 0
    for tree in gen_uniq_BST(1,n):
        print tree
        total += 1
    print 'total:', total


if __name__ == '__main__':
    uniq_BST_II(4)


