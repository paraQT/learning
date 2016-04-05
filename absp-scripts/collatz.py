#Write a function named  collatz() that has one parameter named  number . If  number is even, then  collatz() should print  number // 2 and return this value. If  number is odd, then  collatz() should print and return  3 * number + 1

import sys

def collatz(number):
    if number % 2 == 0:
        print(number // 2)
        return number // 2
    elif number % 2 == 1:
        print(3 * number + 1)
        return 3 * number + 1

inputnum = input("enter a number: ")
try:
    inputnum = int(inputnum)
except ValueError:
    sys.exit("enter an int")

while inputnum > 1:
    inputnum = collatz(inputnum)
