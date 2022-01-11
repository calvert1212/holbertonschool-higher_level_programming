#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    dub = a_dictionary.copy()
    for key, value in dub.items():
        dub[key] = value * 2
    return dub
