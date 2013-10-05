#!/usr/bin/env python
'''
Leetcode: Edit distance
'''
from __future__ import division
import random

### DP: edit distance, ~O(mn)
# E(i,j): edit distance between A[:i] & B[:j]
# E(i,j) = min{1+E(i-1,j), 1+E(i,j-1), diff(i,j)+E(i-1,j-1)}
def edit_distance(A, B):
    a,b = len(A),len(B)
    E = {}
    
    # Initialization
    prev = dict(((i,j),None) for i in range(a+1) for j in range(b+1))
    for i in range(a+1):
        E[(i,0)] = i
        prev[(i,0)] = (i-1,0)
    for j in range(b+1):
        E[(0,j)] = j
        prev[(0,j)] = (0,j-1)
    del prev[(0,0)]
    
    # DP-ing
    for i in range(1,a+1):
        for j in range(1,b+1):
            diff = 0 if A[i-1] == B[j-1] else 1
            prev_choice = {
                (i-1,j): 1+E[(i-1,j)],
                (i,j-1): 1+E[(i,j-1)],
                (i-1,j-1): diff+E[(i-1,j-1)]
            }
            E[(i,j)] = min(prev_choice.values())
            prev[(i,j)] = min(prev_choice, key=lambda x:prev_choice[x])
    
    # Output
    A_edit, B_edit = '', ''
    i,j = a,b
    while prev[(i,j)]:
        prev_i,prev_j = prev[(i,j)]
        if prev_i == i-1 and prev_j == j:
            A_edit = A[i-1] + A_edit
            B_edit = '-' + B_edit
        elif prev_i == i and prev_j == j-1:
            A_edit = '-' + A_edit
            B_edit = B[j-1] + B_edit
        else:
            A_edit = A[i-1] + A_edit
            B_edit = B[j-1] + B_edit
        i,j = prev_i,prev_j
    print A_edit
    print B_edit
    return E[(a,b)]
if __name__ == '__main__':
    func()


