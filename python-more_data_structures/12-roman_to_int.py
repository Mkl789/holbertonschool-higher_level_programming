#!/usr/bin/python3
def roman_to_int(roman_string): 
    result = ""
    if not isinstance(roman_string, str) or roman_string == None:
        return 0
    for numeral in range(0x2160, 0x217):
        result = chr(numeral)
    return result
