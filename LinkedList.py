#!/usr/bin/env python

from __future__ import division

class Node(object):
    def __init__(self, value, next=None, prev=None):
        self.prev = prev
        self.next = next
        self.value = value
    
    def __str__(self):
        if self.next is None:
            return str(self.value)
        else:
            return '%d (%s)' % (self.value, str(self.next))
    
    def __repr__(self):
        s = 'LinkedListNode Object (value='+str(self.value)+')'
        return s


