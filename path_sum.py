#!/usr/bin/env python

from __future__ import division
import random
from BinaryTree import Node, root, root_with_id

'''
Leetcode: Path Sum
Given a binary tree and a sum, determine if the tree has a root-to-leaf path such that adding up all the values along the path equals the given sum.
For example: Given the below binary tree and sum = 22,
              5
             / \
            4   8
           /   / \
          11  13  4
         /  \      \
        7    2      1
return true, as there exist a root-to-leaf path 5->4->11->2 which sum is 22.
'''
def path_sum(root, val):
    if not root: return False
    if not root.left and not root.right: return val == root.value
    return path_sum(root.left, val-root.value) or path_sum(root.right, val-root.value)


'''
Leetcode: Path Sum II
Given a binary tree and a sum, find all root-to-leaf paths where each path's sum equals the given sum.
For example: Given the below binary tree and sum = 22,
              5
             / \
            4   8
           /   / \
          11  13  4
         /  \    / \
        6    2  5   1
return
[
   [5,4,11,2],
   [5,8,4,5]
]
'''
def path_finder(root, val, path, paths):
    if not root:
        return False
    
    if not root.left and not root.right:
        if root.value == val:
            path.append(root.value)
            paths.append(path)
            return True
        else:
            return False
    
    left = path_finder(root.left, val-root.value, path+[root.value], paths)
    right = path_finder(root.right, val-root.value, path+[root.value], paths) # make sure it can be executed!
    return left or right


def path_sum2(root, val):
    paths = []
    path_finder(root, val, [], paths)
    print 'sum:', val
    print 'paths:', paths


if __name__ == '__main__':
    path_sum2(root_with_id, 4)
    path_sum2(root_with_id, -4)
    
    path_sum2(root, 22)
    path_sum2(root, 26)


