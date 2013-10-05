#!/usr/bin/env python

from __future__ import division
from math import log10

class Node(object):
    def __init__(self, value=0,
                 left=None, right=None, 
                 id=None, parent=None):
        self.id = id
        self.left = left
        self.right = right
        self.value = value
        self.parent = parent
    
    def __str__(self):
        if self.left is None and self.right is None:
            return str(self.value)
        else:
            return '%s (%s, %s)' % (
                    str(self.value), 
                    str(self.left), 
                    str(self.right))
    
    def __repr__(self):
        s = 'TreeNode Object (id=' + str(self.id) + \
            ' value='+str(self.value)+')'
        return s
    
    def pretty_print(self):
        # get each levels
        level = [self]
        to_prints = [[self.value]]
        while True:
            is_all_none = True
            next_level = []
            to_print = []
            for n in level:
                if n is None:
                    next_level += [None, None]
                    to_print += ['#','#']
                else:
                    is_all_none = False
                    next_level += [n.left, n.right]
                    left_val = n.left.value if n.left and n.left.value else '#'
                    right_val = n.right.value if n.right and n.right.value else '#'
                    to_print += [left_val, right_val]
            if is_all_none: break
            level = next_level
            to_prints.append(to_print)
        
        #max_val_digits = max([max([len(str(v)) for v in r]) for r in to_prints])
        #print max_val_digits
        
        to_prints = to_prints[:-1] # remove the last row with only '#'
        to_pretty_prints = []
        to_prints.reverse()
        for i, row in enumerate(to_prints):
            row = map(str,row)
            #row = [' '*(max_val_digits-len(v))+v for v in row]
            sep = ' '*(2**(i+1) - 1)
            space = ' '*(2**i - 1)
            to_pretty_prints.insert(0, space + sep.join(row) + space)
        print '\n'.join(to_pretty_prints)


root = Node(value=5,
            left=Node(value=4,
                 left=Node(value=1,
                      right=Node(value=2))
            ),
            right=Node(value=8,
                 left=Node(value=3),
                 right=Node(value=4,
                    left=Node(value=9),
                    right=Node(value=1))
            )
        )

BST = Node(value=5,
            left=Node(value=2,
                 left=Node(value=1,
                    right=Node(value=1.5, 
                        left=Node(value=1.2))),
                 right=Node(value=3)
            ),
            right=Node(value=9,
                 left=Node(value=7),
                 right=Node(value=15,
                    right=Node(value=16)
                 )
            )
        )

root_with_id = Node(id=0,value=-3,
                    left=Node(id=1,value=-2,
                         left=Node(id=3,value=3,
                              left=Node(id=7,value=1,
                                    left=Node(id=11,value=4)),
                              right=Node(id=8,value=1)),
                         right=Node(id=4,value=-1,
                              left=Node(id=9,value=4),
                              right=Node(id=10,value=2))
                    ),
                    right=Node(id=2,value=2,
                         left=Node(id=5,value=-1),
                         right=Node(id=6,value=3,
                            right=Node(id=12,value=2))
                    )
                )


if __name__ == '__main__':
    root.pretty_print()
    print
    BST.pretty_print()
