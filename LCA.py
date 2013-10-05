#!/usr/bin/env python
'''
Leetcode: Lowest common ancesters
http://leetcode.com/2011/07/lowest-common-ancestor-of-a-binary-search-tree.html
http://leetcode.com/2011/07/lowest-common-ancestor-of-a-binary-tree-part-i.html
http://leetcode.com/2011/07/lowest-common-ancestor-of-a-binary-tree-part-ii.html
'''
from __future__ import division
import random
from BinaryTree import Node, BST, root


### We traverse from the bottom, and once we reach a node which matches one of the two nodes, we pass it up to its parent. The parent would then test its left and right subtree if each contain one of the two nodes. If yes, then the parent must be the LCA and we pass its parent up to the root. If not, we pass the lower node which contains either one of the two nodes (if the left or right subtree contains either p or q), or NULL (if both the left and right subtree does not contain either p or q) up.
# O(n)
def lca(root, a, b):
    if not root: return None
    if root.value == a or root.value == b: return root
    left = lca(root.left, a, b)
    right = lca(root.right, a, b)
    if left and right: # if p and q are on both sides
        return root
    else: # either a/b is on one side OR a/b is not in L&R subtrees
        return left if left else right


### With parent pointer
# find the height h(a), h(b)
# move the lower node b up by h(a)-h(b) steps
# move a and b up together until a=b
def lca_parent(root, node_a, node_b):
    h_a = find_height(root, node_a)
    h_b = find_height(root, node_b)
    if h_b > h_a:
        node_a, node_b = node_b, node_a
        h_a,h_b = h_b,h_a
    for _ in range(h_b - h_a):
        node_b = node_b.parent
    while node_a != node_b:
        node_a = node_a.parent
        node_b = node_b.parent
    return node_a

def find_height(root, node):
    h = 0
    while node:
        node = node.parent
        h += 1
    return h


# 1. Both nodes are to the left of the tree.
# 2. Both nodes are to the right of the tree.
# 3. One node is on the left while the other is on the right.
# 4. When the current node equals to either of the two nodes, this node must be the LCA too.
# O(logn)
def lca_BST(root, a, b):
    while root:
        if a <= root.value <= b:
            return root
        elif min(a,b) < root.value:
            root = root.left
        elif max(a,b) > root.value:
            root = root.right
    return None


if __name__ == '__main__':
    print lca_BST(BST, 1,3)
    print lca_BST(BST, 9,16)


