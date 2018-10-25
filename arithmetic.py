#!/usr/bin/env python
'''
Given 2 input numbers, print their sum, difference, and product on
separate lines.

for range in 1 <= x <= 10**10
'''

a = int(input())
b = int(input())

if 1 >= a >= 10**10:
    print("out of bounds")
elif 1 >= b >= 10**10:
    print("out of bounds")
else:
    # print(f"{a + b}\n{a - b}]n{a * b}\n")
    print(a + b)
    print(a - b)
    print(a * b)

