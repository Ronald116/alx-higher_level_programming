#!/usr/bin/python3
def weight_average(my_list=[]):
    if my_list and len(my_list):
        num = 0
        denum = 0
        for tup in my_list:
            num += (tup[0] * tup[1])
            denum += (tup[1])
        return (num/denum)
    return 0
