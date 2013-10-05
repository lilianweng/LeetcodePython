#!/usr/bin/env python
'''
Leetcode: Same Tree
Given two binary trees, write a function to check if they are equal or not.
Two binary trees are considered equal if they are structurally identical and the nodes have the same value.
'''
from __future__ import division
import random
from BinaryTree import Node


def is_same_tree(root1, root2):
    if (not root1.left) and not (root1.right) and (not root2.left) and not (root2.right) and root1.value == root2.value:
        return True
    
    if (root1.value != root2.value) or (root1.left and not root2.left) or (not root1.left and root2.left) or (root1.right and not root2.right) or (not root1.right and root2.right): return False
    
    left = is_same_tree(root1.left, root2.left) \
           if root1.left and root2.left \
           else True
    right = is_same_tree(root1.right, root2.right) \
            if root1.right and root2.right \
            else True
    return left and right


if __name__ == '__main__':
    root1 = Node(value=5,
                left=Node(value=4,
                     left=Node(value=11,
                          left=Node(value=6),
                          right=Node(value=2))
                ),
                right=Node(value=8,
                     left=Node(value=13),
                     right=Node(value=4,
                        left=Node(value=5),
                        right=Node(value=1))
                )
            )
    
    root2 = Node(value=0,
                left=Node(value=4,
                     left=Node(value=11)
                ),
                right=Node(value=8,
                     left=Node(value=13),
                     right=Node(value=4)
                )
            )
    
    print is_same_tree(root1, root1)
    print is_same_tree(root1, root2)