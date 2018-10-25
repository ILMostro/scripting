#!/bin/python3

'''
hackerrank challenge:
If the given input number is odd, print "Weird".
If the number is even, 2 <= N <= 5, print "Not Weird".
If the number is even, 6 <= N <= 20, print "Weird".
Else, print "Not Weird"
for the range in 1 <= N <= 100
    '''

# N = int(input("Enter a number: "))
N = int(input())

def test( i ):

    while i in range(1, 101):
        if i % 2:
            print(f"{i} Weird")
            break;
        elif 6 <= i <= 20:
            print(f"{i} Weird")
            break;
        else:
            print(f"{i} Not Weird")
            break;

if __name__ == "__main__":
    test(N)
