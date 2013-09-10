#!/usr/bin/env python3

"""
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""

i = 0
for x in range(999,100,-1):
    for y in range(x,100,-1):
        a = x * y
        if a > i:
            thing = str(a)
            if thing == thing[::-1]:
                i = a

print(i)


