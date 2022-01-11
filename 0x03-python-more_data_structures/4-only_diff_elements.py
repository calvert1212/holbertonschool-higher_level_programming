#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    xelem = set(set_1 ^ set_2)
    return xelem
