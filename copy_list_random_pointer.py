#!/usr/bin/env python
'''
Leetcode: Copy List with Random Pointer
A linked list is given such that each node contains an additional random pointer 
which could point to any node in the list or null. Return a deep copy of the list.
'''

from __future__ import division
import random
import LinkedList


class Node(LinkedList.Node):
    def __init__(self, value, next=None, prev=None, randp=None):
        super(Node, self).__init__(value, next, prev)
        self.randp = randp
    def __str__(self):
        if self.randp is None: s = '[%d]' % self.value
        else: s = '[%d,%d]' % (self.value, self.randp.value)
        if self.next:
            s += '->(%s)' % str(self.next)
        return s

# Brute-force
# create the list first and then set up the pointer
def copylist(head):
    new_head = Node(head.value)
    # Copy the list
    prev_n = new_head
    node = head.next
    while node:
        n = Node(node.value)
        prev_n.next = n
        prev_n = n
        node = node.next
    
    # Assign pointer
    node = head
    new_node = new_head
    while node:
        if node.randp:
            # locate the pointer
            h = head
            newh = new_head
            while h != node.randp:
                h = h.next
                newh = newh.next
            new_node.randp = newh
        node = node.next
        new_node = new_node.next
    print 'Orig:', head
    print 'Copy:', new_head


if __name__ == '__main__':
    n6 = Node(6)
    n5 = Node(5, n6)
    n4 = Node(4, n5)
    n3 = Node(3, n4)
    n2 = Node(2, n3)
    n1 = Node(1, n2)
    n1.randp = n4
    n2.randp = n4
    n4.randp = n6
    n5.randp = n3
    
    copylist(n1)
    
    
