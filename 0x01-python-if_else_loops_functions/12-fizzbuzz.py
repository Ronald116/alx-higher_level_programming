#!/usr/bin/python3
def fizzbuzz():
    '''
    Write a ftn that prints the numbers from 1 to 100
    '''
    for num in range(1,101):
        if num % 5 == 0 and num % 3 == 0:
            print("{}".format("FizzBuzz", end=' ')

        elif num % 3 == 0:
            print("{}".format("Fizz", end=' ' )

        elif num % 5 == 0:
            print("{}".format("Buzz", end= ' ')

        else:
            print("{}".format(num, end=' ')

    print()
