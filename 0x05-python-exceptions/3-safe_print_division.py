#!/usr/bin/python3

def safe_print_division(a, b):
    '''
    Write a function that divides
    2 integers and prints the result.
    '''

    try:
        c = a/b

    except (ZeroDivisionError, TypeError, ValueError):
        c = none

    finally:
        print("Inside result: {}".format(c))

    return(c)


