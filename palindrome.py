#!/usr/bin/env python
"""
string palindrome checker
"""

def isPalindrome(str):
    for i in range(0, len(str)//2):
        if str[i] != str[len(str) - i - 1]:
            return False
    return True

# sample string test
# s = "racecar"
# second string test
s = "racecars"
t = isPalindrome(s)

if (t):
    print(f"{s} is palindrome")
else:
    print(F"{s} is NOT a palindrome")
