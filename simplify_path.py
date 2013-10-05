#!/usr/bin/env python
'''
Leetcode: Simplify Path
Given an absolute path for a file (Unix-style), simplify it.
For example,
    path = "/home/", => "/home"
    path = "/a/./b/../../c/", => "/c"
Corner Cases:
    Did you consider the case where path = "/../"?
    In this case, you should return "/".
    Another corner case is the path might contain multiple slashes '/' together, such as "/home//foo/".
    In this case, you should ignore redundant slashes and return "/home/foo".
'''
from __future__ import division
import random

def simply_path(path):
    dirs = []
    dir_name = ''
    for ch in path:
        if ch == '/':
            if dir_name:
                if dir_name == '..': dirs = dirs[:-1]
                elif dir_name != '.': dirs.append(dir_name)
            dir_name = ''
        else:
            dir_name += ch
    
    # leftover
    if dir_name:
        if dir_name == '..': dirs = dirs[:-1]
        elif dir_name != '.': dirs.append(dir_name)
    
    sim_path = '/' + '/'.join(dirs)
    print sim_path
    return sim_path



if __name__ == '__main__':
    simply_path("/home/")
    simply_path("/home///foo/./")
    simply_path("/a/./b/../../c/d")
    simply_path("/../../")
    simply_path("/../../foo1/foo2/foo3")



