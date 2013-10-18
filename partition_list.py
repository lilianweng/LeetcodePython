#!/usr/bin/env python
'''
Leetcode: Partition List
Given a linked list and a value x, partition it such that all nodes less than x come before nodes greater than or equal to x. You should preserve the original relative order of the nodes in each of the two partitions.

For example,
  Given 1->4->3->2->5->2 and x = 3,
  return 1->2->2->4->3->5.
'''
from __future__ import division
import random
from LinkedList import Node


def part_list(head, val):
    dummy = Node(None, next=head)
    node = head
    small = dummy # the end of "small part" of the link
    large = dummy # the end of "large part" of the link
    while node:
        print head, 'small:', small.value, 'large:', large.value,
        print 'current:', node, 'next:', node.next
        next_node = node.next
        if node.value >= val:
            large = node
        else:
            # Change the connection
            if small.next != node:
                print 'move', node.value
                node.next = small.next
                small.next = node
                large.next = next_node
            # update the tail pointer to the small part
            small = node
        node = next_node
    head = dummy.next
    print head
    return head


if __name__ == '__main__':
    L = Node(1, Node(4, Node(3, Node(2, Node(5, Node(2))))))
    part_list(L, 3)
    L = Node(5, Node(2, Node(4, Node(4, Node(1, Node(2))))))
    part_list(L, 4)

