#!/usr/bin/python3
a = 0
b = 1

while (a + b) < 18:
    b = a + 1
    while b < 10:
        print("{}{}, ".format(a, b), end = '')
        b += 1
    a += 1
print ("89")
