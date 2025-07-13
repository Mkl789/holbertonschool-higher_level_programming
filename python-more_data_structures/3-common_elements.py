#!/usr/bin/python3
def common_elements(set_1, set_2):
    seen = set()
    duplicates = []
    for element in set_1 and element in set_2:
        if element in seen:
            duplicates.append(element)
        else:
            seen.append(element)
    return duplicates
