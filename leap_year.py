#!/usr/bin/env python

# In the Gregorian calendar, a leap year is identified as follows:
#     if year / 4 can be evenly divided, it's a leap year
#     if year / 100 can be evenly divided, it's NOT a leap year, unless:
#         if year / 400 can be evenly divided, it's a leap year.

'''
Checks if the given year is a leap year or not.
for years between 1900 and 10**5
'''

def is_leap(year):
    leap = False

    if 1900 <= year <= 10**5:
        if year % 4 == 0:
            leap = True
        if year % 100 == 0:
            leap = False
            if year % 400 == 0:
                leap = True

        return leap
    else:
        return "out ouf bounds"

if __name__ == "__main__":
    year = int(input())
    print(is_leap(year))
