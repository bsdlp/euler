#!/usr/bin/env python3

"""
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
"""

thang = 600851475143
i = 2

while i * i < thang:
    while thang % i == 0:
        thang = thang / i
    i += 1

print(thang)
