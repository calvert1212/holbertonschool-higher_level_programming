#!/usr/bin/python3
def search_replace(my_list, search, replace):
    xlist = my_list.copy()
    for i in range(len(xlist)):
        if xlist[i] == search:
            xlist[i] = replace
    return xlist
