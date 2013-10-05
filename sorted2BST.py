#!/usr/bin/env python

from __future__ import division
import random
from BinaryTree import Node as TreeNode
from LinkedList import Node

'''
Leetcode: Convert Sorted Array to Binary Search Tree
'''
def convert2BST(arr):
    n = len(arr)
    if n == 0: return None
    if n == 1: return TreeNode(value=arr[0])
    idx = n//2
    root = TreeNode(
              value = arr[idx],
              left = convert2BST(arr[:idx]),
              right = convert2BST(arr[idx+1:])
          )
    return root


'''
Leetcode: Convert Sorted List to Binary Search Tree
'''
# bottom-up
def convert2BST_link(node, start, end):
    if start > end or node is None:
        return None, node
    mid = (start+end)//2
    left_tree, node = convert2BST_link(node, start, mid-1)
    root = TreeNode(value = node.value)
    node = node.next
    right_tree, node = convert2BST_link(node, mid+1, end)
    root.left = left_tree
    root.right = right_tree
    return root, node


if __name__ == '__main__':
    a = [1,3,5,6,89,100,200,201]
    print convert2BST(a)
    
    l = Node(value=1, next=Node(value=3, next=Node(value=5,next=Node(value=6, next=Node(value=89,next=Node(value=100,next=Node(value=200,next=Node(value=201))))))))
    print l
    print convert2BST_link(l,0,7)[0]


