#!/usr/bin/python3
"""
Displays the value of the X-Request-Id variable
"""


if __name__ == '__main__':
    import urllib.request
    import urllib.parse
    import sys

    with urllib.request.urlopen(sys.argv[1]) as reply:
        html = reply.info()
        print('{}'.format(html.get('X-Request-ID')))
