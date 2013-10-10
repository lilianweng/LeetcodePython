#!/usr/bin/env python
'''
Leetcode: Gas Station

There are N gas stations along a circular route, where the amount of gas at station i is gas[i].
You have a car with an unlimited gas tank and it costs cost[i] of gas to travel from station i to its next station (i+1). You begin the journey with an empty tank at one of the gas stations.
Return the starting gas station's index if you can travel around the circuit once, otherwise return -1.

Note: The solution is guaranteed to be unique.
'''
from __future__ import division
import random

# G(i,j) = the maximum leftover gas a car goes from i-th station to j-th.
# the car can use gas at i-th but not at j-th
# only valid when G(i,j) >= 0
# G(i,j) = max{G(i,mid)+G(k,mid) for i < mid < j, 
#              gas[i] - (cost[i]+...+cost[j])}
# We use G(i,i) for a circular route.
# ~ O(n^2)
def gas_station(gas, cost):
    n = len(gas)
    G = {}
    for i in range(n):
        G[i,(i+1)%n] = gas[i] - cost[i]
    print G
    
    for k in range(2,n+1):
        for i in range(n):
            j = (i+k) % n
            G[i,j] = -float('inf')
            sum_cost = cost[i]
            # with stop
            for mid in range(i+1,i+k):
                mid = mid % n
                if G[i,mid] >= 0:
                    G[i,j] = max(G[i,j], G[i,mid]+G[mid,j])
                sum_cost += cost[mid]
            # no stop
            if gas[i]-sum_cost > 0:
                G[i,j] = max(G[i,j], gas[i]-sum_cost)
    
    circles = dict((i, G[i,j]) for i,j in G if j == i)
    print circles
    return max(circles.values()) >= 0


if __name__ == '__main__':
    gas = [10,5,10,5,10]
    cost = [8,2,2,12,10]
    gas_station(gas, cost)


