#!/usr/bin/env python

from __future__ import division
import random
from BinaryTree import Node as TreeNode

class Node(TreeNode):
    def __init__(id=0, 
                 left=None, right=None, 
                 value=None, parent=None,
                 next=None):
        TreeNode.__init__(self, id, left, right, value, parent)
        self.next = next # next right child on the same level

'''
Leetcode: Populating Next Right Pointers in Each Node
Given a binary tree
    struct TreeLinkNode {
      TreeLinkNode *left;
      TreeLinkNode *right;
      TreeLinkNode *next;
    }
Populate each next pointer to point to its next right node. If there is no next right node, the next pointer should be set to NULL.
Initially, all next pointers are set to NULL.

Note:
!!!! You may only use constant extra space !!!!
You may assume that it is a perfect binary tree (ie, all leaves are at the same level, and every parent has two children).
For example,
Given the following perfect binary tree,
         1
       /  \
      2    3
     / \  / \
    4  5  6  7
After calling your function, the tree should look like:
         1 -> NULL
       /  \
      2 -> 3 -> NULL
     / \  / \
    4->5->6->7 -> NULL
'''
def populate_next_right(root):
    leftmost_node = root
    while left_node:
        across = leftmost_node
        while across:
            # left child --> right child
            if across.left:
                across.left.next = across.right
            # right child --> next node's left child
            if across.right and across.next:
                across.right.next = across.next.left
            across = across.next
    leftmost_node = leftmost_node.left


'''
What if the given tree could be any binary tree? 
Would your previous solution still work?

Note:
You may only use constant extra space.
For example, Given the following binary tree,
         1
       /  \
      2    3
     / \    \
    4   5    7
After calling your function, the tree should look like:
         1 -> NULL
       /  \
      2 -> 3 -> NULL
     / \    \
    4-> 5 -> 7 -> NULL
'''
def populate_next_right2(root):
    node = root
    while node:
        next_level_node = None # the first node of next level
        prev = None # previous node on the same level
        while node:
            # set up the next level starting point
            if not next_level_node:
                next_level_node = node.left if node.left else node.right
            # connect all nodes on this level
            if node.left:
                if prev: prev.next = node.left
                prev = node.left
            if node.right:
                if prev: prev.next = node.right
                prev = node.right
            node = node.next
        # turn to the next level:
        node = next_level_node


if __name__ == '__main__':
    # populate_next_right()
    # populate_next_right2()
    pass


