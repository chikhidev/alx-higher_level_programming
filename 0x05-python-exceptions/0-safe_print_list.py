#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    org = x
    while x >= 0:
        try:
            print("{}".format(my_list[x]))
            x-=1
        except:
            break
    print("\n")
    return (org - x)
