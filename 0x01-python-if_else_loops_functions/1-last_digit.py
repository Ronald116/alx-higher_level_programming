#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
str = "Last digit of"
if number % 10 > 5:
    print("{} {} is {} and is {}".format(str, number, number % 10, "greater than 5"))
elif number % 10 == 0:
    print("{} {} is {} and is {}".format(str, number, number % 10, 0))
elif number % 10 < 6 and number % 10 > 0:
    print("{} {} is {} and is {}".format(str, number, number % 10, "less than 6 and not 0"))
