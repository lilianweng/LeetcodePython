#!/usr/bin/env python

from __future__ import division
import random
from LinkedList import Node


'''
Leetcode: Remove Duplicates from Sorted Array
Given a sorted array, remove the duplicates in place such that each element appear only once and return the new length. Do not allocate extra space for another array, you must do this in place with constant memory.
For example,
    Given input array A = [1,1,2],
    Your function should return length = 2, and A is now [1,2].
'''
# O(1) in space!
def remove_dup_array(A):
    print A, '-->', 
    i = 0
    for j in range(1, len(A)):
        if A[i] != A[j]:
            i += 1
            A[i] = A[j]
    for j in range(i+1, len(A)):
        A[j] = None
    print A
    return i+1, A


'''
Leetcode: Remove Duplicates from Sorted Array II
What if duplicates are allowed at most twice?
For example,
    Given sorted array A = [1,1,1,2,2,3],
    Your function should return length = 5, and A is now [1,1,2,2,3].
'''
# O(1) in space!
def remove_dup_array2(A):
    if len(A) <= 2: return A
    print A, '-->', 
    i = 1
    for j in range(2, len(A)):
        if (not A[j] == A[i-1]) or (not A[j] == A[i]):
            i += 1
            A[i] = A[j]
    for j in range(i+1, len(A)):
        A[j] = None
    print A
    return i+1, A


'''
Leetcode: Remove Duplicates from Sorted List
Given a sorted linked list, delete all duplicates such that each element appear only once. For example,
Given 1->1->2, return 1->2.
Given 1->1->2->3->3, return 1->2->3.
'''
def remove_dup(node):
    seen = set()
    root = node
    last = node # last node of the non-duplicate linked list
    while node:
        if node.value == last.value:
            last.next = node.next
        else:
            seen.add(node.value)
            last = node
        node = node.next
    print root
    return root


'''
Leetcode: Remove Duplicates from Sorted List II
Given a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers from the original list. For example,
Given 1->2->3->3->4->4->5, return 1->2->5.
Given 1->1->1->2->3, return 2->3.
Given 1->1->2->2, return Null.
'''
# keep three pointers:
# (1) prev: previous node of cur
# (2) cur: first element of potential duplicated sequence
# (3) next: last element of potential duplicated sequence
def remove_dup2(head):
    if not head: return None
    
    dummy = Node(None, next=head)
    prev = dummy
    cur = head
    next = head.next
    seen = 0
    while next:
        if cur.value != next.value:
            if seen > 0:
                # delete duplicated numbers
                prev.next = next
                cur = next
                next = next.next
            else:
                # simply move one step for every pointer
                prev = prev.next
                cur = cur.next
                next = next.next
            seen = 0
        else:
            # find the last element of the duplicated number
            next = next.next
            seen += 1
    # leftover (duplications at the end)
    if next is None and seen > 0:
        prev.next = None
    return dummy.next


'''
Leetcode: Remove Element
Given an array and a value, remove all instances of that value in place and return the new length. The order of elements can be changed. It doesn't matter what you leave beyond the new length.
'''
def remove_element(A, val):
    print A, '-->', 
    i = 0
    for j in range(1, len(A)):
        if A[j] != val:
            i += 1
            A[i] = A[j]
    for j in range(i+1, len(A)):
        A[j] = None
    print A
    return i+1, A


'''
Remove Nth Node From End of List
Given a linked list, remove the nth node from the end of list and return its head.
For example,
   Given linked list: 1->2->3->4->5, and n = 2.
   After removing the second node from the end, the linked list becomes 1->2->3->5.
Note: Given n will always be valid.
      Try to do this in ONE pass.
'''
# take care of the first/last
def remove_nth_end(root, n):
    first = root
    second = root
    i = 0
    while second:
        second = second.next
        i += 1
        if i == n+1: break
    
    if i < n+1:
        # the first element will be removed
        root = first.next
    else:
        while second:
            first = first.next
            second = second.next
        # remove first.next node
        first.next = first.next.next
    print root
    return root


if __name__ == '__main__':
    l1 = Node(1, Node(1, Node(1, Node(2))))
    l2 = Node(2, Node(3, Node(3, Node(5, Node(5, Node(7))))))
    l3 = Node(1, Node(1, Node(3, Node(3, Node(5, Node(5))))))
    
    #remove_dup(l1)
    #remove_dup(l2)
    #remove_dup(l3)
    
    remove_dup2(l1)
    remove_dup2(l2)
    remove_dup2(l3)
    
    #remove_nth_end(l1, 3)
    #remove_nth_end(l2, 3)
    #remove_nth_end(l3, 1)
    
    #remove_dup_array2([1,1,2,2,2])
    #remove_dup_array2([2,2,2,3,4,5,5,5,6])
    
    #remove_element([1,1,3,2,2,4,3,5,1,7], 3)
    #remove_element([5,4,3,3], 9)

