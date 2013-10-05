#!/usr/bin/env python
'''
Leetcode: Text Justification
Given an array of words and a length L, format the text such that each line has exactly L characters and is fully (left and right) justified. You should pack your words in a greedy approach; that is, pack as many words as you can in each line. Pad extra spaces ' ' when necessary so that each line has exactly L characters.

Extra spaces between words should be distributed as evenly as possible. If the number of spaces on a line do not divide evenly between words, the empty slots on the left will be assigned more spaces than the slots on the right.

For the last line of text, it should be left justified and no extra space is inserted between words.

For example,
    words: ["This", "is", "an", "example", "of", "text", "justification."]
    L: 16.
Return the formatted lines as:
    [
       "This    is    an",
       "example  of text",
       "justification.  "
    ]
Note: Each word is guaranteed not to exceed L in length.

Corner Cases: A line other than the last line might contain only one word. What should you do in this case? In this case, that line should be left-justified.
'''
from __future__ import division
import random

def justification(words, L):
    lines = []
    cur_words = []; cur_len = 0
    for w in words:
        if cur_len + 1 + len(w) > L:
            # cannot contain current words
            if len(cur_words) > 1:
                space, leftover = divmod(L-cur_len, len(cur_words)-1)
                space += 1
                line = cur_words[0]
                for cw in cur_words[1:]:
                    if leftover > 0:
                        line += ' '*(space+1) + cw
                        leftover -= 1
                    else:
                        line += ' '*space + cw
            else:
                line = cur_words[0]+' '*(L-cur_len)
            lines.append(line)
            cur_words = [w]
            cur_len = len(w)
        else:
            cur_words.append(w)
            cur_len += 1+len(w)
    # last line
    if cur_words:
        line = ' '.join(cur_words) + ' '*(L-cur_len)
        lines.append(line)
    
    print '\n'.join(['"'+l+'"' for l in lines])
    return lines


if __name__ == '__main__':
    justification(["This", "is", "an", "example", "of", "text", "justification."], 16)
    justification(['Supervised', 'learning', 'is', 'the', 'machine', 'learning', 'task', 'of', 'inferring', 'a', 'function', 'from', 'labeled', 'training', 'data.', 'The', 'training', 'data', 'consist', 'of', 'a', 'set', 'of', 'training', 'examples.', 'In', 'supervised', 'learning', 'each', 'example', 'is', 'a', 'pair', 'consisting', 'of', 'an', 'input', 'object', 'typically', 'a', 'vector', 'and', 'a', 'desired', 'output', 'value', 'also', 'called', 'the', 'supervisory', 'signal.', 'A', 'supervised', 'learning', 'algorithm', 'analyzes', 'the', 'training', 'data', 'and', 'produces', 'an', 'inferred', 'function', 'which', 'can', 'be', 'used', 'for', 'mapping', 'new', 'examples', 'An', 'optimal', 'scenario', 'will', 'allow', 'for', 'the', 'algorithm', 'to', 'correctly', 'determine', 'the', 'class', 'labels', 'for', 'unseen', 'instances.', 'This', 'requires', 'the', 'learning', 'algorithm', 'to', 'generalize', 'from', 'the', 'training', 'data', 'to', 'unseen', 'situations', 'in', 'a', 'reasonable', 'way.'], 100)


