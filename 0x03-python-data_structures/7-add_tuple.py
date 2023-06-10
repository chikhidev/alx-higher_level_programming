#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    res = ()
    a = len(tuple_a) - 1
    b = len(tuple_b) - 1
    length = min(a, b)
    i = 0
    while i <= length:
        res[i] += (tuple_a[i] + tuple_b[i],)
        i+=1
    return res
