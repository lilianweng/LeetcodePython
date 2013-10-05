#!/usr/bin/env python
'''
Leetcode: Valid Binary Search Tree
Given a binary tree, determine if it is a valid binary search tree (BST).

Assume a BST is defined as follows:
The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.
'''
from __future__ import division
import random
from BinaryTree import Node, BST, root


def valid_BST(root):
    if not root.left and not root.right:
        return True
    
    left_valid = right_valid = False
    
    if root.left:
        print root.left.value, '<=', root.value
        if root.left.value <= root.value:
            left_valid = valid_BST(root.left)
    
    if root.right:
        print root.value, '<=', root.right.value
        if root.right.value >= root.value:
            right_valid = valid_BST(root.right)
    
    return left_valid and right_valid


if __name__ == '__main__':
    BST2 = Node(value=5,
                left=Node(value=2,
                     left=Node(value=1),
                     right=Node(value=3)
                ),
                right=Node(value=9,
                     left=Node(value=7),
                     right=Node(value=16,
                        right=Node(value=15)
                     )
                )
            )
    
    print valid_BST(BST)
    print valid_BST(BST2)
    print valid_BST(root)


