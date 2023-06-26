#!/usr/bin/python3
def magic_calculation(a, b):
    result = 0
    i = 1
    while i < 3:
        try:
            if i > a:
                raise Exception('Too far')
            else:
                result += a ** b / i
        except Exception as e:
            result = a + b
            pass
        finally:
            i += 1
    return result
