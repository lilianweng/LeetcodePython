#!/usr/bin/env python
'''
Leetcode: Add Two Numbers

You are given two linked lists representing two non-negative numbers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
'''
from __future__ import division
import random

class DigitNode(object):
    def __init__(self, digit, next=None):
        self.digit = digit
        self.next = next
    def __str__(self):
        if next:
            return 'DigitNode(%d, %s)' % (self.digit, str(self.next))
        else:
            return 'DigitNode(%d)' % (self.digit)

def add_two_numbers(a, b):
    prev_carry = 0
    orig_node = None
    prev_node = None
    while a and b:
        digit = (a.digit + b.digit + prev_carry) % 10
        cur_carry = (a.digit + b.digit + prev_carry) // 10
        node = DigitNode(digit)
        if prev_node: prev_node.next = node
        else: orig_node = node
        a = a.next
        b = b.next
        prev_carry = cur_carry
        prev_node = node
    # leftover
    x = a if a else b
    while x:
        digit = (x.digit + prev_carry) % 10
        cur_carry = (x.digit + prev_carry) // 10
        node = DigitNode(digit)
        if prev_node: prev_node.next = node
        x = x.next
        prev_carry = cur_carry
        prev_node = node
    return orig_node


if __name__ == '__main__':
    a = DigitNode(2, DigitNode(4, DigitNode(3, DigitNode(5))))
    b = DigitNode(5, DigitNode(6, DigitNode(4, DigitNode(1, DigitNode(2)))))
    print add_two_numbers(a,b)

