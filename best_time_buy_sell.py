#!/usr/bin/env python

from __future__ import division
import random


'''
Leetcode: Best Time to Buy and Sell Stock
Say you have an array for which the ith element is the price of a given stock on day i.
If you were only permitted to complete at most one transaction (ie, buy one and sell one share of the stock), design an algorithm to find the maximum profit.
'''
# Find i, j to maximize A[j]-A[i] and i < j
# O(nlogn)
def stock1(A):
    n = len(A)
    sorted_days = sorted(range(n), key=lambda x:A[x])
    i,j = 0,n-1
    while sorted_days[i] > sorted_days[j]:
        i += 1; j -= 1
    buy = sorted_days[i]
    sell = sorted_days[j]
    print 'Buy on day', buy, A[buy]
    print 'Sell on day', sell, A[sell]
    return sorted_days[i], sorted_days[j]

# Scan through each day and consider it as a "sell" day, we know 
# which day is the corresponding best "buy" day! ~O(n)
def stock1_better(A):
    min_day = buy = sell = 0 # day indices
    max_diff = 0
    for i in range(len(A)):
        if A[i] < A[min_day]: min_day = i
        cur_diff = A[i] - A[min_day] # always sell after buy!
        if cur_diff > max_diff:
            buy = min_day
            sell = i
            max_diff = cur_diff
    print 'Buy on day', buy, ':', A[buy]
    print 'Sell on day', sell, ':', A[sell]
    return sell, buy


'''
Leetcode: Best Time to Buy and Sell Stock II
Say you have an array for which the ith element is the price of a given stock on day i.
Design an algorithm to find the maximum profit. You may complete as many transactions as you like (ie, buy one and sell one share of the stock multiple times). However, you may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).
'''
# Consider: (a,b,c,d) and c < b
# X = d-a; Y = (b-a) + (d-c) then X < Y
# Compute the difference between each two consecutive days, select positive values
def stock2(A):
    transactions = []
    profit = 0
    buy = sell = 0
    for i in range(1,len(A)):
        if A[i] - A[i-1] > 0:
            sell = i
        else:
            # finish previous transaction
            if sell > buy and A[sell] - A[buy] > 0:
                transactions.append((buy, sell))
                profit += A[sell] - A[buy]
            # start a new transaction
            buy = sell = i
    # last transaction
    if sell > buy and A[sell] - A[buy] > 0:
        transactions.append((buy, sell))
        profit += A[sell] - A[buy]
    print 'Profit:', profit
    return transactions


'''
Leetcode: Best Time to Buy and Sell Stock III
Say you have an array for which the ith element is the price of a given stock on day i. Design an algorithm to find the maximum profit. You may complete at most two transactions. You may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).
'''
# Find i1, j1, i2, j2 to maximize A[j2]-A[i2]+A[j1]-A[i1] and i1 < j1 <= i2 < j2
# We are actually trying to break the day at each time instance, by adding the potential max profit before and after it together. By recording history and future for each time point, we can again do this within O(n) time.
def stock3(A):
    max_profit = 0
    max_split = None
    # max profit you can get before day i
    max_history_profit = {0:(0, (0,0))}
    min_day = 0
    for i in range(1,len(A)):
        if A[i] <= A[min_day]: min_day = i
        cur_diff = A[i]-A[min_day]
        if max_history_profit[i-1][0] > cur_diff:
            max_history_profit[i] = max_history_profit[i-1]
        else:
            max_history_profit[i] = (cur_diff, (min_day,i))
    
    # max profit you can get after day i
    max_future_profit = {len(A)-1:(0, (len(A)-1,len(A)-1))}
    max_day = len(A)-1
    for i in reversed(range(len(A)-1)):
        if A[i] > A[max_day]: max_day = i
        cur_diff = A[max_day] - A[i]
        if max_future_profit[i+1][0] > cur_diff:
            max_future_profit[i] = max_future_profit[i+1]
        else:
            max_future_profit[i] = (cur_diff, (i,max_day))
        if max_history_profit[i][0] + max_future_profit[i][0] > max_profit:
            max_profit = max_history_profit[i][0] + max_future_profit[i][0]
            max_split = i
    print 'split:', max_split, 
    print max_history_profit[max_split][1], max_future_profit[max_split][1]
    print 'profit:', max_profit
    return max_profit


if __name__ == '__main__':
    A = [8,9,12,11,13,12,15]
    print A, stock3(A)
    A = [10,5,5,5,5,6,11,9,13,8,10,11,12]
    print A, stock3(A)

