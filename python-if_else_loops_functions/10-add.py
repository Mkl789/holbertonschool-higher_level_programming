#!/usr/bin/python3
def add(a, b):
    if a < 0:
        result = b - a
    elif b < 0:
        result = a - b
    else:
        result = a + b
    print(result)
    return result
