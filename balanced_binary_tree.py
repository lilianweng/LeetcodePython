#!/usr/bin/env python
'''
Leetcode: Balanced Binary Tree

Given a binary tree, determine if it is height-balanced.
For this problem, a height-balanced binary tree is defined as a binary tree in which the depth of the two subtrees of every node never differ by more than 1.
'''

from __future__ import division
import random
from BinaryTree import Node, SampleTreeRoot


# return, True/False (whether balanced), height of the tree
import math
def balanced_binary_tree(root):
    if not root:
        return True, 0
    if not root.left and not root.right:
        return True, 1
    
    balance_left, left = balanced_binary_tree(root.left)
    balance_right, right = balanced_binary_tree(root.right)
    is_balanced = (math.fabs(left-right) <=1 and balance_left and balance_right)
    tree_height = max(left, right) + 1
    return is_balanced, tree_height


if __name__ == '__main__':
    
    root = SampleTreeRoot
    print root
    print balanced_binary_tree(root)


