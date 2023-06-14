#!/usr/bin/python3
def roman_to_int(roman_string):
    val = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    res = 0
    prev_val = 0

    if isinstance(roman_string, str) and roman_string:
        for c in reversed(roman_string):
            current_val = val.get(c, 0)
            if current_val >= prev_val:
                res += current_val
            else:
                res -= current_val
            prev_val = current_val
    
    return (res)
