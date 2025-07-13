#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    product = 2
    for value in a_dictionary.values():
        product *= value
    return product 
