#!/usr/bin/python3
"""
A script that sends a POST request with an email as a parameter
and displays the body of the response (decoded in utf-8).
"""
from sys import argv
from urllib import parse, request

if __name__ == "__main__":
    url = argv[1]
    email = argv[2]
    data = parse.urlencode({"email": email}).encode()
    req = request.Request(url, data=data, method="POST")
    with request.urlopen(req) as response:
        print(response.read().decode("utf-8"))
