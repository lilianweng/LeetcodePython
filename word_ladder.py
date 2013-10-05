#!/usr/bin/env python

from __future__ import division
import random
from collections import defaultdict


def only_one_letter_diff(w1, w2):
    diff = 0
    if len(w1) != len(w2): return False
    for i in range(len(w1)):
        if w1[i] != w2[i]: diff += 1
        if diff > 1: return False
    return diff == 1


'''
Leetcode: Word Ladder
Given two words (start and end), and a dictionary, find the length of shortest transformation sequence from start to end, such that:
Only one letter can be changed at a time
Each intermediate word must exist in the dictionary
For example,
Given:
    start = "hit"
    end = "cog"
    dict = ["hot","dot","dog","lot","log"]
As one shortest transformation is "hit" -> "hot" -> "dot" -> "dog" -> "cog",
Return: its length 5.
Note:
    Return 0 if there is no such transformation sequence.
    All words have the same length.
    All words contain only lowercase alphabetic characters.
'''
# (0) Build a graph first
# (1) Find a shortest path in the graph
#     or DP similar to "longest incresing subsequence"??
def word_ladder(start, end, words):
    import heapq
    links = defaultdict(list)
    allwords = list(set(words) | set([start,end]))
    n = len(allwords)
    for i in range(n):
        for j in range(i+1,n):
            if only_one_letter_diff(allwords[i], allwords[j]):
                links[allwords[i]].append(allwords[j])
                links[allwords[j]].append(allwords[i])
    
    print '\n'.join([k+': '+str(v) for k,v in links.items()])
    
    # Dijkstra's algorithm: shortest path between start and end
    queue = set(allwords)
    dist = dict((w, float('inf')) for w in allwords)
    dist[start] = 0 # distance between a node and the start node.
    prev = {}
    while queue:
        word = min(queue, key=lambda x:dist[x])
        queue.remove(word)
        if dist[word] == float('inf'): break
        for w in links[word]:
            alt_dist = dist[word] + 1
            if alt_dist < dist[w]:
                dist[w] = alt_dist
                prev[w] = word
    
    print dist
    return dist[end]

'''
Leetcode: Word Ladder II
Given two words (start and end), and a dictionary, find all shortest transformation sequence(s) from start to end, such that:
Only one letter can be changed at a time
Each intermediate word must exist in the dictionary
For example,
Given:
    start = "hit"
    end = "cog"
    dict = ["hot","dot","dog","lot","log"]
Return:
    [
      ["hit","hot","dot","dog","cog"],
      ["hit","hot","lot","log","cog"]
    ]
Note:
    All words have the same length.
    All words contain only lowercase alphabetic characters.
'''

### Find all transformation, but not necessarily shortest
def word_ladder_II1(start, end, words):
    links = defaultdict(list)
    allwords = list(set(words) | set([start,end]))
    n = len(allwords)
    for i in range(n):
        for j in range(i+1,n):
            if only_one_letter_diff(allwords[i], allwords[j]):
                links[allwords[i]].append(allwords[j])
                links[allwords[j]].append(allwords[i])
    #print '\n'.join([k+': '+str(v) for k,v in links.items()])
    
    for path in BFS(start, end, links, set()):
        print [start] + path


def BFS(start, end, links, visited):
    if start == end:
        yield []
    else:
        for next in links[start]:
            if next in visited: continue
            for p in BFS(next, end, links, visited | set([next])):
                yield [next] + p


### Fina all shortest transformation!!
def word_ladder_II2(start, end, words):
    links = defaultdict(list)
    allwords = list(set(words) | set([start,end]))
    n = len(allwords)
    for i in range(n):
        for j in range(i+1,n):
            if only_one_letter_diff(allwords[i], allwords[j]):
                links[allwords[i]].append(allwords[j])
                links[allwords[j]].append(allwords[i])
    #print '\n'.join([k+': '+str(v) for k,v in links.items()])
    
    # Use BFS to find shortest path and build prev[x] = [list]
    
    # distance between start and all other nodes.
    dist = dict((w,float('inf')) for w in allwords) 
    dist[start] = 0
    
    prev = dict((w,[]) for w in allwords)
    queue = set(allwords) # start with full queue
    while queue:
        # always pop out the node with min dist
        word = min(queue, key=lambda x:dist[x])
        queue.remove(word)
        for w in links[word]:
            alt_dist = dist[word]+1
            if alt_dist < dist[w]:
                dist[w] = alt_dist
                prev[w] = [word]
            elif alt_dist == dist[w]: # key!
                prev[w].append(word)
    
    paths = [path+[end] for path in recover_paths(end, prev)]
    print paths
    return paths

def recover_paths(end, prev):
    if len(prev[end]) == 0: yield []
    else:
        for word in prev[end]:
            for prev_path in recover_paths(word, prev):
                yield prev_path + [word]


if __name__ == '__main__':
    words = ["hot","dot","dog","leg","dig","die","lie","doe","lot","log","cog","hit"]
    #word_ladder("hit", "lot", words)
    word_ladder_II2("hit", "cog", words)
    word_ladder_II2("dot", "log", words)
    word_ladder_II2("die", "cog", words)
    word_ladder_II2("die", "leg", words)
    word_ladder_II2("lot", "dig", words)


