#!/usr/bin/env python

from __future__ import division
import random
from math import sqrt

'''
Output all prime numbers up to a specified integer n.
'''
# using The Sieve of Erantosthenes
def prime_sieve(n):
    is_prime = dict((i,True) for i in range(2,n+1))
    limit = int(sqrt(n))
    for i in range(2, limit+1):
        for j in range(2, n//i+1):
            is_prime[i*j] = False
    ret = [n for n in is_prime if is_prime[n]]
    print ret
    return ret

'''
Output first n prime numbers
'''
def prime(n):
    primes = [2]
    num = 3
    while len(primes) < n:
        is_prime = True
        for p in primes:
            if num % p == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(num)
        num += 1
    print primes
    return primes


if __name__ == '__main__':
    prime_sieve(230)
    prime(50)


