#!/usr/bin/env python
'''
Leetcode: Recover Binary Search Tree
Two elements of a binary search tree (BST) are swapped by mistake.
Recover the tree without changing its structure.
Note: A solution using O(n) space is pretty straight forward. Could you devise a constant space solution?
'''
from __future__ import division
import random
from BinaryTree import Node, BST

def find_outliers(root, outliers):
    if root.left:
        if root.left.value <= root.value:
            find_outliers(root.left, outliers)
        else:
            outliers.append(root.left)
    if root.right:
        if root.right.value >= root.value:
            return find_outliers(root.right, outliers)
        else:
            outliers.append(root.right)


# time ~ O(n), space ~ O(1)
def recover_BST(root):
    print root
    outliers = []
    find_outliers(root, outliers)
    x, y = outliers
    print x, y
    # swith them
    x.value, y.value = y.value, x.value
    print root


if __name__ == '__main__':
    recover_BST(BST)



