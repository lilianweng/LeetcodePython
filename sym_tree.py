#!/usr/bin/env python
'''
Leetcode: Symmetric Tree
Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).
For example, this binary tree is symmetric:
    1
   / \
  2   2
 / \ / \
3  4 4  3
But the following is not:
    1
   / \
  2   2
   \   \
   3    3
Note: Bonus points if you could solve it both recursively and iteratively.
'''
from __future__ import division
import random
from BinaryTree import Node


# Recursive: the left and right tree are same when 
#            left and right children are swapped.
def sym_tree_recur(root):
    left_tree = root.left
    right_tree = root.right
    return is_same_tree_sym(left_tree, right_tree)

def is_same_tree_sym(root1, root2):
    # whether root is None
    if not root1 and not root2: return True
    elif not root1 or not root2: return False
    
    # Both roots have no child and values are same
    if not root1.left and not root2.left and \
       not root1.right and not root2.right and \
       root1.value == root2.value: return True
    
    # Roots have different #children
    if (root1.value != root2.value) or \
       ((not root1.left)^(not root2.right)) or \
       ((not root1.right)^(not root2.left)): return False
    
    left = is_same_tree_sym(root1.left, root2.right) \
           if root1.left and root2.right \
           else True
    right = is_same_tree_sym(root1.right, root2.left) \
            if root1.right and root2.left \
            else True
    return left and right


## Iterative: pre-order traversal of the left and right sub-trees
# push in slightly different order for left and right trees.
def sym_tree_iter(root):
    lstack = [root.left]
    rstack = [root.right]
    while lstack or rstack:
        l = lstack.pop()
        r = rstack.pop()
        if not l and not r: return True
        if not l or not r: return False
        if l.value != r.value: return False
        lstack.append(l.right)
        lstack.append(l.left)
        rstack.append(r.left)
        rstack.append(r.right)
    return True



if __name__ == '__main__':
    root1 = Node(1, 
              left=Node(2, left=Node(4), right=Node(3)), 
              right=Node(2, left=Node(3), right=Node(4)))
    root2 = Node(1, 
              left=Node(2, right=Node(3)), 
              right=Node(2, right=Node(3)))
    
    print sym_tree_recur(root1)
    print sym_tree_recur(root2)
    
    print sym_tree_iter(root1)
    print sym_tree_iter(root2)
