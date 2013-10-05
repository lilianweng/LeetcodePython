#!/usr/bin/env python
'''
Leetcode: Sum Root to Leaf Numbers
Given a binary tree containing digits from 0-9 only, each root-to-leaf path could represent a number.
An example is the root-to-leaf path 1->2->3 which represents the number 123.
Find the total sum of all root-to-leaf numbers.
For example,
        1
       / \
      2   3
    The root-to-leaf path 1->2 represents the number 12.
    The root-to-leaf path 1->3 represents the number 13.
Return the sum = 12 + 13 = 25.
'''
from __future__ import division
import random
from BinaryTree import Node


def sum_root_to_leaf(root, cur_path_num, sum):
    if not root.left and not root.right:
        cur_path_num = cur_path_num*10 + root.value
        print '+', cur_path_num
        sum += cur_path_num
        return sum
    
    cur_path_num = cur_path_num*10 + root.value
    if root.left:
        sum = sum_root_to_leaf(root.left, cur_path_num, sum)
    if root.right:
        sum = sum_root_to_leaf(root.right, cur_path_num, sum)
    return sum


# Is it possible to do this iteratively?
def sum_root_to_leaf_iter():
    pass


if __name__ == '__main__':
    root = Node(1, 
                left=Node(2, left=Node(4), right=Node(1,right=Node(6))), 
                right=Node(3, right=Node(5)))
    
    print sum_root_to_leaf(root, 0, 0)
    
