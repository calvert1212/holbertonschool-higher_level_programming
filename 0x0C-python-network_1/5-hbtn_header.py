#!/usr/bin/python3
"""
Displays the value of X-Request-Id
"""


if __name__ == '__main__':
    from requests import get
    from sys import argv
    request = get(argv[1])
    print(request.headers.get('X-Request-Id'))
