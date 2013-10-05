#!/usr/bin/env python
'''
Leetcode: Swap Nodes in Pairs
Given a linked list, swap every two adjacent nodes and return its head.
For example, Given 1->2->3->4, you should return the list as 2->1->4->3.
Your algorithm should use only constant space. 
You may not modify the values in the list, only nodes itself can be changed.
'''
from __future__ import division
import random
from LinkedList import Node


def swap_pairs(head):
    print head
    if not head or not head.next:
        return head
    first_prev = None
    first = head
    second = head.next
    while first and second:
        # swap
        first.next = second.next
        second.next = first
        if first_prev:
            first_prev.next = second
        else:
            # first pair, change root
            head = second
        # move to the next pair
        if not first or not first.next: break
        first_prev = first
        first = first.next
        second = first.next
    
    print head
    return head


if __name__ == '__main__':
    l1 = Node(1, Node(2, Node(3)))
    l2 = Node(2, Node(3, Node(4, Node(5, Node(6, Node(7))))))
    swap_pairs(l1)
    swap_pairs(l2)


