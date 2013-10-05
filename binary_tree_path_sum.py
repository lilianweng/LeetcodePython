#!/usr/bin/env python
'''
Leetcode: Binary Tree Maximum Path Sum
Given a binary tree, find the maximum path sum.
The path may start and end at any node in the tree.
For example: Given the below binary tree,
       1
      / \
     2   3
Return 6.
2-1-3
'''

from __future__ import division
import random
from BinaryTree import Node, SampleTreeRoot

# L(node) = max sum path in node's left sub-tree
# R(node) = max sum path in node's right sub-tree
# L(node) = node.val + max{L(node.left), R(node.left)}
# R(node) = node.val + max{L(node.right), R(node.right)}
# max{L(node)+R(node) for any node in the tree}
def subtree_maxsum_path(node, is_left=True, Lpath={}, Rpath={}):
    if is_left:
        # left sub-tree
        if not node.left:
            Lpath[node.id] = 0
            return 0
        else:
            Lpath[node.id] = node.value + max(
                subtree_maxsum_path(node.left, True, Lpath, Rpath),
                subtree_maxsum_path(node.left, False, Lpath, Rpath)
            )
            return Lpath[node.id]
    else:
        # right sub-tree
        if not node.right:
            Rpath[node.id] = 0
            return 0
        else:
            Rpath[node.id] = node.value + max(
                subtree_maxsum_path(node.right, True, Lpath, Rpath),
                subtree_maxsum_path(node.right, False, Lpath, Rpath)
            )
            return Rpath[node.id]


def maxsum_path(root):
    Lpath = {}
    Rpath = {}
    subtree_maxsum_path(root, True, Lpath, Rpath)
    subtree_maxsum_path(root, False, Lpath, Rpath)
    print 'Left-path:', Lpath
    print 'Right-path:', Rpath
    path2sum = dict((i, Lpath[i]+Rpath[i]) for i in Lpath.keys())
    i = max(path2sum, key=path2sum.get)
    print 'The path going through node', i, 'with max sum', path2sum[i]
    return path2sum[i]


if __name__ == '__main__':
    print maxsum_path(SampleTreeRoot)
    
    
