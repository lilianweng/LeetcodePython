#!/usr/bin/env python
'''
Leetcode: Convert Binary Search Tree (BST) to Sorted Doubly-Linked List
'''
from __future__ import division
import random
from BinaryTree import *


def get_tail(node):
    while node.right:
        node = node.right
    return node


def convert(root):
    if not root: return None
    left_list = convert(root.left)
    right_list = convert(root.right)
    
    if left_list:
        tail = get_tail(left_list)
        tail.right = root
        root.left = tail
    
    if right_list:
        right_list.left = root
        root.right = right_list
    
    if left_list: return left_list
    else: return root


if __name__ == '__main__':
    print BST
    head = convert(BST)
    
    # to right
    node = head
    while node.right:
        print node.value, '->',
        node = node.right
    print node.value
    
    # to right
    while node.left:
        print node.value, '<-',
        node = node.left
    print node.value



