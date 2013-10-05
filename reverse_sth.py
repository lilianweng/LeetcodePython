#!/usr/bin/env python
'''
Leetcode: Reverse Integer
Leetcode: Reverse Linked List II
Leetcode: Rotate List
Leetcode: Reverse Nodes in k-Group
'''
from __future__ import division
import random
from LinkedList import Node

'''
Reverse digits of an integer.
Example1: x = 123, return 321
Example2: x = -123, return -321
'''
# consider 0
# consider the last few digits == 0
def reverse_int(x):
    x = str(x)[::-1]
    # remove the first zero
    for i,ch in enumerate(x):
        if ch != '0': break
    x = x[i:]
    if x[-1] == '-': x = '-' + x[:-1]
    return x


'''
Leetcode: Reverse Linked List II
Reverse a linked list from position m to n. Do it in-place and in one-pass.
For example:
    Given 1->2->3->4->5->NULL, m = 2 and n = 4,
    return 1->4->3->2->5->NULL.
Note: Given m, n satisfy the following condition: 1 <= m <= n <= length of list.
'''
# three pointers:
# (1) prevM, the one before m-th element
# (2) head, scanning through the list; act when pointing to (m+1)-th ~ n-th elements
# (3) prev, previous node of head
def reverse_llist(head, m, n):
    if m >= n: return head
    dummy = Node(0, next=head)
    prev = prevM = dummy
    for i in range(1,n+1):
        if i == m:
            # prevM.next = the first element to revert (m-th)
            prevM = prev
        elif m < i <= n:
            # insert head after prevM
            prev.next = head.next
            head.next = prevM.next
            preM.next = head
            head = prev # points to the later element
        prev = head
        head = head.next
    return dummy.next


'''
Given a list, rotate the list to the right by k places, where k is non-negative.
For example:
    Given 1->2->3->4->5->NULL and k = 2,
    return 4->5->1->2->3->NULL.
'''
def rotate_llist(head, k):
    dummy = Node(-1, next=head)
    # count how many nodes in the list
    len = 1
    last = head # find the last node
    while last.next:
        len += 1
        last = last.next
    k = k % len
    if k == 0: return dummy.next
    
    # reset
    prev = dummy
    head = dummy.next
    # point to the new head and the previous node
    for _ in range(len-k):
        prev = head
        head = prev.next
    prev.next = last.next
    last.next = dummy.next
    dummy.next = head
    return dummy.next


'''
Given a linked list, reverse the nodes of a linked list k at a time and return its modified list. If the number of nodes is not a multiple of k then left-out nodes in the end should remain as it is.

You may not alter the values in the nodes, only nodes itself may be changed.
Only constant memory is allowed.

For example,
    Given this linked list: 1->2->3->4->5
    For k = 2, you should return: 2->1->4->3->5
    For k = 3, you should return: 3->2->1->4->5
'''
# ~O(1) in space
def reverse_nodes(head, k):
    if k <= 1: return head
    dummy = Node(-1, next=head)
    # count the number of nodes
    len = 0
    while head:
        len += 1
        head = head.next
    # point to the previous node of the first node in the reverse section of length k.
    starter = dummy
    for _ in range(len//k):
        prev = starter
        head = starter.next
        # this part is similar to "Reverse Linked List II"
        for _ in range(k-1): # insert k-1 times
            if head is None:
                return dummy.next
            prev = head
            head = head.next
            # inset head to be right after starter
            prev.next = head.next
            head.next = starter.next
            starter.next = head
            head = prev
        
        # set up new starter
        starter = prev
    return dummy.next


if __name__ == '__main__':
    #print reverse_int(123099999)
    #print reverse_int(-19900000)
    
    l1 = Node(1, Node(1, Node(2)))
    l2 = Node(2, Node(3, Node(3, Node(5, Node(5, Node(7))))))
    print reverse_nodes(Node(1, Node(2, Node(3, Node(4, Node(5, Node(6)))))), 2)
    print reverse_nodes(Node(1, Node(2, Node(3, Node(4, Node(5, Node(6)))))), 3)
    print reverse_nodes(Node(1, Node(2, Node(3, Node(4, Node(5, Node(6)))))), 4)


