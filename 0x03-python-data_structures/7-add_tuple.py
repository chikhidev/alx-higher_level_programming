#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    res = ()
    length = max(len(tuple_a), len(tuple_b))
    i = 0
    while i <= length:
        left = tuple_a[i] if i < len(tuple_a) else 0
        right = tuple_b[i] if i < len(tuple_b) else 0
        res += (left + right,)
    return res

