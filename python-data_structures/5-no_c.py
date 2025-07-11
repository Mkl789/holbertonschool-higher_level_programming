#!/usr/bin/python3
def no_c(my_string):
    for char in my_string:
        if char != "c" or char != "C":
            no_c_string += char
            print(no_c_string)
