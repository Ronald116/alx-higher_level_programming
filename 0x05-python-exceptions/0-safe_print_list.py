#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    '''
    A ftn that prints x elements of a list
    '''
    ttl = 0
    for i in range(x):
        try:
            print("{}".format(my_list[i]), end='')
            
            ttl += 1

        except IndexError:
            break

    return(ttl)
