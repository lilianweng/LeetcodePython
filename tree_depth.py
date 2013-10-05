#!/usr/bin/env python

from __future__ import division
import random
from BinaryTree import Node, SampleTreeRoot

'''
Leetcode: Maximum Depth of Binary Tree
Given a binary tree, find its maximum depth. The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.
'''
def max_tree_depth_recur(root):
    if not root:
        return 0
    if not root.left and not root.right:
        return 1
    else:
        left_h = max_tree_depth_recur(root.left) if root.left else 0
        right_h = max_tree_depth_recur(root.right) if root.right else 0
        return max(left_h+1, right_h+1)


# level-order traversal
def max_tree_depth_iter(root):
    if not root: return 0
    cur_level = [root] # queue
    h = 0
    while cur_level:
        h += 1
        # traverse this level!
        next_level = []
        for node in cur_level:
            if node.left: next_level.append(node.left)
            if node.right: next_level.append(node.right)
        cur_level = next_level
    return h


### post-order traversal; check the stack depth
def max_tree_depth_iter2(root):
    if not root: return 0
    h = 0
    stack = [root]
    prev = None
    while stack:
        curr = stack[-1]
        if (not prev) or (prev.left == curr) or (prev.right == curr):
            if curr.left: stack.append(curr.left)
            elif curr.right: stack.append(curr.right)
        elif curr.left == prev:
            if curr.right: stack.append(curr.right)
        else:
            stack.pop()
        prev = curr
        h = max(h, len(stack))
    return h


'''
Leetcode: Minimum Depth of Binary Tree
Given a binary tree, find its minimum depth. The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.
'''
def min_tree_depth_recur(root):
    if not root.left or not root.right:
        return 1
    else:
        left_dep = min_tree_depth_recur(root.left)
        right_dep = min_tree_depth_recur(root.right)
        return min(left_dep, right_dep)+1


# level-order traversal
def min_tree_depth_iter(root):
    if not root: return 0
    cur_level = [root] # queue
    h = 0
    while cur_level:
        h += 1
        # traverse this level!
        next_level = []
        for node in cur_level:
            if not node.left or not node.right:
                return h
            else:
                next_level.append(node.left)
                next_level.append(node.right)
        cur_level = next_level
    return h


### post-order traversal
def min_tree_depth_iter2(root):
    stack = [root]
    prev = None
    h = None
    while stack:
        curr = stack[-1]
        if (not prev) or (prev.left == curr) or (prev.right == curr):
            if curr.left: stack.append(curr.left)
            elif curr.right: stack.append(curr.right)
        elif (curr.left == prev):
            if curr.right: stack.append(curr.right)
        else:
            if not curr.left and not curr.right: # a leave node
                if not h: h = len(stack)
                else: h = min(h, len(stack))
            stack.pop()
        prev = curr
    return h


if __name__ == '__main__':
    print SampleTreeRoot
    print max_tree_depth_recur(SampleTreeRoot)
    print max_tree_depth_iter(SampleTreeRoot)
    print max_tree_depth_iter2(SampleTreeRoot)
    print
    print min_tree_depth_recur(SampleTreeRoot)
    print min_tree_depth_iter(SampleTreeRoot)
    print min_tree_depth_iter2(SampleTreeRoot)
    
    
