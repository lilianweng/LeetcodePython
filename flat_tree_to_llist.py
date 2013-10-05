#!/usr/bin/env python
'''
Leetcode: Flatten Binary Tree to Linked List
Given a binary tree, flatten it to a linked list in-place.
For example,
Given
         1
        / \
       2   5
      / \   \
     3   4   6
The flattened tree should look like:
   1
    \
     2
      \
       3
        \
         4
          \
           5
            \
             6
If you notice carefully in the flattened tree, 
each node's right child points to the next node of a pre-order traversal.
'''
from __future__ import division
import random
from BinaryTree import Node, root


### In-order traversal without using recursion or stack, in place
### (Morris traversal)
# 1. cur = root
# 2. if cur has no left-child
#     2.1 print cur.value
#     2.2 cur --> cur.right
# 3. else:
#     3.1 cur --> the right most child of the left subtree
#     3.2 cur --> cur.left
def morris_traversal(root):
    cur = root
    while cur:
        if cur.left is not None:
            rightmost_in_left = cur.left
            while rightmost_in_left.right:
                rightmost_in_left = rightmost_in_left.right
            rightmost_in_left.right = cur
            cur_left = cur.left
            cur.left = None
            cur = cur_left
        else: # visit right child
            # no left child, it is the turn to visit the root!
            print cur.value,
            cur = cur.right


# For each node:
# 1. cur = root
# 2. visit cur
# 3. if cur has no left-child:
#     3.1 cur = cur.right
# 4. else:
#     4.1 move cur's right-child to the rightmost child of its left subtree
#     4.2 cur = cur.left
def inplace_preorder_traversal(root):
    cur = root
    while cur:
        print cur.value,
        if cur.left:
            if cur.right:
                rightmost_in_left = cur.left
                while rightmost_in_left.right:
                    rightmost_in_left = rightmost_in_left.right
                rightmost_in_left.right = cur.right
            cur.right = None
            cur = cur.left
        else:
            cur = cur.right


def flatten(root):
    cur = root
    # pre-order in-place traversal
    while cur:
        #print cur.value,
        if cur.left:
            if cur.right:
                rightmost_in_left = cur.left
                while rightmost_in_left.right:
                    rightmost_in_left = rightmost_in_left.right
                rightmost_in_left.right = cur.right
            cur.right = None
            cur = cur.left
        else:
            cur = cur.right
    print root
    # move all left child to be right child
    cur = root
    while cur:
        if cur.left:
            cur.right = cur.left
            cur.left = None
        cur = cur.right
    print root


if __name__ == '__main__':
    print root
    flatten(root)



