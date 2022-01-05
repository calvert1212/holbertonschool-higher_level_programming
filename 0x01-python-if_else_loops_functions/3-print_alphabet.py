#!/usr/bin/python3
a = 97
while (a <= 122):
    if (a != 101 and a != 113):
        print("{}".format(chr(a)), end = '')
        a += 1
    else:
        a += 1
