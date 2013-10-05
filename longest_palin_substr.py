#!/usr/bin/env python
'''
Leetcode: Longest Palindromic Substring

Given a string S, find the longest palindromic substring in S. You may assume that the maximum length of S is 1000, and there exists one unique longest palindromic substring.

http://leetcode.com/2011/11/longest-palindromic-substring-part-i.html
http://leetcode.com/2011/11/longest-palindromic-substring-part-ii.html
'''
from __future__ import division

# Using pair of indices for same lements
# ~O(n^2)
def longest_palin_substr1(s):
    print s, '-->', 
    elems = set(list(s))
    pos = {}
    for i, elem in enumerate(list(s)):
        pos.setdefault(elem,[]).append(i)
    #print pos
    # Get pairs of locations with same element
    pairs = set()
    for elem in pos:
        elem_pos = pos[elem]
        for i in range(len(elem_pos)):
            for j in range(i+1, len(elem_pos)):
                pairs.add((elem_pos[i],elem_pos[j]))
    # Prioritize distant pairs
    sorted_pairs = sorted(pairs, 
                          key=lambda x:x[1]-x[0], 
                          reverse=True)
    #print sorted_pairs
    for start, end in sorted_pairs:
        i, j = start, end
        while i < j:
            if not (i,j) in pairs: break
            i += 1
            j -= 1
        if i >= j:
            # find a match!
            return s[start:end+1]
    return ''


# Reverse S and become S'. Find the longest common substring between S and S', which must also be the longest palindromic substring.
# For example, S="abacdfgdcaba", S'="abacdgfdcaba".
# The longest common substring between S and S' is "abacd". Clearly, this is not a valid palindrome.
def longest_palin_substr2(s):
    n = len(s)
    if n == 0: return ''
    rev_s = s[::-1]
    # longest common string with same indices (i <--> n-1-i)
    # DP?
    longest_common_string(s, rev_s)


# DP: P(i,j) = true if S[i:j+1] is palindrome
# P(i,j) = P(i+1,j-1) and S[i] == S[j]
# ~O(n^2) in time, ~O(n^2) in space
def longest_palin_substr3(s):
    n = len(s)
    if n == 0: return ''
    P = {}
    for i in range(n): P[(i,i)] = True
    # k = j-i between 0 and n-1
    for k in range(n-1):
        for i in range(n):
            j = i+k
            if j >= n: continue
            if i+1 <= j-1:
                P[(i,j)] = P[(i+1,j-1)] and s[i] == s[j]
            else:
                P[(i,j)] = s[i] == s[j]
    start, end = max([k for k in P if P[k]], 
                      key=lambda x:x[1]-x[0])
    return s[start:end+1]


# Find center of a substring palindrome and expand it
# ~O(n^2) in time and ~O(1) in space
def longest_palin_substr4(s):
    n = len(s)
    if n == 0: return ''
    max_pali = ''
    # Center can be on a letter or between letters
    for i in range(n):
        for j in [i,i+1]:
            # Center at s[i:j+1]
            while i >= 0 and j <= n-1:
                if s[i] != s[j]: break
                i -= 1
                j += 1
            cur_pali = s[i+1:j]
            if len(cur_pali) > len(max_pali):
                max_pali = cur_pali
    return max_pali


# Manacher's Algorithm
# http://leetcode.com/2011/11/longest-palindromic-substring-part-ii.html
# http://www.felix021.com/blog/read.php?2040
# ~O(n)
def longest_palin_substr5(s):
    # reformat the string
    s = list(s)
    # so that all the palindrome substrings are of odd length
    for i in range(len(s)+1): s.insert(i*2,'#')
    print s
    p = defaultdict(int) # left/right length of palindrome centered at s[i]
    max_center = 0 # current maximum palindrom's center
    max_upper = 0 # maximum palindrom's upper boundary, max_center+P[max_center]
    for i in range(1,len(s)):
        # i & j are symmetric points to max_center_id
        j = 2*max_center - i
        p[i] = min(p[j], max_upper-i) if max_upper > i else 1
        while i-p[i] >= 0 and i+p[i] <= len(s)-1 and s[i+p[i]] == s[i-p[i]]: 
            p[i]+=1
        if p[i]+i > max_upper:
            max_upper = p[i]+i
            max_center = i
    print 's:', ','.join(s)
    print 'p:', ','.join(map(str, [p[i] for i in range(len(s))]))
    return max(p.values())-1


# Using suffix tree
# ~O(nlogn)


if __name__ == '__main__':
    __func__ = longest_palin_substr4
    print __func__('cabcbaabac')
    print __func__('abbaaa')
    print __func__('abacdfgdcaba')
    print __func__('aaaaaaa')
    print __func__('')


