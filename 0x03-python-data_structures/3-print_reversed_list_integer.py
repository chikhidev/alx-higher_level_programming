#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    for i in range (len(my_list) - 1, 0):
        print('{}'.format(my_list[-i]))
