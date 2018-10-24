#!/usr/bin/env python
"""
pydoc goes here
"""

my_range = iter(list(range(1, 100)))
evens = []; odds = []

for num in my_range:
    if num % 2 == 0:
        evens.append(num)
    else:
        odds.append(num)

longest = 1

def fun(result):
    # results = []
    results = [result]
    while result > 1:
        if result in evens:
            # result = (result / 2)
            # Let's get bottom result int, rather than float
            result = (result // 2)
            results.append(result)
            continue
        elif result in odds:
            result = result * 3 + 1
            results.append(result)
            continue
    else:
        if result == 1:
            # results.append(result)
            # return results
            return f'The sequence starting with {results[0]} has a length of {len(results)} values, which are as follows: \n{results}'\
                    f'\n\nThe sum of the values is {sum(results)}'
        else:
            print("Out of bounds")


# def funsum():


if __name__ == "__main__":
    print(fun(3))
