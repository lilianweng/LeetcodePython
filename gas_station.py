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


# We can use a Queue to store the current tour. We first enqueue first petrol pump to the queue, we keep enqueueing petrol pumps till we either complete the tour, or current amount of petrol becomes negative. If the amount becomes negative, then we keep dequeueing petrol pumps till the current amount becomes positive or queue becomes empty.
def gas_station(gas, cost):
    n = len(gas)
    start = 0; next = 1
    Q = []
    cur_gas = gas[start] - cost[start]
    while start != next or cur_gas < 0:
        while start != next and cur_gas < 0:
            # pop, changing starting point
            cur_gas -= gas[start] - cost[start]
            start = (start+1)%n
            if start == 0: # go back to the first trial
                return -1
        cur_gas += gas[next] - cost[next]
        next = (next+1)%n
    return start


'''
What if we want to keep the leftover gas as much as possible?
'''
# G(i,j) = the maximum leftover gas a car goes from i-th station to j-th.
# the car can use gas at i-th but not at j-th
# only valid when G(i,j) >= 0
# G(i,j) = max{G(i,mid)+G(k,mid) for i < mid < j, 
#              gas[i] - (cost[i]+...+cost[j])}
# We use G(i,i) for a circular route.
# ~ O(n^3)
def gas_station2(gas, cost):
    n = len(gas)
    G = {}
    for i in range(n): G[i,(i+1)%n] = gas[i] - cost[i]
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


''' 
What if we want to get the trip with the minimum times of stops?
'''
# G(i,j,s) = maximum leftover gas from i-th to j-th station with s stops in-between; 0 <= s <= j-i-1
# G(i,j,0) = gas[i] - sum(cost[i..j-1])
# G(i,j,s) = max{G(i,mid,s1) + G(mid,j,s2) for 
#                     0 <= s1 <= mid-i-1, 
#                     0 <= s2 <= j-mid-1,
#                     s1+s2+1 == s}
# Final results: argmin_s G(i,j,s) >= 0.
# ~O(n^4)
def gas_station3(gas, cost):
    n = len(gas)
    G = {}
    for i in range(n): G[i,(i+1)%n,0] = gas[i] - cost[i]
    
    for k in range(2, n+1):
        for i in range(n):
            j = i+k
            G[i,j%n,0] = gas[i] - sum([cost[x%n] for x in range(i,j)])
            for s in range(1, k):
                G[i,j%n,s] = -float('inf')
                for mid in range(i+1,i+k):
                    for s1 in range(0, mid-i):
                        s2 = s-s1-1
                        if s2 < 0 or s2 > j-mid-1: continue
                        
                        print '(i,j,s)=(%d,%d,%d)'%(i,j,s), s1, s2
                        G[i,j%n,s] = max(G[i,j%n,s], \
                                         G[i,mid%n,s1]+G[mid%n,j%n,s2])
            #'''
            for x,y,z in G:
                if z == s:
                    print x,y,z, ':', G[x,y,z]
            #'''
    
    for k,v in G.items(): print k,v
    
    min_step = n-1
    for i in range(n):
        args = [x for x in range(0,n) if G[i,i,x] > 0]
        if args:
            min_s = min(args)
            min_step = min(min_step, min_s)
            print i,'-->',i, 'steps:',min_s, 'leftover gas:', G[i,i,min_s]
    return min_step


# Greedy algorithm, starting at 


if __name__ == '__main__':
    gas = [10,5,10,5,10]
    cost = [2,2,2,5,2]
    print gas_station3(gas, cost)


