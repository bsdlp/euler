#!/usr/bin/env python3
"""
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?
"""

from math import sqrt

def is_prime(urmom):
    return all(urmom % i for i in range(2,int(sqrt(urmom))))

blah = 0
shiz = 1

while blah < 10001:
    shiz += 1
    if is_prime(shiz):
        print(shiz)
        blah += 1

print(shiz)

