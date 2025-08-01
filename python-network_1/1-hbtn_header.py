#!/usr/bin/python3
"""
Write script that takes in a URL,sends a request to URL and displays the value
of the X-Request-Id variable found in the header ofthe response.
"""
from sys import argv
from urllib import request

if __name__ == "__main__":
    url = argv[1]
    with request.urlopen(url) as response:
        print(response.info().get("X-Request-Id"))
