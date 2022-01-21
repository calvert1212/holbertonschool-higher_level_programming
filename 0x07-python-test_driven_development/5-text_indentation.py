#!/usr/bin/python3
"""
This module contains the function text_indentation.
"""


def text_indentation(text):
    """
    Prints text but replaces certain chars with newline
    """
    a = 1
    buff = ''
    limiters = ['.', '?', ':']
    if type(text) is not str:
        raise TypeError("text must be a string")
    for i in text:
        buff = buff + i
        if a == len(text) and i not in limiters:
            buff = buff.strip()
            print(buff, end="")
        elif i in limiters:
            buff = buff.strip()
            print(buff)
            print()
            buff = ""
        a += 1
