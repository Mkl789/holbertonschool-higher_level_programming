#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    if len(tuple_a) > 0:
        first_ele_tuple_a = tuple_a[0]
    else:
        first_ele_tuple_a = 0

    if len(tuple_a) > 1:
        second_ele_tuple_a = tuple_a[1]
    else:
        second_ele_tuple_a = 0

    if len(tuple_b) > 0:
        first_ele_tuple_b = tuple_b[0]
    else:
        first_ele_tuple_b = 0

    if len(tuple_b) > 1:
        second_ele_tuple_b = tuple_b[1]
    else:
        second_ele_tuple_b = 0

    result = (first_ele_tuple_a + first_ele_tuple_b,
              second_ele_tuple_a + second_ele_tuple_b)
    return result
